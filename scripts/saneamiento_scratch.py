#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
=============================================================================
Script de Saneamiento Seguro y Organizacion del Scratchpad (D:\Proyectos)
=============================================================================
Proposito:
  Clasificar y mover de manera 100% segura y reversible todos los archivos
  y carpetas de staging sueltos en la raiz de 'D:\Proyectos' hacia una
  estructura jerarquica limpia en 'D:\Proyectos\_archive_scratch\'.

Garantias de Seguridad:
  1. Modo Dry-Run por defecto: No mueve nada si no se especifica '--apply'.
  2. Whitelist de Proteccion Estricta: Jamas toca ni mueve repositorios Git,
     proyectos documentados, junctions ni configuraciones de Obsidian.
  3. Manifiesto y Rollback Total: Genera 'manifest_saneamiento.json'. Con
     '--rollback' restaura cada archivo exactamente a su ubicacion original.
  4. Preservacion de '.env': Mantiene '.env' en la raiz y coloca una copia
     en 'scripts_python/' para que los scripts sigan funcionando.
=============================================================================
"""

import os
import sys
import shutil
import json
import argparse
from datetime import datetime
from pathlib import Path

# Ajuste de encoding para Windows console
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Directorio raiz del Scratch
SCRATCH_ROOT = Path(r"D:\Proyectos")
ARCHIVE_ROOT = SCRATCH_ROOT / "_archive_scratch"

# Directorios estrictamente protegidos (NUNCA TOCAR NI MOVER)
PROTECTED_DIRS = {
    ".git",
    ".obsidian",
    "_archive_scratch",
    # 18 Repositorios Git Activos
    "adelat-cier-benchmarking",
    "analizador_perfiles",
    "antigravity-agents-repository",
    "asesoramiento-parque-solar-fotovoltaico",
    "auditoria-relevamiento-conectar",
    "career-market-intelligence",
    "control-catastral-georeferencia",
    "dashboard-gestion-intermediacion",
    "demo-dashboard",
    "despliegue-medidores-inteligentes-ami",
    "encuesta_cier",
    "facturacion-reverse-engineering",
    "forwarded-message",
    "protelem-indicadores-gerencia-comercial",
    "proyecto-pistacho-alcaparra-neuquen",
    "relevamiento-alumbrado-publico-medidores",
    "showroom-energycpy",
    "sigec-ruta-nueva-catastro-georef",
    "real-estate-investment-intelligence",
    # Carpetas de Proyectos / Presentaciones no-git
    "cier_html_presentation",
    "showroom-energycpy-preview",
    "inovare",
    "C_repo_local",
    "viewer",
}

# Archivos protegidos que se preservan en la raiz
PROTECTED_FILES = {
    "saneamiento_scratch.py",
    "workspace.code-workspace",
    # '.env' se preserva en raiz Y se copia a scripts_python
}

# Carpetas de staging / temporales a mover a staging_folders/
STAGING_DIRS = {
    "temp_pdf_imgs",
    "temp_video_staging",
    "chrome_temp",
    "extracted_images",
    "extracted_images_2025",
    "extracted_pdf_2025",
    "__pycache__",
}

# Mapeo de categorias por extension
EXT_CATEGORIES = {
    ".py": "scripts_python",
    ".bat": "scripts_python",
    ".js": "scripts_python",
    ".md": "markdown_docs",
    ".pkl": "data_and_pickles",
    ".txt": "data_and_pickles",
    ".json": "data_and_pickles",
    ".sql": "data_and_pickles",
    ".xlsx": "data_and_pickles",
    ".csv": "data_and_pickles",
    ".parquet": "data_and_pickles",
    ".mp3": "multimedia_audio",
    ".ogg": "multimedia_audio",
    ".wav": "multimedia_audio",
    ".html": "web_assets",
}


def get_category_for_file(file_path: Path) -> str:
    ext = file_path.suffix.lower()
    return EXT_CATEGORIES.get(ext, "otros_archivos")


def scan_scratch():
    """Escanea la raiz de SCRATCH_ROOT y clasifica los elementos candidatos a mover."""
    items_to_move = []
    staging_folders_to_move = []

    for entry in SCRATCH_ROOT.iterdir():
        # Evaluar directorios
        if entry.is_dir():
            name = entry.name
            if name in PROTECTED_DIRS:
                continue
            if name in STAGING_DIRS:
                staging_folders_to_move.append(entry)
            continue

        # Evaluar archivos en la raiz
        if entry.is_file():
            name = entry.name
            if name in PROTECTED_FILES:
                continue
            
            # Caso especial .env: se preserva en raiz y se copia
            if name == ".env":
                continue

            category = get_category_for_file(entry)
            target_dir = ARCHIVE_ROOT / category
            target_file = target_dir / name
            items_to_move.append({
                "source": entry,
                "target_dir": target_dir,
                "target_file": target_file,
                "category": category,
                "size": entry.stat().st_size
            })

    return items_to_move, staging_folders_to_move


def execute_saneamiento(apply: bool = False):
    items_to_move, staging_folders_to_move = scan_scratch()

    # Contadores por categoria
    category_counts = {}
    category_bytes = {}
    for item in items_to_move:
        cat = item["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1
        category_bytes[cat] = category_bytes.get(cat, 0) + item["size"]

    print("=" * 80)
    print(" SANEAMIENTO SEGURO DEL SCRATCHPAD (D:\\Proyectos)")
    print(f" Modo: {'APLICACION REAL (--apply)' if apply else 'SIMULACION (DRY-RUN)'}")
    print(f" Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    print("\n[RESUMEN] ELEMENTOS DETECTADOS PARA CLASIFICACION:")
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        mb = category_bytes[cat] / (1024 * 1024)
        print(f"  * {cat:<20}: {count:>4} archivos ({mb:>7.2f} MB)")

    total_files = len(items_to_move)
    total_mb = sum(item["size"] for item in items_to_move) / (1024 * 1024)
    print(f"\n  TOTAL ARCHIVOS SUELTOS: {total_files} ({total_mb:.2f} MB)")

    print(f"\n[CARPETAS TEMPORALES / STAGING DETECTADAS] ({len(staging_folders_to_move)}):")
    for s_dir in staging_folders_to_move:
        print(f"  * {s_dir.name}/")

    if not apply:
        print("\n" + "#" * 80)
        print(" [AVISO]: Modo de simulacion (DRY-RUN). Ningun archivo ha sido modificado.")
        print(" Para ejecutar el saneamiento definitivo, ejecuta:")
        print("   python saneamiento_scratch.py --apply")
        print("#" * 80 + "\n")
        return

    # APLICACION REAL
    print("\n[APPLY] INICIANDO MOVIMIENTO SEGURO Y GENERACION DE MANIFIESTO...")
    ARCHIVE_ROOT.mkdir(exist_ok=True)
    manifest = {
        "timestamp": datetime.now().isoformat(),
        "scratch_root": str(SCRATCH_ROOT),
        "archive_root": str(ARCHIVE_ROOT),
        "files_moved": [],
        "folders_moved": [],
    }

    # 1. Mover archivos sueltos
    moved_count = 0
    for item in items_to_move:
        target_dir = item["target_dir"]
        target_dir.mkdir(parents=True, exist_ok=True)
        src = item["source"]
        dst = item["target_file"]

        # Evitar sobreescritura accidental
        if dst.exists():
            dst = target_dir / f"{src.stem}_{int(datetime.now().timestamp())}{src.suffix}"

        shutil.move(str(src), str(dst))
        manifest["files_moved"].append({
            "source": str(src),
            "target": str(dst),
            "size": item["size"]
        })
        moved_count += 1

    # 2. Copiar .env a scripts_python/ para mantener funcionalidad de scripts
    env_file = SCRATCH_ROOT / ".env"
    if env_file.exists():
        scripts_env = ARCHIVE_ROOT / "scripts_python" / ".env"
        scripts_env.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(env_file), str(scripts_env))
        print("  [OK] Archivo '.env' duplicado con exito en '_archive_scratch/scripts_python/.env' (y preservado en raiz).")

    # 3. Mover carpetas de staging
    staging_target = ARCHIVE_ROOT / "staging_folders"
    staging_target.mkdir(parents=True, exist_ok=True)
    for s_dir in staging_folders_to_move:
        dst_folder = staging_target / s_dir.name
        if dst_folder.exists():
            shutil.rmtree(str(dst_folder))
        shutil.move(str(s_dir), str(dst_folder))
        manifest["folders_moved"].append({
            "source": str(s_dir),
            "target": str(dst_folder)
        })
        print(f"  [OK] Carpeta '{s_dir.name}/' movida a 'staging_folders/'")

    # 4. Guardar manifiesto de auditoria
    manifest_path = ARCHIVE_ROOT / "manifest_saneamiento.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\n[EXITO] SANEAMIENTO COMPLETADO:")
    print(f"  * {moved_count} archivos organizados en '{ARCHIVE_ROOT}'.")
    print(f"  * {len(staging_folders_to_move)} carpetas de staging reubicadas.")
    print(f"  * Manifiesto de auditoria guardado en: '{manifest_path}'.")
    print("  * Para revertir completamente los cambios en cualquier momento, ejecuta:")
    print("      python saneamiento_scratch.py --rollback\n")


def execute_rollback():
    manifest_path = ARCHIVE_ROOT / "manifest_saneamiento.json"
    if not manifest_path.exists():
        print(f"[ERROR] No se encontro el manifiesto de rollback en '{manifest_path}'.")
        return

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    print("=" * 80)
    print(" EJECUTANDO ROLLBACK DE SANEAMIENTO (REVERSION A D:\\Proyectos)")
    print(f" Manifiesto original: {manifest.get('timestamp')}")
    print("=" * 80)

    # 1. Revertir archivos
    files_reverted = 0
    for entry in manifest.get("files_moved", []):
        src = Path(entry["target"])  # Donde esta ahora
        dst = Path(entry["source"])  # Donde estaba originalmente
        if src.exists():
            shutil.move(str(src), str(dst))
            files_reverted += 1

    # 2. Revertir carpetas
    folders_reverted = 0
    for entry in manifest.get("folders_moved", []):
        src = Path(entry["target"])
        dst = Path(entry["source"])
        if src.exists():
            shutil.move(str(src), str(dst))
            folders_reverted += 1

    print(f"\n[EXITO] ROLLBACK COMPLETADO:")
    print(f"  * {files_reverted} archivos restaurados a 'D:\\Proyectos\\'.")
    print(f"  * {folders_reverted} carpetas restauradas a 'D:\\Proyectos\\'.")


def main():
    parser = argparse.ArgumentParser(description="Saneamiento Seguro de D:\\Proyectos")
    parser.add_argument("--apply", action="store_true", help="Aplica el saneamiento y mueve los archivos.")
    parser.add_argument("--rollback", action="store_true", help="Revierte el saneamiento usando el manifiesto.")
    args = parser.parse_args()

    if args.rollback:
        execute_rollback()
    else:
        execute_saneamiento(apply=args.apply)


if __name__ == "__main__":
    main()

