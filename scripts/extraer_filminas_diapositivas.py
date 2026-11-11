"""
extraer_filminas_diapositivas.py
---------------------------------
Extrae automáticamente imágenes de alta resolución de las diapositivas/filminas
expuestas en los videos de las diplomaturas, filtrando tomas de personas/webcams
mediante visión artificial (densidad de bordes, histograma de fondo, máscara de piel YCrCb)
y deduplicando láminas consecutivas.

Asocia cada filmina a:
1. Carpeta dedicada por video: `diapositivas/<video_id>/`
2. Nomenclatura secuencial: `<index:02d>_<HH-MM-SS>_<tema-sanitizado>.jpg`
3. Vinculación con timestamps de la transcripción y actualización de notas Obsidian .md.
"""

import os
import sys
import json
import re
import math
import subprocess
import shutil
import unicodedata
import cv2
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

# Directorios y rutas clave
REPO_ROOT = r'C:\Users\jidiaz\.gemini\antigravity-ide\scratch\antigravity-agents-repository'
FFMPEG_EXE = os.path.join(REPO_ROOT, 'scripts', 'ffmpeg.exe')
CATALOG_PATH = os.path.join(REPO_ROOT, 'docs', 'Cursos', 'catalogo_descargas_videos.json')
DOCS_CURSOS = os.path.join(REPO_ROOT, 'docs', 'Cursos')
TEMP_STAGING = r'D:\Usuarios\jidiaz\.gemini\antigravity-ide\scratch\temp_slide_staging'

os.makedirs(TEMP_STAGING, exist_ok=True)

# Palabras clave y regex de transición de diapositivas en transcripción
TRANSITION_PATTERNS = [
    r'(?:en esta|en la|en la siguiente|vemos en la|miramos la)\s+(?:diapositiva|filmina|l[aá]mina|presentaci[oó]n|imagen|pantalla|gr[aá]fica|tabla|figura)',
    r'(?:en este|en el siguiente)\s+(?:gr[aá]fico|cuadro|esquema|diagrama|mapa|eje|punto|art[ií]culo|procedimiento|circuito)',
    r'(?:ac[aá] vemos|aqu[ií] vemos|como muestra|como se ve ac[aá]|pasamos a|vean este|comparto|proyectamos|siguiente slide|slide)',
    r'(?:vamos a ver|observen ac[aá]|f[ií]jense en|en pantalla|curva de|estructura de|definici[oó]n de)'
]
TRANSITION_REGEX = re.compile('|'.join(TRANSITION_PATTERNS), re.IGNORECASE)

STOPWORDS = {
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'de', 'del', 'a', 'al', 'en', 'para',
    'por', 'con', 'sin', 'sobre', 'entre', 'que', 'se', 'es', 'son', 'fue', 'era', 'muy', 'mas',
    'más', 'pero', 'como', 'cuando', 'donde', 'dónde', 'este', 'esta', 'estos', 'estas', 'esto',
    'ese', 'esa', 'esos', 'esas', 'aqui', 'acá', 'aca', 'ahi', 'ahí', 'alla', 'allá', 'todo',
    'toda', 'todos', 'todas', 'bien', 'bueno', 'entonces', 'ahora', 'tambien', 'también', 'nos',
    'les', 'nosotros', 'ustedes', 'ellos', 'ellas', 'su', 'sus', 'mi', 'mis', 'tu', 'tus', 'si',
    'sí', 'no', 'ya', 'o', 'u', 'e', 'y', 'vamos', 'vemos', 'decir', 'hacer', 'tener', 'estar',
    'música', 'aplausos', 'risas', 'hola', 'gracias', 'buenas', 'tardes', 'dias', 'días', 'noches'
}


def sanitize_filename(text: str, max_words: int = 5) -> str:
    """Sanitiza y normaliza un texto para generar un slug kebab-case limpio."""
    if not text:
        return "tema-general"
    # Normalizar acentos
    nfkd = unicodedata.normalize('NFKD', text)
    ascii_text = ''.join([c for c in nfkd if not unicodedata.combining(c)])
    # Limpiar caracteres especiales
    clean = re.sub(r'[^a-zA-Z0-9\s]', ' ', ascii_text).lower()
    words = [w for w in clean.split() if w not in STOPWORDS and len(w) > 2]
    if not words:
        words = [w for w in clean.split() if len(w) > 1]
    selected_words = words[:max_words] if words else ["diapositiva"]
    slug = '-'.join(selected_words)
    return slug[:40] if slug else "tema-general"


