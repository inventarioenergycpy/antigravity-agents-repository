import os
import re
import json
import sys
import shutil
import argparse
from pathlib import Path

# Fix Windows console encoding for UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Paths
REPO_ROOT = Path(r"D:\Usuarios\jidiaz\.gemini\antigravity-ide\scratch\antigravity-agents-repository")
CURSOS_DIR = REPO_ROOT / "docs" / "Cursos"
DEST_BASE_DIR = Path(r"\\srvfs01\ProyectoTelemedicion\13-Documentacion_Tutoriales_Videos_Instaladores\cursos_videos_diplomaturas")
LOCAL_STAGING_DIR = Path(r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\temp_video_staging")
FFMPEG_EXE = REPO_ROOT / "scripts" / "ffmpeg.exe"

def sanitize_clean_name(name):
    # Remove emojis, non-standard quotes, brackets and invalid Windows chars
    clean = name.replace("🔴", "").replace("PROXIMAMENTE!", "").replace('"', '').replace("'", "")
    clean = clean.replace("“", "").replace("”", "").replace("＂", "").replace(":", "-").replace("|", "-")
    clean = re.sub(r'[\\/*?:"<>|]', "-", clean)
    clean = re.sub(r'[^\w\s\-\.\,\(\)\[\]]', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:75]

def normalize_target_subfolder(rel_folder):
    rf = str(rel_folder).replace("\\", "/")
    
    if "Diplomatura-Energia-Electrica" in rf:
        return "Diplomatura-Energia-Electrica"
    elif "Modulo-03" in rf or "MÓDULO-03" in rf or "Almacenamiento" in rf:
        return "Diplomatura-Transicion-Energetica/Modulo-03-Almacenamiento"
    elif "Modulo-04" in rf or "MÓDULO-04" in rf or "Transporte" in rf:
        return "Diplomatura-Transicion-Energetica/Modulo-04-Transporte-Energetico"
    elif "Modulo-05" in rf or "MÓDULO-05" in rf or "Regulaciones" in rf:
        return "Diplomatura-Transicion-Energetica/Modulo-05-Regulaciones"
    elif "Modulo-06" in rf or "MÓDULO-06" in rf or "Beneficios" in rf:
        return "Diplomatura-Transicion-Energetica/Modulo-06-Beneficios-y-Politicas"
    elif "Transici" in rf:
        return "Diplomatura-Transicion-Energetica/General"
    else:
        clean = re.sub(r'[\\/*?:"<>|]', "", rf)
        return clean.replace(" ", "-")

def scan_and_deduplicate_courses():
    unique_videos = {}
    
    for root, dirs, files in os.walk(CURSOS_DIR):
        for file in sorted(files):
            if file.endswith(".md") and not file.startswith("00-") and file != "README.md":
                filepath = Path(root) / file
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                except Exception as e:
                    print(f"[WARN] Error al leer {filepath}: {e}")
                    continue
                
                vid_match = re.search(r'video_id:\s*["\']?([^"\'\n\r]+)', content)
                url_match = re.search(r'url:\s*["\']?([^"\'\n\r]+)', content)
                title_match = re.search(r'title:\s*["\']?([^"\'\n\r]+)', content)
                dur_match = re.search(r'duracion:\s*["\']?([^"\'\n\r]+)', content)
                
                video_id = vid_match.group(1).strip() if vid_match else None
                url = url_match.group(1).strip() if url_match else None
                title = title_match.group(1).strip() if title_match else file.replace(".md", "")
                dur = dur_match.group(1).strip() if dur_match else "N/A"
                
                if not url and video_id:
                    url = f"https://www.youtube.com/watch?v={video_id}"
                
                if video_id:
                    rel_folder = Path(root).relative_to(CURSOS_DIR)
                    canonical_folder = normalize_target_subfolder(rel_folder)
                    
                    if video_id not in unique_videos:
                        unique_videos[video_id] = {
                            "video_id": video_id,
                            "url": url,
                            "title": title,
                            "duration": dur,
                            "target_subfolder": canonical_folder,
                            "original_file": file,
                            "filepath": str(filepath)
                        }
                        
    return list(unique_videos.values())

def download_video(video_info, dest_folder, yt_dlp_module):
    video_id = video_info["video_id"]
    url = video_info["url"]
    title = video_info["title"]
    clean_base = sanitize_clean_name(title)
    
    # Ensure dest_folder exists
    dest_folder.mkdir(parents=True, exist_ok=True)
    
    # Check if a completed mp4 with this video_id already exists in dest_folder
    existing = list(dest_folder.glob(f"*{video_id}*.mp4"))
    if existing:
        size_mb = existing[0].stat().st_size / (1024 * 1024)
        print(f"  ⏭️ [OMITIDO] Ya existe en red ({size_mb:.1f} MB): {existing[0].name}")
        return True, "Ya existente"
        
    print(f"  ⬇️ [DESCARGANDO] {clean_base} [{video_id}]")
    print(f"     🔗 URL: {url} ➔ 📁 Destino: {dest_folder.name}")
    
    LOCAL_STAGING_DIR.mkdir(parents=True, exist_ok=True)
    clean_out_name = f"{clean_base} [{video_id}]"
    temp_template = str(LOCAL_STAGING_DIR / f"{clean_out_name}.%(ext)s")
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'ffmpeg_location': str(FFMPEG_EXE),
        'outtmpl': temp_template,
        'quiet': False,
        'no_warnings': True,
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'retries': 5,
        'fragment_retries': 5,
    }
    
    try:
        with yt_dlp_module.YoutubeDL(ydl_opts) as ydl:
            retcode = ydl.download([url])
            
        # Find the produced mp4 file in LOCAL_STAGING_DIR
        staged_files = list(LOCAL_STAGING_DIR.glob(f"*{video_id}*.mp4"))
        if staged_files and retcode == 0:
            staged_file = staged_files[0]
            clean_filename = f"{clean_base} [{video_id}].mp4"
            target_file = dest_folder / clean_filename
            size_mb = staged_file.stat().st_size / (1024 * 1024)
            print(f"  📦 [TRASLADANDO A RED] {clean_filename} ({size_mb:.1f} MB)...")
            
            # Copy and remove for robust UNC transfer
            shutil.copy2(str(staged_file), str(target_file))
            staged_file.unlink()
            
            print(f"  ✅ [OK] Guardado en servidor: {target_file}")
            return True, "Completado"
        else:
            print(f"  ⚠️ [WARN] No se encontró archivo combinado o retcode {retcode}")
            return False, f"Retcode {retcode}"
            
    except Exception as e:
        print(f"  ❌ [ERROR] Falló la descarga de {url}: {e}")
        return False, str(e)
    finally:
        # Clean any leftovers in staging
        for leftover in LOCAL_STAGING_DIR.glob(f"*{video_id}*"):
            try:
                leftover.unlink()
            except Exception:
                pass

