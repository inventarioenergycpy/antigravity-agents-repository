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
    origen_dc,
    LENGTH(TRIM(dc)) as len_dc,
    COUNT(*) as cant,
    MIN(dc) as min_dc,
    MAX(dc) as max_dc
FROM georef.vw_suministros
WHERE dc IS NOT NULL AND ROWNUM <= 20000
GROUP BY origen_dc, LENGTH(TRIM(dc))
ORDER BY cant DESC
"""

df = pd.read_sql(query, conn)
print("=== DISTRIBUCION ORIGEN_DC Y LONGITUDES EN MUESTRA DE 20.000 ===")
print(df.to_string())

conn.close()
