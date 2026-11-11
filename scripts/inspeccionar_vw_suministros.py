import os, oracledb
from dotenv import load_dotenv

load_dotenv(r"D:\Proyectos\.env")
load_dotenv(r"D:\Proyectos\antigravity-agents-repository\.env")

lib_dir = os.environ.get("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception as e:
    pass

dsn = oracledb.makedsn(host=os.environ["OR_HOST"], port=int(os.environ.get("OR_PORT", 1521)), service_name=os.environ["OR_SERVICE_NAME"])
conn = oracledb.connect(user=os.environ["OR_USER"], password=os.environ["OR_PASS"], dsn=dsn)

with conn.cursor() as cur:
    cur.execute("""
        SELECT owner, table_name, column_name, data_type, data_length
        FROM all_tab_cols
        WHERE table_name = 'VW_SUMINISTROS'
        ORDER BY owner, column_id
    """)
    rows = cur.fetchall()
    print("Columns in VW_SUMINISTROS:")
    for r in rows:
        print(f"{r[0]}.{r[1]} -> {r[2]} ({r[3]}:{r[4]})")

conn.close()
