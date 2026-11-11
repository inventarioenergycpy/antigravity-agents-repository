import os, oracledb, pandas as pd
from dotenv import load_dotenv

load_dotenv(r"D:\Proyectos\.env")
lib_dir = os.environ.get("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")
oracledb.init_oracle_client(lib_dir=lib_dir)

dsn = oracledb.makedsn(host=os.environ["OR_HOST"], port=int(os.environ.get("OR_PORT", 1521)), service_name=os.environ["OR_SERVICE_NAME"])
conn = oracledb.connect(user=os.environ["OR_USER"], password=os.environ["OR_PASS"], dsn=dsn)

cur = conn.cursor()
cur.execute("SELECT column_name, data_type FROM sys.all_tab_cols WHERE owner = 'XXSIGEC' AND table_name = 'SERVICIOS' AND (column_name LIKE '%LAT%' OR column_name LIKE '%LON%' OR column_name LIKE '%CATA%' OR column_name LIKE '%GEO%')")
print("Columnas de coordenadas/catastro en XXSIGEC.SERVICIOS:")
for r in cur.fetchall():
    print(r)

conn.close()