def format_timestamp(seconds: float) -> str:
    """Convierte segundos a HH-MM-SS para nombres de archivo."""
    s = int(round(seconds))
    h = s // 3600
    m = (s % 3600) // 60
    sec = s % 60
    return f"{h:02d}-{m:02d}-{sec:02d}"


def format_timestamp_display(seconds: float) -> str:
    """Convierte segundos a HH:MM:SS para texto visible."""
    s = int(round(seconds))
    h = s // 3600
    m = (s % 3600) // 60
    sec = s % 60
    return f"{h:02d}:{m:02d}:{sec:02d}"


def parse_duration_to_seconds(dur_str: str) -> float:
    """Parsea duraciones tipo '153m 10s' o '0m 53s' o '2h 30m' a segundos."""
    if not dur_str:
        return 0.0
    total = 0.0
    h_match = re.search(r'(\d+)\s*h', dur_str)
    m_match = re.search(r'(\d+)\s*m', dur_str)
    s_match = re.search(r'(\d+)\s*s', dur_str)
    if h_match:
        total += float(h_match.group(1)) * 3600
    if m_match:
        total += float(m_match.group(1)) * 60
    if s_match:
        total += float(s_match.group(1))
    return total


def is_presentation_slide(img: np.ndarray) -> tuple[bool, str, dict]:
    """
    Analiza una imagen mediante visión artificial para determinar si es
    una diapositiva/filmina o una toma de persona/cámara web/fondo vacío.
    """
    if img is None or img.size == 0:
        return False, "Imagen vacía o corrupta", {}

    h, w, c = img.shape
    total_pixels = h * w

    # 1. Comprobación de dimensiones mínimas
    if w < 640 or h < 360:
        return False, f"Resolución insuficiente ({w}x{h})", {}

    # 2. Análisis de brillo y contraste (descartar pantallas negras o blancas uniformes)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mean_val = float(np.mean(gray))
    std_val = float(np.std(gray))
    if mean_val < 20 or mean_val > 248 or std_val < 14:
        return False, f"Pantalla negra o plana (mean={mean_val:.1f}, std={std_val:.1f})", {}

    # 3. Detección de piel humana (YCrCb) para filtrar cámaras web / personas en primer plano
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    skin_mask = cv2.inRange(ycrcb, np.array([0, 133, 77]), np.array([255, 173, 127]))
    skin_ratio = float(np.count_nonzero(skin_mask)) / total_pixels

    # Si más del 16% del cuadro es piel humana -> es un expositor/persona, no filmina
    if skin_ratio > 0.16:
        return False, f"Toma de persona/webcam predominante (SkinRatio={skin_ratio:.3f})", {"skin": skin_ratio}

    # 4. Densidad de bordes (Canny) - Las diapositivas tienen texto y diagramas nítidos
    edges = cv2.Canny(gray, 50, 150)
    edge_ratio = float(np.count_nonzero(edges)) / total_pixels
    if edge_ratio < 0.007:
        return False, f"Baja densidad de bordes (EdgeRatio={edge_ratio:.4f})", {"edge": edge_ratio}

    # 5. Pico de color dominante (histograma 3D) - Diapositivas tienen lienzo/fondo uniforme
    hist = cv2.calcHist([img], [0, 1, 2], None, [16, 16, 16], [0, 256, 0, 256, 0, 256])
    color_peak = float(np.max(hist)) / total_pixels
    if color_peak < 0.15:
        return False, f"Falta de fondo uniforme de diapositiva (ColorPeak={color_peak:.3f})", {"color_peak": color_peak}

    metrics = {
        "edge_ratio": round(edge_ratio, 4),
        "skin_ratio": round(skin_ratio, 4),
        "color_peak": round(color_peak, 4),
        "mean": round(mean_val, 1),
        "std": round(std_val, 1)
    }
    return True, "Diapositiva válida", metrics


