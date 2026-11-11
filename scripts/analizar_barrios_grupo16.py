import os, oracledb, pandas as pd
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

query = """
SELECT 
    localidad,
    barrio,
    COUNT(*) as total_suministros,
    COUNT(DISTINCT SUBSTR(dc, 1, 13)) as total_manzanas,
    MIN(ruta_lectura) as min_ruta,
    MAX(ruta_lectura) as max_ruta
FROM georef.vw_suministros
WHERE distrito = 1 AND grupo_lectura = '16'
GROUP BY localidad, barrio
ORDER BY total_suministros DESC
"""

df = pd.read_sql(query, conn)
print("=== TOP 25 BARRIOS EN DISTRITO 1, GRUPO 16 ===")
print(df.head(25).to_string())

print(f"\nTotal Localidades en Grupo 16: {df['LOCALIDAD'].nunique()}")
print(f"Total Barrios en Grupo 16: {df['BARRIO'].nunique()}")
print(f"Total Manzanas distintas en Grupo 16: {df['TOTAL_MANZANAS'].sum()}")

conn.close()
