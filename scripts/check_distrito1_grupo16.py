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

query_check_grupo = """
SELECT 
    distrito,
    grupo_lectura,
    COUNT(*) as total_suministros,
    COUNT(dc) as con_dc,
    COUNT(DISTINCT ruta_lectura) as rutas_actuales,
    MIN(ruta_lectura) as ruta_min,
    MAX(ruta_lectura) as ruta_max
FROM georef.vw_suministros
WHERE distrito = 1 AND (grupo_lectura = '16' OR grupo_lectura = '016' OR grupo_lectura LIKE '%16%')
GROUP BY distrito, grupo_lectura
"""

with conn.cursor() as cur:
    cur.execute(query_check_grupo)
    cols = [d[0] for d in cur.description]
    for r in cur.fetchall():
        print(dict(zip(cols, r)))

conn.close()