def compute_image_difference(img1: np.ndarray, img2: np.ndarray) -> float:
    """Calcula la diferencia perceptual (MSE sobre imagen normalizada a 64x36)."""
    g1 = cv2.cvtColor(cv2.resize(img1, (64, 36)), cv2.COLOR_BGR2GRAY)
    g2 = cv2.cvtColor(cv2.resize(img2, (64, 36)), cv2.COLOR_BGR2GRAY)
    diff = np.mean((g1.astype("float") - g2.astype("float")) ** 2)
    return float(diff)


def load_transcript(video_id: str, course_subfolder: str) -> list[dict]:
    """Carga la transcripción raw o parsea el archivo de texto minutado."""
    # Buscar en carpeta transcripciones de ambos cursos
    search_dirs = [
        os.path.join(DOCS_CURSOS, course_subfolder, 'transcripciones'),
        os.path.join(DOCS_CURSOS, 'Diplomatura-Energia-Electrica', 'transcripciones'),
        os.path.join(DOCS_CURSOS, 'Diplomatura-Transicion-Energetica', 'transcripciones')
    ]
    
    for sdir in search_dirs:
        if not os.path.exists(sdir):
            continue
        raw_json = os.path.join(sdir, f"{video_id}_transcript_raw.json")
        if os.path.exists(raw_json):
            try:
                with open(raw_json, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list) and len(data) > 0:
                        return data
            except Exception:
                pass
        
        timed_txt = os.path.join(sdir, f"{video_id}_transcript_timed.txt")
        if os.path.exists(timed_txt):
            try:
                entries = []
                with open(timed_txt, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        m = re.match(r'\[(\d+):(\d+):(\d+)\]\s*(.*)', line)
                        if m:
                            hh, mm, ss, txt = int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)
                            sec = hh * 3600 + mm * 60 + ss
                            entries.append({"start": sec, "duration": 4.0, "text": txt})
                if entries:
                    return entries
            except Exception:
                pass
    return []


DISCOURSE_FILLERS = [
    r'^(?:bueno|como dec[ií]a|este|digamos|entonces|vean|ac[aá]|vamos a ver|f[ií]jense|ok|okay|un poco|les dec[ií]a|comentaba|por ejemplo|la idea es|ac[aá] tenemos)\s*,?\s*',
    r'^(?:tenemos|podemos|vemos|vamos a|empezamos por|arrancamos con|pasamos a|despu[eé]s)\s*,?\s*'
]
DISCOURSE_REGEX = re.compile('|'.join(DISCOURSE_FILLERS), re.IGNORECASE)

TECHNICAL_KEYWORDS = [
    'mercado electrico mayorista', 'marco regulatorio', 'ley 24065', 'ley 11769', 'cammesa', 'sadi',
    'matriz energetica', 'balance energetico', 'generacion distribuida', 'redes de distribucion',
    'lineas de transmision', 'transformador de potencia', 'caida de tension', 'flujo de potencia',
    'calidad de servicio', 'saidi', 'saifi', 'cortocircuito', 'protecciones electricas', 'flicker',
    'energia solar fotovoltaica', 'energia eolica', 'biomasa', 'hidroelectrica', 'baterias de litio',
    'almacenamiento bsf', 'hidrogeno verde', 'movilidad electrica', 'tarifa electrica', 'subsidios',
    'peajes de transporte', 'despacho economico', 'costo marginal', 'perdidas tecnicas y no tecnicas',
    'telemedicion', 'smart grids', 'medidores inteligentes', 'eficiencia energetica', 'factor de potencia',
    'compensacion reactiva', 'banco de capacitores', 'subestacion transformadora', 'curva de carga'
]


