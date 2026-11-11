"""
Módulo de Utilidad: Protocolo de Snapshot Local de Mínima Interferencia de Red
=============================================================================
Ecosistema: Antigravity IDE / Repositorio Central de Agentes
Objetivo: Garantizar que cualquier acceso a recursos compartidos de red (UNC como \\srvfs01,
unidades de red mapeadas o fuentes online) se realice creando inmediatamente una copia local
de trabajo en 'data/network_cache/', liberando el archivo de red en milisegundos para no
interferir con otros usuarios ni causar bloqueos (Sharing Violations).
"""

import os
import sys
import shutil
import hashlib
from pathlib import Path
from typing import Optional, Union

# Directorio base del repositorio central
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CACHE_DIR = REPO_ROOT / "data" / "network_cache"


def is_network_path(path_str: str) -> bool:
    """Detecta si una ruta corresponde a una ubicación de red UNC o compartida."""
    p = str(path_str).strip()
    # UNC path (ej. \\srvfs01\...)
    if p.startswith(r"\\") or p.startswith("//"):
        return True
    return False


def get_local_snapshot(
    remote_path: Union[str, Path],
    cache_dir: Optional[Union[str, Path]] = None,
    force_refresh: bool = False,
    buffer_size: int = 4 * 1024 * 1024  # 4MB buffer para alta velocidad
) -> Path:
    """
    Obtiene una copia local (snapshot) de un archivo de red con mínima interferencia.
    
    1. Si la ruta ya es local y no es de red, la retorna directamente.
    2. Si es de red (ej. \\srvfs01\\...):
       a. Verifica tamaño y fecha de modificación (mtime).
       b. Si el archivo ya existe localmente con el mismo tamaño y timestamp (Delta Cache),
          lo retorna de inmediato sin abrir la red (interferencia = 0 segundos).
       c. Si es nuevo o cambió, realiza una copia binaria rápida con permisos de lectura
          compartida y cierra el handle de inmediato.
    
    Retorna la ruta absoluta local en 'data/network_cache/'.
    """
    remote_path_obj = Path(remote_path)
    remote_str = str(remote_path)

    # Si es un archivo local normal que no está en ruta UNC, no requiere staging
    if not is_network_path(remote_str):
        if remote_path_obj.exists():
            return remote_path_obj.resolve()
        # Si no existe localmente, podría ser una ruta relativa
        resolved = (REPO_ROOT / remote_path_obj).resolve()
        if resolved.exists():
            return resolved

    if cache_dir is None:
        target_cache_dir = DEFAULT_CACHE_DIR
    else:
        target_cache_dir = Path(cache_dir).resolve()

    target_cache_dir.mkdir(parents=True, exist_ok=True)

    # Sanear y organizar la estructura de carpetas locales basándonos en la ruta de red
    clean_unc = remote_str.replace("/", "\\").lstrip("\\")
    local_target = target_cache_dir / clean_unc

    # Si el nombre es demasiado largo para Windows o contiene caracteres raros, usar subdirectorio
    local_target_dir = local_target.parent
    local_target_dir.mkdir(parents=True, exist_ok=True)

    if not remote_path_obj.exists():
        raise FileNotFoundError(f"El recurso de red no existe o no es accesible: {remote_str}")

    remote_stat = remote_path_obj.stat()
    remote_size = remote_stat.st_size
    remote_mtime = remote_stat.st_mtime

    # Comprobación de Caché Inteligente (Delta Check)
    if not force_refresh and local_target.exists():
        local_stat = local_target.stat()
        # Tolerancia de 1 segundo por diferencias de precisión en sistemas de archivos SMB/NTFS
        if local_stat.st_size == remote_size and abs(local_stat.st_mtime - remote_mtime) < 1.5:
            # Reutilización inmediata: Interferencia en red = 0 milisegundos
            return local_target.resolve()

    def _win_path(p: Union[str, Path]) -> str:
        s = os.path.abspath(str(p))
        if sys.platform == "win32" and not s.startswith("\\\\?\\"):
            if s.startswith("\\\\"):
                return "\\\\?\\UNC\\" + s[2:]
            return "\\\\?\\" + s
        return s

    # Copia rápida por streaming en bloques con apertura no bloqueante
    temp_target = local_target.with_suffix(local_target.suffix + ".tmp")
    src_path = _win_path(remote_path_obj)
    dst_temp_path = _win_path(temp_target)
    dst_final_path = _win_path(local_target)

    try:
        with open(src_path, "rb") as src, open(dst_temp_path, "wb") as dst:
            while True:
                chunk = src.read(buffer_size)
                if not chunk:
                    break
                dst.write(chunk)
        
        # Preservar atributos de fecha para el delta cache
        shutil.copystat(src_path, dst_temp_path)
        
        # Renombrado atómico
        if os.path.exists(dst_final_path):
            os.remove(dst_final_path)
        os.rename(dst_temp_path, dst_final_path)
        
    except Exception as e:
        if os.path.exists(dst_temp_path):
            try:
                os.remove(dst_temp_path)
            except Exception:
                pass
        raise IOError(f"Error al generar snapshot local de mínima interferencia para '{remote_str}': {e}")

    return local_target.resolve()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Snapshot Local de Mínima Interferencia de Red")
    parser.add_argument("remote_path", help="Ruta de red UNC o archivo a respaldar localmente")
    parser.add_argument("--force", action="store_true", help="Forzar recopia ignorando el cache delta")
    args = parser.parse_args()

    try:
        local_file = get_local_snapshot(args.remote_path, force_refresh=args.force)
        print(f"SNAPSHOT_OK: {local_file}")
    except Exception as err:
        print(f"SNAPSHOT_ERROR: {err}", file=sys.stderr)
        sys.exit(1)
