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
cur.execute("SELECT text FROM sys.all_views WHERE owner = 'GEOREF' AND view_name = 'VW_SUMINISTROS'")
row = cur.fetchone()
text = str(row[0])
pos_dc = text.find("DC")
while pos_dc != -1:
    print("--- SNIPPET AROUND DC ---")
    print(text[max(0, pos_dc-200):min(len(text), pos_dc+400)])
    pos_dc = text.find("DC", pos_dc+400)

conn.close()