def extract_topic_from_transcript(transcript: list[dict], timestamp: float, window_sec: float = 35.0) -> tuple[str, str]:
    """Extrae el tema tratado y un extracto de texto representativo alrededor del timestamp."""
    if not transcript:
        return "presentacion-de-catedra", "Exposición temática de cátedra."

    start_w = max(0, timestamp - 5.0)
    end_w = timestamp + window_sec
    relevant_texts = [
        e['text'].strip() for e in transcript
        if (e.get('start', 0) >= start_w and e.get('start', 0) <= end_w)
    ]
    full_snippet = " ".join(relevant_texts).strip()
    if not full_snippet:
        past_entries = [e for e in transcript if e.get('start', 0) <= timestamp]
        if past_entries:
            full_snippet = past_entries[-1]['text'].strip()
        else:
            full_snippet = "Desarrollo conceptual de cátedra."

    # Limpiar corchetes y fillers
    clean_snippet = re.sub(r'\[.*?\]', '', full_snippet).strip()
    trimmed = clean_snippet
    for _ in range(3):
        trimmed = DISCOURSE_REGEX.sub('', trimmed).strip()

    # Verificar si hay palabras clave técnicas relevantes en la ventana
    lower_context = clean_snippet.lower()
    matched_tech = None
    for kw in TECHNICAL_KEYWORDS:
        if kw in lower_context:
            matched_tech = kw
            break

    if matched_tech:
        topic_slug = sanitize_filename(matched_tech, max_words=5)
    else:
        topic_slug = sanitize_filename(trimmed if len(trimmed) > 10 else clean_snippet, max_words=5)

    return topic_slug, clean_snippet[:200]


