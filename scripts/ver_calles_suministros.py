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
    suministro, distrito, calle, altura, barrio, localidad, datos_adicionales_domicilio,
    dc, latitud, longitud
FROM georef.vw_suministros
WHERE distrito = 1 AND dc IS NOT NULL AND ROWNUM <= 10
"""

df = pd.read_sql(query, conn)
for _, r in df.iterrows():
    print(f"Sum: {r['SUMINISTRO']} | Calle: {r['CALLE']} {r['ALTURA']} | Bar: {r['BARRIO']} | DC: {r['DC']}")

conn.close()
