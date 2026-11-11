import os, oracledb, pandas as pd
from dotenv import load_dotenv

load_dotenv(r"D:\Proyectos\.env")
lib_dir = os.environ.get("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")
oracledb.init_oracle_client(lib_dir=lib_dir)

dsn = oracledb.makedsn(host=os.environ["OR_HOST"], port=int(os.environ.get("OR_PORT", 1521)), service_name=os.environ["OR_SERVICE_NAME"])
conn = oracledb.connect(user=os.environ["OR_USER"], password=os.environ["OR_PASS"], dsn=dsn)

cur = conn.cursor()
cur.execute("SELECT text FROM sys.all_views WHERE owner = 'GEOREF' AND view_name = 'VW_SUMINISTROS_GEO'")
row = cur.fetchone()
if row:
    print("=== TEXTO SQL DE LA VISTA GEOREF.VW_SUMINISTROS_GEO ===")
    print(str(row[0]))

conn.close()