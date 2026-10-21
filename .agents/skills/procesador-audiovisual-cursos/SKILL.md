---
name: procesador-audiovisual-cursos
description: Especialista en ingesta masiva de cursos audiovisuales (YouTube/MP4), transcripción minutada, extracción y filtrado de diapositivas con visión artificial (OpenCV/YCrCb), deduplicación perceptual y generación de documentación enriquecida en Obsidian.
---

# 🎓 Skill: Procesador y Analizador Audiovisual de Cursos Académicos

Esta habilidad define el estándar de excelencia operativa para procesar grabaciones de cursos, conferencias y diplomaturas, extrayendo tanto el audio minutado como las diapositivas de alta resolución, clasificándolas con visión artificial y generando notas de conocimiento interconectadas en Obsidian.

---

## 🛠️ Pipeline de 5 Fases

```
[1. Ingesta y Catálogo] ➔ [2. Transcripción Minutada] ➔ [3. Visión Artificial & Slides] ➔ [4. Naming & Deduplicación] ➔ [5. Documentación Obsidian]
```

### 1. Ingesta y Catálogo JSON
- **Objetivo**: Descargar o localizar los archivos de video `.mp4` en el almacenamiento local o de red (`\\srvfs01\...`).
- **Registro Central**: Mantener `docs/Cursos/catalogo_descargas_videos.json` con `video_id`, `url`, `title`, `duration`, `target_subfolder`, y rutas de archivo.

### 2. Transcripción de Audio y Minutado
- **Archivos Generados**:
  - `transcripciones/<video_id>_transcript_raw.json`: Lista de objetos `{"start": float, "duration": float, "text": str}`.
  - `transcripciones/<video_id>_transcript_timed.txt`: Archivo estructurado `[HH:MM:SS] Texto pronunciado`.
- **Detección de Transiciones Verbales**: Identificar marcadores lingüísticos como `"en esta diapositiva"`, `"en este gráfico"`, `"vemos en la siguiente lámina"`, `"este esquema"`, `"curva de carga"`, `"ley 24065"`.

### 3. Visión Artificial y Filtrado de Personas/Webcam
Para cada cuadro candidato extraído vía FFmpeg (`-ss <timestamp> -vframes 1 -q:v 2`):
1. **Espacio de Color YCrCb (Máscara de Piel)**:
   - Rango: `Y in [0, 255]`, `Cr in [133, 173]`, `Cb in [77, 127]`.
   - Si `SkinRatio > 0.16` (más del 16% del cuadro es rostro/piel humana) $\rightarrow$ **Descartar** (toma de expositor/webcam).
2. **Densidad de Bordes (Canny)**:
   - Umbral: `cv2.Canny(gray, 50, 150)`.
   - Si `EdgeRatio < 0.007` $\rightarrow$ **Descartar** (pantalla plana, fondo liso o sin contenido técnico).
3. **Pico de Color Dominante (Histograma 3D)**:
   - Matriz 16x16x16: si `ColorPeak < 0.15` $\rightarrow$ **Descartar** (falta de fondo de lienzo/slide continuo).
4. **Varianza y Brillo**:
   - `Mean in [20, 248]`, `Std > 14` (evita pantallas negras o blancas saturadas).

### 4. Deduplicación Perceptual y Nomenclatura Estructurada
- **Deduplicación**: Comparar fotogramas válidos consecutivos redimensionados a 64x36 en escala de grises mediante Mean Squared Error (MSE). Si $\text{MSE} < 9.0$, se considera la misma filmina proyectada.
- **Nomenclatura Estándar**:  
  `diapositivas/<video_id>/<index:02d>_<HH-MM-SS>_<tema-sanitizado>.jpg`
  - Sanitización en minúsculas, sin acentos ni caracteres especiales, removiendo *fillers* conversacionales (`"bueno"`, `"digamos"`, `"como decía"`) y priorizando sustantivos técnicos (`mercado-electrico`, `curva-de-carga`, `lineas-transmision`, `sadi-cammesa`).

### 5. Documentación Enriquecida en Obsidian
- Insertar en la nota `.md` de cátedra:
  - Ficha técnica completa (enlace YouTube, archivo de red, duración, IDs).
  - Sección `## 🖼️ Registro y Desglose Exhaustivo de Diapositivas Proyectadas` con tabla embebida:
    - Previsualización: `![Tema](diapositivas/<video_id>/<filename>)`
    - Insignia de tiempo: `⏱️ HH:MM:SS`
    - Extracto textual de la transcripción correspondiente.
    - Enlace clickable directo al archivo local `file:///...`.
  - Desglose temático en 6 ejes (Conceptos clave, Observaciones, Casos de éxito, Inconvenientes, Dudas y Planificación).
  - Circuito dialéctico de 10 iteraciones [[docs/Agentes/09-Profesor-Experto-Mercado-Electrico]] vs [[docs/Agentes/10-Alumno-Auditor-Academico]].

---

## 💻 Herramientas y Scripts Asociados
- [`scripts/descargar_videos_cursos.py`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/descargar_videos_cursos.py)
- [`scripts/procesar_todas_transcripciones_y_documentacion.py`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/procesar_todas_transcripciones_y_documentacion.py)
- [`scripts/extraer_filminas_diapositivas.py`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/extraer_filminas_diapositivas.py)
- [`scripts/circuito_profesor_alumno_10_iteraciones.py`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/circuito_profesor_alumno_10_iteraciones.py)
