import os, time, oracledb, pandas as pd
from dotenv import load_dotenv

load_dotenv(r"D:\Proyectos\.env")
load_dotenv(r"D:\Proyectos\antigravity-agents-repository\.env")

lib_dir = os.environ.get("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception:
    pass

dsn = oracledb.makedsn(host=os.environ["OR_HOST"], port=int(os.environ.get("OR_PORT", 1521)), service_name=os.environ["OR_SERVICE_NAME"])
conn = oracledb.connect(user=os.environ["OR_USER"], password=os.environ["OR_PASS"], dsn=dsn)

query_manzanas = """
SELECT 
    SUBSTR(dc, 1, 13) as mza_13dig,
    COUNT(*) as cant_suministros,
    ROUND(AVG(latitud), 6) as lat_centroide,
    ROUND(AVG(longitud), 6) as lon_centroide,
    COUNT(CASE WHEN latitud IS NOT NULL THEN 1 END) as con_coords,
    MIN(barrio) as barrio_ejemplo,
    MIN(ruta_lectura) as min_ruta_actual,
    MAX(ruta_lectura) as max_ruta_actual,
    COUNT(DISTINCT ruta_lectura) as rutas_actuales_en_mza
FROM georef.vw_suministros
WHERE distrito = 1 AND grupo_lectura = '16' AND dc IS NOT NULL AND LENGTH(TRIM(dc)) = 16
GROUP BY SUBSTR(dc, 1, 13)
ORDER BY cant_suministros DESC
"""

t0 = time.time()
df_mzas = pd.read_sql(query_manzanas, conn)
t1 = time.time()
conn.close()

print(f"[+] Total Manzanas unicas agrupadas: {len(df_mzas)} en {t1-t0:.2f} s")
print(f"Total suministros en estas manzanas: {df_mzas['CANT_SUMINISTROS'].sum()}")
print("\nDistribucion del tamano de manzanas (suministros por manzana):")
print(df_mzas['CANT_SUMINISTROS'].describe())

print("\nTop 15 Manzanas con mayor cantidad de suministros:")
print(df_mzas.head(15).to_string())

# Guardar temporalmente para modelado
df_mzas.to_parquet("D:\Proyectos\antigravity-agents-repository\scripts\mzas_distrito1_grupo16.parquet", index=False)
print("\n[+] Guardado archivo parquet local para optimizacion algoritmica.")
