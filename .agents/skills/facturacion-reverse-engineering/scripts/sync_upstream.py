#!/usr/bin/env python3
"""
sync_upstream.py
================
Script de sincronización y control de versión para el Agente 12 (Facturación Reverse Engineering).
Verifica que el repositorio local esté 100% alineado con el upstream remoto oficial:
    https://github.com/PROTELEM-EPEC/facturacion-reverse-engineering.git (branch: main)

Uso:
    python sync_upstream.py [--pull] [--quiet]
"""

import sys
import os
import subprocess
import argparse

UPSTREAM_URL = "https://github.com/PROTELEM-EPEC/facturacion-reverse-engineering.git"
DEFAULT_BRANCH = "main"

# Candidatos para localizar el repositorio local
CANDIDATE_PATHS = [
    r"D:\Proyectos\facturacion-reverse-engineering",
    os.path.expandvars(r"%USERPROFILE%\.gemini\antigravity-ide\scratch\facturacion-reverse-engineering"),
    r"C:\Proyectos\facturacion-reverse-engineering",
]

def find_repo_path():
    for path in CANDIDATE_PATHS:
        git_dir = os.path.join(path, ".git")
        if os.path.exists(git_dir):
            return os.path.abspath(path)
    return None

def run_git(cmd, cwd):
    result = subprocess.run(
        ["git"] + cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def check_and_sync(auto_pull=False, quiet=False):
    repo_path = find_repo_path()
    if not repo_path:
        print("[ERROR] No se encontró el repositorio local 'facturacion-reverse-engineering'.")
        print(f"Candidatos evaluados: {CANDIDATE_PATHS}")
        return False, "Repositorio no encontrado localmente."

    if not quiet:
        print(f"[*] Repositorio detectado en: {repo_path}")
        print(f"[*] Verificando sincronización contra upstream remoto: {UPSTREAM_URL} ({DEFAULT_BRANCH})...")

    # 1. Fetch upstream
    ret, out, err = run_git(["fetch", "origin", DEFAULT_BRANCH], cwd=repo_path)
    if ret != 0:
        msg = f"Error en git fetch: {err}"
        if not quiet:
            print(f"[!] {msg}")
        return False, msg

    # 2. Obtener hashes
    _, local_head, _ = run_git(["rev-parse", "HEAD"], cwd=repo_path)
    _, remote_head, _ = run_git(["rev-parse", f"origin/{DEFAULT_BRANCH}"], cwd=repo_path)

    # 3. Comprobar diferencias
    _, diff_commits, _ = run_git(["log", f"HEAD..origin/{DEFAULT_BRANCH}", "--oneline"], cwd=repo_path)
    _, uncommitted, _ = run_git(["status", "--porcelain"], cwd=repo_path)

    status_info = {
        "repo_path": repo_path,
        "local_head": local_head,
        "remote_head": remote_head,
        "is_synced": (local_head == remote_head),
        "pending_commits": diff_commits.splitlines() if diff_commits else [],
        "has_uncommitted": bool(uncommitted)
    }

    if status_info["is_synced"]:
        if not quiet:
            print(f"[OK] El Agente 12 está 100% SINCRONIZADO con el último commit upstream ({local_head[:10]}).")
        return True, status_info

    # Si hay commits pendientes
    if not quiet:
        print(f"[ALERTA] Se detectaron {len(status_info['pending_commits'])} commits pendientes en upstream:")
        for c in status_info["pending_commits"]:
            print(f"   -> {c}")

    if auto_pull:
        if not quiet:
            print("[*] Ejecutando sincronización automática (git pull origin main)...")
        p_ret, p_out, p_err = run_git(["pull", "--ff-only", "origin", DEFAULT_BRANCH], cwd=repo_path)
        if p_ret == 0:
            if not quiet:
                print(f"[OK] Sincronización exitosa. Ahora en commit: {remote_head[:10]}.")
            status_info["is_synced"] = True
            return True, status_info
        else:
            if not quiet:
                print(f"[ERROR] No se pudo hacer fast-forward pull: {p_err}. Revise cambios locales.")
            return False, status_info

    return False, status_info

def main():
    parser = argparse.ArgumentParser(description="Control de Sincronización para Agente 12 (Facturación Reverse Engineering)")
    parser.add_argument("--pull", action="store_true", help="Aplica git pull si hay actualizaciones remotas")
    parser.add_argument("--quiet", action="store_true", help="Modo silencioso, sólo retorna código de salida")
    args = parser.parse_args()

    success, info = check_and_sync(auto_pull=args.pull, quiet=args.quiet)
    if not success and not (isinstance(info, dict) and not info.get("is_synced") and not args.pull):
        sys.exit(1)
    if isinstance(info, dict) and not info.get("is_synced"):
        sys.exit(2) # Código 2: desincronizado
    sys.exit(0)

if __name__ == "__main__":
    main()