def process_video_slides(video_item: dict, output_base_dir: str) -> dict:
    """Procesa un video completo: extrae fotogramas, filtra con IA/CV y guarda las filminas."""
    video_id = video_item['video_id']
    course_subfolder = video_item.get('target_subfolder', 'Diplomatura-Energia-Electrica')
    title = video_item.get('title', f'Video {video_id}')
    duration_str = video_item.get('duration', '0m')
    duration_sec = parse_duration_to_seconds(duration_str)
    
    # Localizar archivo MP4
    mp4_path = video_item.get('mp4_path')
    if not mp4_path or not os.path.exists(mp4_path):
        # Buscar en red
        net_dir = r'\\srvfs01\ProyectoTelemedicion\13-Documentacion_Tutoriales_Videos_Instaladores\cursos_videos_diplomaturas'
        found = None
        for root, dirs, files in os.walk(net_dir):
            for f in files:
                if f.endswith('.mp4') and f"[{video_id}]" in f:
                    found = os.path.join(root, f)
                    break
            if found:
                break
        mp4_path = found

    if not mp4_path or not os.path.exists(mp4_path):
        return {"video_id": video_id, "status": "ERROR", "message": f"Archivo MP4 no encontrado para {video_id}"}

    # Protocolo de Snapshot Local de Mínima Interferencia de Red
    try:
        from network_snapshot import get_local_snapshot
        mp4_path = str(get_local_snapshot(mp4_path))
    except Exception as e_snap:
        print(f"Aviso snapshot de red: {e_snap}, intentando ruta directa...")

    # Carpeta de salida de diapositivas para este video
    # docs/Cursos/<Course_Subfolder>/diapositivas/<video_id>/
    video_slide_dir = os.path.join(output_base_dir, 'diapositivas', video_id)
    os.makedirs(video_slide_dir, exist_ok=True)

    # Cargar transcripción
    transcript = load_transcript(video_id, course_subfolder)
    
    # Recopilar timestamps candidatos:
    # 1. Momentos con palabras clave de cambio de filmina
    cue_timestamps = set()
    for entry in transcript:
        txt = entry.get('text', '')
        if TRANSITION_REGEX.search(txt):
            ts = entry.get('start', 0)
            # Agregar timestamp + 2 segundos para asegurar renderizado completo de la lámina
            cue_timestamps.add(round(ts + 2.0, 1))

    # 2. Muestreo regular cada 40 segundos a lo largo del video
    if duration_sec <= 0:
        duration_sec = 3600.0  # fallback 1 hora si no se detectó
    
    grid_timestamps = np.arange(15.0, duration_sec - 10.0, 40.0).tolist()
    all_candidate_ts = sorted(list(cue_timestamps.union(set(grid_timestamps))))

    print(f"\n▶ Procesando Video [{video_id}]: '{title[:55]}...'")
    print(f"  Duración: {duration_sec:.0f}s ({duration_str}) | Candidatos a evaluar: {len(all_candidate_ts)}")

    extracted_slides = []
    prev_slide_img = None
    slide_idx = 1

    temp_frame_path = os.path.join(TEMP_STAGING, f"temp_{video_id}.jpg")

    for ts in all_candidate_ts:
        # Extraer frame con ffmpeg
        cmd = [
            FFMPEG_EXE, '-y',
            '-ss', str(ts),
            '-i', mp4_path,
            '-vframes', '1',
            '-q:v', '2',
            temp_frame_path
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not os.path.exists(temp_frame_path) or os.path.getsize(temp_frame_path) < 1000:
            continue

        img = cv2.imread(temp_frame_path)
        if img is None:
            continue

        is_slide, reason, metrics = is_presentation_slide(img)
        if not is_slide:
            continue

        # Comprobar si es una filmina duplicada respecto a la anterior
        if prev_slide_img is not None:
            diff = compute_image_difference(img, prev_slide_img)
            # Si la diferencia perceptual es menor a 9.0 -> es la misma diapositiva
            if diff < 9.0:
                continue

        # Diapositiva nueva y válida confirmada
        topic_slug, snippet = extract_topic_from_transcript(transcript, ts)
        time_str = format_timestamp(ts)
        time_disp = format_timestamp_display(ts)

        filename = f"{slide_idx:02d}_{time_str}_{topic_slug}.jpg"
        final_img_path = os.path.join(video_slide_dir, filename)
        
        # Guardar en alta calidad
        cv2.imwrite(final_img_path, img, [cv2.IMWRITE_JPEG_QUALITY, 95])
        prev_slide_img = img.copy()

        rel_path = f"diapositivas/{video_id}/{filename}"
        extracted_slides.append({
            "index": slide_idx,
            "timestamp": ts,
            "timestamp_str": time_disp,
            "filename": filename,
            "relative_path": rel_path,
            "topic": topic_slug.replace('-', ' ').title(),
            "snippet": snippet,
            "metrics": metrics
        })
        print(f"  [+] Filmina {slide_idx:02d} @ {time_disp} -> {filename} ({metrics.get('edge_ratio')} bordes, {metrics.get('color_peak')} fondo)")
        slide_idx += 1

    # Limpiar temporal
    if os.path.exists(temp_frame_path):
        try:
            os.remove(temp_frame_path)
        except Exception:
            pass

    return {
        "video_id": video_id,
        "title": title,
        "duration": duration_str,
        "total_slides": len(extracted_slides),
        "slides": extracted_slides,
        "status": "OK"
    }


def update_markdown_note(md_filepath: str, slide_results: dict):
    """Actualiza la nota Obsidian .md con la galería y secuencia de filminas extraídas."""
    if not os.path.exists(md_filepath):
        return False

    with open(md_filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    video_id = slide_results['video_id']
    slides = slide_results.get('slides', [])
    total = len(slides)

    # Construir sección de diapositivas
    slide_section = f"## 🖼️ Registro y Desglose Exhaustivo de Diapositivas Proyectadas\n\n"
    slide_section += f"> **Total de Diapositivas / Filminas Identificadas**: `{total}` láminas de presentación.\n"
    slide_section += f"> **Algoritmo de Detección**: Visión artificial con filtrado de expositores/webcam, detección morfológica de texto y vinculación minutada con transcripción de audio.\n\n"

    if total == 0:
        slide_section += f"*No se identificaron diapositivas proyectadas continuas en este video (sesión netamente expositiva o sin filminas detectables).*\n\n"
    else:
        slide_section += f"| N° | Timestamp | Tema / Eje Conceptual de la Filmina | Previsualización y Vínculo de Archivo |\n"
        slide_section += f"| :-: | :--- | :--- | :--- |\n"
        for s in slides:
            idx = s['index']
            ts_str = s['timestamp_str']
            topic = s['topic']
            snippet = s['snippet']
            rel_p = s['relative_path']
            slide_section += f"| **{idx:02d}** | `⏱️ {ts_str}` | **{topic}**<br>_{snippet}_ | ![{topic}]({rel_p})<br>[`{s['filename']}`](file:///{os.path.join(os.path.dirname(md_filepath), rel_p).replace(chr(92), '/')}) |\n"
        slide_section += "\n"

    # Reemplazar o insertar sección
    if re.search(r'## 🖼️ Registro y Desglose.*?Diapositivas Proyectadas.*?(?=\n## |\Z)', content, re.DOTALL):
        new_content = re.sub(
            r'## 🖼️ Registro y Desglose.*?Diapositivas Proyectadas.*?(?=\n## |\Z)',
            slide_section + "\n---\n\n",
            content,
            flags=re.DOTALL
        )
    else:
        # Insertar antes de Conceptos Clave
        if "## 💡 1. Conceptos Clave" in content:
            new_content = content.replace("## 💡 1. Conceptos Clave", slide_section + "\n---\n\n## 💡 1. Conceptos Clave")
        else:
            new_content = content + "\n\n---\n\n" + slide_section

    with open(md_filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Extractor de diapositivas")
    parser.add_argument("--limit", type=int, default=0, help="Limitar cantidad de videos a procesar")
    parser.add_argument("--video-id", type=str, default=None, help="Procesar solo un video_id específico")
    args = parser.parse_args()

    print("=" * 80)
    print("🚀 PROCESADOR Y EXTRACTOR MASIVO DE DIAPOSITIVAS Y FILMINAS DE CURSOS")
    print("=" * 80)

    with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    print(f"Catálogo cargado: {len(catalog)} videos registrados.")

    # Prioridad: 1) Diplomatura-Energia-Electrica, 2) Diplomatura-Transicion-Energetica
    ee_videos = [v for v in catalog if 'Diplomatura-Energia-Electrica' in v.get('target_subfolder', '')]
    te_videos = [v for v in catalog if 'Diplomatura-Transicion-Energetica' in v.get('target_subfolder', '')]

    ordered_videos = ee_videos + te_videos

    if args.video_id:
        ordered_videos = [v for v in ordered_videos if v.get('video_id') == args.video_id]
        print(f"Filtrando por video_id: {args.video_id} ({len(ordered_videos)} coincidencia)")
    elif args.limit > 0:
        ordered_videos = ordered_videos[:args.limit]
        print(f"Limitando ejecución a los primeros {args.limit} videos.")

    print(f"  - Total videos a procesar en esta corrida: {len(ordered_videos)}")

    summary_results = []

    for i, item in enumerate(ordered_videos, start=1):
        v_id = item['video_id']
        subfolder = item.get('target_subfolder', 'Diplomatura-Energia-Electrica')
        course_dir = os.path.join(DOCS_CURSOS, subfolder)
        
        print(f"\n[{i}/{len(ordered_videos)}] ===================================================")
        res = process_video_slides(item, course_dir)
        summary_results.append(res)

        # Actualizar notas markdown asociadas
        md_file = item.get('filepath')
        if md_file and os.path.exists(md_file):
            update_markdown_note(md_file, res)
            print(f"  [✓] Nota Markdown actualizada: {os.path.basename(md_file)}")

        # También buscar si hay notas duplicadas con nombre sanitizado en el directorio
        for f in os.listdir(course_dir):
            if f.endswith('.md') and not f.startswith('00-') and f != os.path.basename(md_file or ''):
                full_f = os.path.join(course_dir, f)
                try:
                    with open(full_f, 'r', encoding='utf-8') as fp:
                        txt_head = fp.read(400)
                        if f"video_id: \"{v_id}\"" in txt_head:
                            update_markdown_note(full_f, res)
                            print(f"  [✓] Nota Markdown homóloga actualizada: {f}")
                except Exception:
                    pass

    # Guardar resumen final
    summary_path = os.path.join(DOCS_CURSOS, "resumen_extraccion_diapositivas.json")
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary_results, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 80)
    print("✨ PROCESO COMPLETADO EXITOSAMENTE")
    print(f"Resumen general guardado en: {summary_path}")
    print("=" * 80)


if __name__ == '__main__':
    main()
