import os
import sys
import json
import time
import oracledb
import pandas as pd
from dotenv import load_dotenv

# Cargar .env desde D:\Proyectos\.env o local
load_dotenv(r"D:\Proyectos\.env")

lib_dir = os.environ.get("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")
user = os.environ.get("OR_USER", "jidiaz")
password = os.environ.get("OR_PASS")
host = os.environ.get("OR_HOST", "epec2-scan2.epec.net")
port = int(os.environ.get("OR_PORT", 1521))
service_name = os.environ.get("OR_SERVICE_NAME", "PRODEBS_SEE")

print(f"=== CONECTANDO A ORACLE ({user}@{host}:{port}/{service_name}) ===")

try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except oracledb.ProgrammingError as e:
    if "already" not in str(e).lower():
        print(f"Aviso init_oracle_client: {e}")

dsn = oracledb.makedsn(host=host, port=port, service_name=service_name)
conn = oracledb.connect(user=user, password=password, dsn=dsn)

# Read only transaction
with conn.cursor() as cur:
    cur.execute("SET TRANSACTION READ ONLY")

print("Conexion exitosa en modo Solo Lectura.")

# 1. Resumen por esquema
q1 = """
WITH inventario_unificado AS (
    SELECT owner, table_name AS object_name, 'TABLE' AS object_type, num_rows
    FROM sys.all_tables
    UNION ALL
    SELECT owner, view_name AS object_name, 'VIEW' AS object_type, NULL AS num_rows
    FROM sys.all_views
),
clasificacion AS (
    SELECT 
        owner, object_name, object_type, num_rows,
        CASE 
            WHEN owner IN ('SYS', 'SYSTEM', 'DBSNMP', 'OUTLN', 'XDB', 'WMSYS', 'CTXSYS', 
                           'MDSYS', 'ORDSYS', 'AUDSYS', 'GSMADMIN_INTERNAL', 'OJVMSYS', 
                           'APEX_040000', 'APEX_050000', 'APEX_190000', 'LBACSYS', 'DVSYS') 
                THEN 'SISTEMA_ORACLE'
            WHEN owner LIKE 'APEX%' OR owner LIKE 'FLOWS_%' 
                THEN 'FRAMEWORK_APEX'
            WHEN owner IN ('XXSIGEC', 'SIGEC', 'EPEC', 'COMMERCIAL', 'GIS', 'CATASTRO', 'PROTELEM')
                THEN 'NEGOCIO_CORE_OPERACIONAL'
            ELSE 'APLICATIVO_EXTERNO_O_USUARIO'
        END AS categoria_esquema
    FROM inventario_unificado
)
SELECT 
    categoria_esquema,
    owner,
    COUNT(CASE WHEN object_type = 'TABLE' THEN 1 END) AS total_tablas,
    COUNT(CASE WHEN object_type = 'VIEW' THEN 1 END) AS total_vistas,
    COUNT(1) AS total_objetos_accesibles,
    NVL(SUM(num_rows), 0) AS total_filas_estimadas
FROM clasificacion
GROUP BY categoria_esquema, owner
ORDER BY 
    CASE 
        WHEN categoria_esquema = 'NEGOCIO_CORE_OPERACIONAL' THEN 1
        WHEN categoria_esquema = 'APLICATIVO_EXTERNO_O_USUARIO' THEN 2
        ELSE 3 
    END,
    total_objetos_accesibles DESC
"""
df_esquemas = pd.read_sql(q1, conn)
print("\n--- DISTRIBUCION POR ESQUEMAS ---")
print(df_esquemas.to_string(index=False))

