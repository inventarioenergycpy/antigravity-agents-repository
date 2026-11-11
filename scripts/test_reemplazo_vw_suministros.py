import os, oracledb, pandas as pd
from dotenv import load_dotenv

load_dotenv(r"D:\Proyectos\.env")
lib_dir = os.environ.get("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")
oracledb.init_oracle_client(lib_dir=lib_dir)

dsn = oracledb.makedsn(host=os.environ["OR_HOST"], port=int(os.environ.get("OR_PORT", 1521)), service_name=os.environ["OR_SERVICE_NAME"])
conn = oracledb.connect(user=os.environ["OR_USER"], password=os.environ["OR_PASS"], dsn=dsn)

query_reemplazo = """
SELECT 
    c.srv_codigo,
    b.cnt_numero,
    c.srv_codigo || '/' || LPAD(TO_CHAR(b.cnt_numero), 2, '0') AS suministro_formato,
    a.prs_numero,
    a.prs_razon_social,
    a.prs_cuit,
    c.srv_calle || CASE WHEN c.srv_nro IS NOT NULL THEN ' ' || c.srv_nro ELSE '' END AS domicilio,
    c.srv_distrito_cata AS distrito_catastral,
    c.srv_zona_cata AS zona_catastral,
    c.srv_manzana_cata AS manzana_catastral,
    c.srv_lote_cata AS lote_catastral,
    e.zon_codigo AS zona_comercial,
    c.scf_codigo AS distrito_comercial,
    e.scf_descripcion AS sucursal_descripcion,
    c.grl_codigo AS grupo_lectura,
    c.rtl_codigo AS ruta_lectura,
    c.srv_orden_lectura AS orden_lectura,
    b.tcl_codigo AS codigo_tarifa,
    t.tcl_descripcion AS tarifa,
    eq.ste_numero AS medidor_activo,
    c.srv_gps_latitud AS latitud_gps,
    c.srv_gps_longitud AS longitud_gps
FROM XXSIGEC.servicios c
JOIN XXSIGEC.contratos b ON c.srv_codigo = b.srv_codigo
JOIN XXSIGEC.personas a ON b.prs_numero = a.prs_numero
LEFT JOIN XXSIGEC.sucursales e ON c.scf_codigo = e.scf_codigo
LEFT JOIN XXSIGEC.tarifas t ON b.tcl_codigo = t.tcl_codigo
LEFT JOIN XXSIGEC.equipos eq ON c.srv_codigo = eq.srv_codigo AND eq.eqp_estado IS NULL
WHERE b.cnt_estado = 'V'
  AND ROWNUM <= 5
"""

df_test = pd.read_sql(query_reemplazo, conn)
print("=== EJECUCION EXITOSA DEL REEMPLAZO 100% OPERATIVO ===")
print(df_test.to_string())

conn.close()