def main():
    parser = argparse.ArgumentParser(description="Descargador de videos de cursos y diplomaturas a red")
    parser.add_argument("--dry-run", action="store_true", help="Solo escanear y catalogar sin descargar")
    parser.add_argument("--limit", type=int, default=0, help="Limitar número de descargas (0 = todos)")
    parser.add_argument("--filter", type=str, default="", help="Filtrar por subcarpeta o nombre")
    args = parser.parse_args()
    
    print("=" * 85)
    print(" 🎬 DESCARGADOR AUTOMÁTICO DE CURSOS Y DIPLOMATURAS - AGENTE 07 YOUTUBE")
    print("=" * 85)
    print(f"Directorio Origen Obsidian: {CURSOS_DIR}")
    print(f"Directorio Destino en Red:  {DEST_BASE_DIR}")
    print("-" * 85)
    
    if not DEST_BASE_DIR.exists():
        try:
            DEST_BASE_DIR.mkdir(parents=True, exist_ok=True)
            print(f"[INFO] Creada carpeta base en red: {DEST_BASE_DIR}")
        except Exception as e:
            print(f"[ERROR] No se pudo acceder o crear la carpeta en red: {e}")
            sys.exit(1)
    else:
        print("[OK] Acceso verificado al recurso compartido de red.")
        
    catalog = scan_and_deduplicate_courses()
    print(f"[OK] Se descubrieron {len(catalog)} videos ÚNICOS en la base de datos de Obsidian.\n")
    
    # Summary by canonical subfolder
    folders = {}
    for item in catalog:
        f = item["target_subfolder"]
        folders[f] = folders.get(f, 0) + 1
        
    print("📂 Distribución Canónica en el Almacenamiento de Red:")
    for f, count in sorted(folders.items()):
        print(f"  📁 {f}: {count} videos")
    print("-" * 85)
    
    # Apply filters if specified
    filtered_catalog = catalog
    if args.filter:
        filtered_catalog = [v for v in catalog if args.filter.lower() in v["target_subfolder"].lower() or args.filter.lower() in v["title"].lower()]
        print(f"[FILTRO] Aplicado filtro '{args.filter}': {len(filtered_catalog)} videos seleccionados.")
        
    if args.limit > 0:
        filtered_catalog = filtered_catalog[:args.limit]
        print(f"[LÍMITE] Procesando los primeros {args.limit} videos.")
        
    # Save catalog summary json
    catalog_json = REPO_ROOT / "docs" / "Cursos" / "catalogo_descargas_videos.json"
    with open(catalog_json, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print(f"[OK] Catálogo sincronizado en: {catalog_json}\n")
    
    if args.dry_run:
        print("🔍 MODO SIMULACIÓN (DRY-RUN) ACTIVO. No se descargarán archivos:")
        for idx, item in enumerate(filtered_catalog, 1):
            clean_t = sanitize_clean_name(item['title'])
            print(f" {idx:02d}. [{item['target_subfolder']}] {item['video_id']} -> {clean_t} ({item['duration']})")
        return
        
    # Import yt-dlp
    try:
        import yt_dlp
    except ImportError:
        print("[ERROR] yt-dlp no está instalado en el entorno de Python.")
        sys.exit(1)
        
    print(f"🚀 Iniciando procesamiento de {len(filtered_catalog)} videos hacia el servidor de red...\n")
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for idx, item in enumerate(filtered_catalog, 1):
        print(f"\n[{idx}/{len(filtered_catalog)}] Procesando:")
        
        dest_folder = DEST_BASE_DIR / item["target_subfolder"].replace("/", os.sep)
        dest_folder.mkdir(parents=True, exist_ok=True)
        
        ok, msg = download_video(item, dest_folder, yt_dlp)
        if ok:
            if "existente" in msg.lower() or "omitido" in msg.lower():
                skip_count += 1
            else:
                success_count += 1
        else:
            error_count += 1
            
    print("\n" + "=" * 85)
    print(" 📊 RESUMEN FINAL DE DESCARGAS EN RED")
    print("=" * 85)
    print(f"  ✅ Descargados con éxito en esta sesión: {success_count}")
    print(f"  ⏭️  Omitidos (ya existentes y verificados): {skip_count}")
    print(f"  ❌ Errores: {error_count}")
    print(f"  📁 Directorio final: {DEST_BASE_DIR}")
    print("=" * 85)

if __name__ == "__main__":
    main()
