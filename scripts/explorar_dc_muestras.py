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
    suministro, distrito, grupo_lectura, ruta_lectura, orden_lectura, 
    latitud, longitud, dc, origen_dc, distrito_catastral, zona_catastral, 
    manzana_catastral, lote_catastral, ph_catastral,
    localidad, barrio, datos_adicionales_domicilio
FROM georef.vw_suministros
WHERE dc IS NOT NULL AND ROWNUM <= 25
"""

df = pd.read_sql(query, conn)
print("=== MUESTRA DE 25 REGISTROS CON DC ===")
for idx, r in df.iterrows():
    print(f"Sum: {r['SUMINISTRO']} | Dist: {r['DISTRITO']} | DC: '{r['DC']}' | OrigDC: {r['ORIGEN_DC']} | Loc: {r['LOCALIDAD']} | Bar: {r['BARRIO']} | DomicilioExtra: {r['DATOS_ADICIONALES_DOMICILIO']}")

conn.close()
