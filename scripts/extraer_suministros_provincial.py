# -*- coding: utf-8 -*-
import os, sys, time, oracledb
import pandas as pd
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
load_dotenv(r"D:\Proyectos\.env")

lib_dir = os.environ.get("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")
try:
    if os.path.exists(lib_dir):
        oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception:
    pass

user = os.environ.get("OR_USER", "jidiaz")
password = os.environ.get("OR_PASS")
host = os.environ.get("OR_HOST", "epec2-scan2.epec.net")
port = int(os.environ.get("OR_PORT", 1521))
service_name = os.environ.get("OR_SERVICE_NAME", "PRODEBS_SEE")

out_parquet = r"D:\Proyectos\antigravity-agents-repository\data\suministros_provincial_completo.parquet"

def extraer_suministros():
    print("=" * 80)
    print(">>> EXTRACCION MASIVA DE SUMINISTROS PROVINCIALES EPEC (georef.vw_suministros)")
    print("=" * 80)
    
    t0 = time.time()
    dsn = oracledb.makedsn(host=host, port=port, service_name=service_name)
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
    
    query = """
    SELECT 
        suministro, cliente, contrato,
        distrito, distrito_descripcion, grupo_lectura, ruta_lectura, orden_lectura,
        dc, origen_dc,
        zona_catastral, distrito_catastral, manzana_catastral, lote_catastral, ph_catastral,
        calle, altura, barrio, localidad,
        latitud, longitud,
        estado_contrato, tarifa
    FROM georef.vw_suministros
    """
    
    print("Ejecutando consulta en Oracle...")
    cursor = conn.cursor()
    cursor.arraysize = 50000
    cursor.execute(query)
    
    cols = [col[0].lower() for col in cursor.description]
    
    print("Descargando registros por batches de 50.000...")
    chunks = []
    total_filas = 0
    while True:
        rows = cursor.fetchmany(50000)
        if not rows:
            break
        df_chunk = pd.DataFrame(rows, columns=cols)
        chunks.append(df_chunk)
        total_filas += len(df_chunk)
        print(f"  Descargadas {total_filas:,} filas ({time.time()-t0:.1f}s)...", flush=True)
        
    cursor.close()
    conn.close()
    
    print("\nConsolidando DataFrame...", flush=True)
    df_all = pd.concat(chunks, ignore_index=True)
    print(f"Total registros descargados: {len(df_all):,}", flush=True)
    
    print(f"Guardando en cache Parquet: {out_parquet}...", flush=True)
    df_all.to_parquet(out_parquet, index=False, engine='pyarrow', compression='snappy')
    size_mb = os.path.getsize(out_parquet) / (1024 * 1024)
    print(f"Guardado exitoso: {size_mb:.2f} MB en {time.time()-t0:.2f} segundos.", flush=True)

if __name__ == "__main__":
    extraer_suministros()
