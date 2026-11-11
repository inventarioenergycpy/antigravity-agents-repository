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
cur.execute("""
    SELECT NOMENCLATURA, DESIG_OFICIAL, DEPARTAMENTO, PEDANIA, PUEBLO, DISTRITO, ZONA, MANZANA, PARCELA, TIPO
    FROM GEOREF.DC_PCIA
    WHERE DEPARTAMENTO = 23 AND PEDANIA = 4 AND PUEBLO = 55 AND ROWNUM <= 5
""")
cols = [d[0] for d in cur.description]
for r in cur.fetchall():
    print(dict(zip(cols, r)))

conn.close()
