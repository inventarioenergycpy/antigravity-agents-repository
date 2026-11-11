import os, oracledb
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

cur = conn.cursor()
for tbl in ['DC_PCIA', 'DC_MUNI']:
    print(f"=== COLUMNAS DE GEOREF.{tbl} ===")
    cur.execute(f"SELECT column_name, data_type, data_length FROM all_tab_cols WHERE owner = 'GEOREF' AND table_name = '{tbl}' ORDER BY column_id")
    for r in cur.fetchall():
        print(f"  {r[0]} ({r[1]}:{r[2]})")

conn.close()
