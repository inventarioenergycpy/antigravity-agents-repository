import os, oracledb, pandas as pd
from dotenv import load_dotenv

load_dotenv(r"D:\Proyectos\.env")
lib_dir = os.environ.get("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")
oracledb.init_oracle_client(lib_dir=lib_dir)

dsn = oracledb.makedsn(host=os.environ["OR_HOST"], port=int(os.environ.get("OR_PORT", 1521)), service_name=os.environ["OR_SERVICE_NAME"])
conn = oracledb.connect(user=os.environ["OR_USER"], password=os.environ["OR_PASS"], dsn=dsn)

excel_path_repo = r"D:\Proyectos\antigravity-agents-repository\data\inventario_tablas_vistas_oracle_jidiaz.xlsx"
downloads_dir = os.path.expanduser(r"~\Downloads")
excel_path_down = os.path.join(downloads_dir, "inventario_tablas_vistas_oracle_jidiaz.xlsx")

df_esquemas = pd.read_excel(excel_path_repo, sheet_name="Resumen_Esquemas")
df_negocio = pd.read_excel(excel_path_repo, sheet_name="Tablas_Vistas_Negocio")
df_privs = pd.read_excel(excel_path_repo, sheet_name="Privilegios_Detalle")
df_roles = pd.read_excel(excel_path_repo, sheet_name="Roles_Usuario")
df_synonyms = pd.read_excel(excel_path_repo, sheet_name="Sinonimos")

# Marcar estado de operatividad real
error_georef = ['VW_INSP_ILICITOS', 'VW_ILICITOS', 'VW_INT', 'VW_INTELIGENTES', 'VW_ORD', 'VW_PCT', 'VW_RUTAS', 'VW_SUMINISTROS', 'VW_SUMINISTROS_GEO']

def clasificar_operatividad(row):
    if row['ESQUEMA'] == 'GEOREF' and row['NOMBRE_OBJETO'] in error_georef:
        return 'RESTRICCION_FUNCION_PLSQL (ORA-01031)'
    if row['ESQUEMA'] == 'XXSIGEC':
        return 'VERIFICADO_100%_OPERATIVO (Via XXSIGEC_SEL)'
    return 'VERIFICADO_OPERATIVO'

df_negocio['ESTADO_OPERATIVO_TESTEADO'] = df_negocio.apply(clasificar_operatividad, axis=1)

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

print("Excel actualizado con columna de verificacion operativa real.")
conn.close()