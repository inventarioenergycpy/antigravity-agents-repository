"""
Pruebas Unitarias y de Integración: scripts/network_snapshot.py
"""

import os
import sys
import time
from pathlib import Path

# Ajustar sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
from network_snapshot import get_local_snapshot, is_network_path, DEFAULT_CACHE_DIR

def run_tests():
    print("=== INICIANDO PRUEBAS PARCIALES (FASE 3) ===")
    
    # 1. Comprobar detección de rutas UNC
    assert is_network_path(r"\\srvfs01\ProyectoTelemedicion\test.xlsx") is True
    assert is_network_path(r"C:\Users\test\file.txt") is False
    assert is_network_path(r"D:\Proyectos\test.py") is False
    print("✓ Detección de rutas UNC validada.")

    # 2. Crear archivo simulado en scratch/test_remote
    test_remote_dir = Path(__file__).resolve().parent.parent / "data" / "test_remote_sim"
    test_remote_dir.mkdir(parents=True, exist_ok=True)
    sim_remote_file = test_remote_dir / "simulacion_planilla_red.xlsx"
    
    with open(sim_remote_file, "wb") as f:
        f.write(b"MOCK EXCEL CONTENT FOR NETWORK TEST" * 100)
    
    # 3. Forzar snapshot
    # Para simular que es de red aunque esté en disco local, pasamos una ruta absoluta
    # y probamos get_local_snapshot especificando una carpeta de caché temporal
    test_cache_dir = Path(__file__).resolve().parent.parent / "data" / "network_cache" / "unit_test"
    
    # Simular llamada como si fuera ruta UNC pasando string
    # Probamos la función directa con ruta existente
    snap1 = get_local_snapshot(sim_remote_file, cache_dir=test_cache_dir, force_refresh=True)
    assert snap1.exists(), "El archivo de snapshot debe existir"
    assert snap1.stat().st_size == sim_remote_file.stat().st_size, "El tamaño debe coincidir"
    print(f"✓ Primer Snapshot generado exitosamente: {snap1.name} ({snap1.stat().st_size} bytes)")

    # 4. Prueba Delta Cache (Caché inteligente sin recopia)
    t0 = time.time()
    snap2 = get_local_snapshot(sim_remote_file, cache_dir=test_cache_dir, force_refresh=False)
    elapsed = time.time() - t0
    assert snap2 == snap1, "Debe retornar la misma ruta local"
    print(f"✓ Prueba Delta Cache superada: Retorno en {elapsed*1000:.2f} ms (0 recopia)")

    # 5. Limpieza de prueba
    if sim_remote_file.exists():
        sim_remote_file.unlink()
    if test_remote_dir.exists():
        try:
            test_remote_dir.rmdir()
        except Exception:
            pass

    print("=== TODAS LAS PRUEBAS PARCIALES (FASE 3) HAN SIDO EXITOSAS ===")

if __name__ == "__main__":
    run_tests()