# 2. Tablas y Vistas de Negocio
q2 = """
WITH catalogo_objetos AS (
    SELECT t.owner, t.table_name AS nombre_objeto, 'TABLA' AS tipo_objeto, t.num_rows AS filas_estimadas, 
           t.last_analyzed AS ultima_fecha_analisis, t.partitioned AS es_particionada
    FROM sys.all_tables t
    UNION ALL
    SELECT v.owner, v.view_name AS nombre_objeto, 'VISTA' AS tipo_objeto, NULL AS filas_estimadas, 
           NULL AS ultima_fecha_analisis, 'NO' AS es_particionada
    FROM sys.all_views v
),
conteo_cols AS (
    SELECT owner, table_name AS nombre_objeto, COUNT(1) AS total_columnas
    FROM sys.all_tab_cols
    GROUP BY owner, table_name
),
comentarios AS (
    SELECT owner, table_name AS nombre_objeto, comments AS descripcion_funcional
    FROM sys.all_tab_comments
)
SELECT 
    c.owner AS esquema,
    c.nombre_objeto,
    c.tipo_objeto,
    NVL(col.total_columnas, 0) AS cant_columnas,
    c.filas_estimadas,
    c.es_particionada,
    TO_CHAR(c.ultima_fecha_analisis, 'YYYY-MM-DD HH24:MI:SS') AS fecha_estadisticas,
    com.descripcion_funcional
FROM catalogo_objetos c
LEFT JOIN conteo_cols col ON c.owner = col.owner AND c.nombre_objeto = col.nombre_objeto
LEFT JOIN comentarios com ON c.owner = com.owner AND c.nombre_objeto = com.nombre_objeto
WHERE c.owner NOT IN ('SYS', 'SYSTEM', 'DBSNMP', 'OUTLN', 'XDB', 'WMSYS', 'CTXSYS', 'MDSYS', 'ORDSYS', 'AUDSYS', 'GSMADMIN_INTERNAL', 'OJVMSYS')
ORDER BY c.owner ASC, c.tipo_objeto ASC, c.nombre_objeto ASC
"""
df_negocio = pd.read_sql(q2, conn)
print(f"\nTotal objetos en esquemas de negocio: {len(df_negocio)}")

# 3. Privilegios y Roles
q3 = """
SELECT 
    grantee,
    owner,
    table_name,
    privilege,
    grantable,
    grantor
FROM sys.all_tab_privs_recd
WHERE owner NOT IN ('SYS', 'SYSTEM', 'XDB', 'WMSYS', 'MDSYS')
ORDER BY owner, table_name
"""
df_privs = pd.read_sql(q3, conn)
print(f"Total registros de privilegios recibidos: {len(df_privs)}")

# 4. Roles del usuario
q4 = "SELECT * FROM user_role_privs"
df_roles = pd.read_sql(q4, conn)
print("\n--- ROLES DE USUARIO ASIGNADOS ---")
print(df_roles.to_string(index=False))

# 5. Sinonimos
q5 = """
SELECT 
    owner AS tipo_sinonimo,
    synonym_name,
    table_owner,
    table_name
FROM sys.all_synonyms
WHERE table_owner NOT IN ('SYS', 'SYSTEM', 'XDB', 'WMSYS', 'MDSYS')
  AND (owner = 'PUBLIC' OR owner = USER)
ORDER BY table_owner, synonym_name
"""
df_synonyms = pd.read_sql(q5, conn)
print(f"Total sinonimos accesibles: {len(df_synonyms)}")

# Guardar reportes en CSV y Excel
os.makedirs(r"D:\Proyectos\antigravity-agents-repository\data", exist_ok=True)
downloads_dir = os.path.expanduser(r"~\Downloads")

excel_path_repo = r"D:\Proyectos\antigravity-agents-repository\data\inventario_tablas_vistas_oracle_jidiaz.xlsx"
excel_path_down = os.path.join(downloads_dir, "inventario_tablas_vistas_oracle_jidiaz.xlsx")

with pd.ExcelWriter(excel_path_repo, engine="openpyxl") as writer:
    df_esquemas.to_excel(writer, sheet_name="Resumen_Esquemas", index=False)
    df_negocio.to_excel(writer, sheet_name="Tablas_Vistas_Negocio", index=False)
    df_privs.to_excel(writer, sheet_name="Privilegios_Detalle", index=False)
    df_roles.to_excel(writer, sheet_name="Roles_Usuario", index=False)
    df_synonyms.to_excel(writer, sheet_name="Sinonimos", index=False)

with pd.ExcelWriter(excel_path_down, engine="openpyxl") as writer:
    df_esquemas.to_excel(writer, sheet_name="Resumen_Esquemas", index=False)
    df_negocio.to_excel(writer, sheet_name="Tablas_Vistas_Negocio", index=False)
    df_privs.to_excel(writer, sheet_name="Privilegios_Detalle", index=False)
    df_roles.to_excel(writer, sheet_name="Roles_Usuario", index=False)
    df_synonyms.to_excel(writer, sheet_name="Sinonimos", index=False)

print(f"\nArchivo Excel guardado con exito en:")
print(f"- {excel_path_repo}")
print(f"- {excel_path_down}")

conn.close()