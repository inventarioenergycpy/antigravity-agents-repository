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

query_stats = """
SELECT 
    COUNT(*) as total_suministros,
    COUNT(dc) as total_dc_not_null,
    COUNT(DISTINCT dc) as dc_unicos,
    ROUND(COUNT(dc) * 100.0 / COUNT(*), 2) as pct_con_dc
FROM georef.vw_suministros
"""

query_lengths = """
SELECT 
    LENGTH(TRIM(dc)) as longitud_dc,
    COUNT(*) as cantidad,
    MIN(TRIM(dc)) as ejemplo_min,
    MAX(TRIM(dc)) as ejemplo_max
FROM georef.vw_suministros
WHERE dc IS NOT NULL
GROUP BY LENGTH(TRIM(dc))
ORDER BY cantidad DESC
"""

with conn.cursor() as cur:
    print("=== ESTADISTICAS GENERALES DE DC ===")
    cur.execute(query_stats)
    cols = [d[0] for d in cur.description]
    for row in cur.fetchall():
        print(dict(zip(cols, row)))

    print("\n=== DISTRIBUCION POR LONGITUD DE DC ===")
    cur.execute(query_lengths)
    cols = [d[0] for d in cur.description]
    for row in cur.fetchall():
        print(dict(zip(cols, row)))

conn.close()
