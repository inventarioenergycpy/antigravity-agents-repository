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

query = """
SELECT 
    suministro,
    distrito,
    grupo_lectura,
    ruta_lectura,
    orden_lectura,
    latitud,
    longitud,
    dc,
    localidad,
    barrio,
    datos_adicionales_domicilio
FROM georef.vw_suministros
WHERE dc IS NOT NULL
  AND ROWNUM <= 2000
"""

t0 = time.time()
with conn.cursor() as cur:
    cur.execute("SET TRANSACTION READ ONLY")
df = pd.read_sql(query, conn)
t1 = time.time()
print(f"Leidos {len(df)} registros en {t1-t0:.2f} s")
print("Longitudes de DC en la muestra:")
print(df['DC'].str.strip().str.len().value_counts())
print("\nLocalidades encontradas (top 15):")
print(df['LOCALIDAD'].value_counts().head(15))

conn.close()
