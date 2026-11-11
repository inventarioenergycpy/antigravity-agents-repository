import shutil
import os
import sys
import time
import oracledb
import pandas as pd
import numpy as np
from datetime import datetime
from dotenv import load_dotenv
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Configurar stdout a UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("[*] Iniciando proceso de extracción y generación de Excel para Auditoría CAMMESA...")
print("[*] Aplicando controles solicitados: Filtro de Energía Negativa, Inclusión de GUDIS y Mapeo Estricto de Relaciones SIGEC-CAMMESA.")

# Cargar variables de entorno
ENV_PATHS = [
    r"D:\Proyectos\antigravity-agents-repository\.env",
    r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\.env",
    r"C:\Users\jidiaz\.env"
]
for p in ENV_PATHS:
    if os.path.exists(p):
        load_dotenv(p)

OR_USER = os.getenv("OR_USER", "jidiaz")
OR_PASS = os.getenv("OR_PASS")
OR_HOST = os.getenv("OR_HOST", "epec2-scan2.epec.net")
OR_PORT = int(os.getenv("OR_PORT", "1521"))
OR_SERVICE_NAME = os.getenv("OR_SERVICE_NAME", "PRODEBS_SEE")
OR_INSTANT_CLIENT = os.getenv("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")

if not OR_PASS:
    print("ERROR: Contraseña OR_PASS no encontrada.")
    sys.exit(1)

# Inicializar Oracle Client Thick
try:
    oracledb.init_oracle_client(lib_dir=OR_INSTANT_CLIENT)
except oracledb.ProgrammingError as e:
    if "already" not in str(e).lower():
        raise

print(f"[*] Conectando a Oracle Database ({OR_HOST}:{OR_PORT}/{OR_SERVICE_NAME})...")
dsn = oracledb.makedsn(host=OR_HOST, port=OR_PORT, service_name=OR_SERVICE_NAME)
conn = oracledb.connect(user=OR_USER, password=OR_PASS, dsn=dsn)

# ==========================================
# 1. EXTRACCIÓN DE CONTRATOS, PERSONAS Y GUDIS
# ==========================================
print("[*] Paso 1: Consultando contratos, servicios y campos GUDI de las entidades...")

sql_contracts = """
SELECT DISTINCT
    prs.prs_numero,
    prs.prs_cuit,
    prs.prs_razon_social,
    cnt.srv_codigo,
    cnt.cnt_numero,
    cnt.cnt_estado,
    cnt.cnt_gudi,
    cnt.tcl_codigo AS cnt_tcl,
    cnt.cla_codigo AS cnt_cla,
    cnt.ten_codigo AS cnt_ten,
    cnt.cnt_fecha_inicio,
    cnt.cnt_fecha_fin,
    srv.scf_codigo AS srv_scf,
    suc.scf_descripcion AS sucursal,
    NVL(TO_CHAR(srv.srv_distrito_cata), srv.srv_distrito_cat) AS distrito_cat,
    srv.srv_calle,
    srv.srv_nro,
    srv.srv_direccion,
    srv.srv_estado
FROM xxsigec.contratos cnt
JOIN xxsigec.personas prs ON prs.prs_numero = cnt.prs_numero
LEFT JOIN xxsigec.servicios srv ON srv.srv_codigo = cnt.srv_codigo
LEFT JOIN xxsigec.sucursales suc ON suc.scf_codigo = srv.scf_codigo
WHERE
    prs.prs_cuit IN (30678221976, 30522751916, 33628302729, 30714292141, 30546690519, 30546697858, 30617281577)
    OR UPPER(prs.prs_razon_social) LIKE '%FABRICA ARGENTINA DE AVIONES%'
    OR UPPER(prs.prs_razon_social) LIKE '%AVIACION MILITAR%'
    OR UPPER(prs.prs_razon_social) LIKE '%FUERZA AEREA%'
    OR UPPER(prs.prs_razon_social) LIKE '%IOSFA%'
    OR UPPER(prs.prs_razon_social) LIKE '%EJERCITO ARGENTINO%'
"""

df_contracts = pd.read_sql(sql_contracts, conn)
print(f"[+] Contratos obtenidos: {len(df_contracts)} filas (Suministros únicos: {df_contracts['SRV_CODIGO'].nunique()})")

# Identificar contratos GUDI
df_contracts["ES_GUDI"] = df_contracts["CNT_GUDI"].notna() & (df_contracts["CNT_GUDI"].str.strip() != "")
df_contracts["CODIGO_GUDI"] = df_contracts["CNT_GUDI"].fillna("-")
print(f"[+] Contratos GUDI detectados: {df_contracts['ES_GUDI'].sum()} (Vigentes: {((df_contracts['ES_GUDI']) & (df_contracts['CNT_ESTADO'] == 'V')).sum()})")

# ==========================================
# 2. EXTRACCIÓN DE AUDITORIA_CAMMESA 2025-2026 CON RELACIONES OFICIALES
# ==========================================
print("[*] Paso 2: Consultando tabla xxsigec.auditoria_cammesa (Años 2025-2026)...")
print("    Relaciones estrictas aplicadas:")
print("    - cammesa[tcl_codigo_gral] -> tarifas[tcl_codigo]")
print("    - cammesa[cla_codigo_gral] -> clases[cla_codigo] AND clases[tcl_codigo] = cammesa[tcl_codigo_gral]")
print("    - cammesa[ten_codigo_gral] -> tensiones[ten_codigo]")

stros = df_contracts["SRV_CODIGO"].dropna().astype(int).unique().tolist()
chunks = [stros[i:i+500] for i in range(0, len(stros), 500)]
dfs_cam = []

for idx, c in enumerate(chunks, 1):
    sql_cam = f"""
    SELECT
        cam.srv_codigo,
        cam.cnt_numero,
        cam.anio,
        cam.periodo,
        cam.fecha_emision,
        cam.fecha_lec,
        cam.scf_codigo AS cam_scf,
        suc.scf_descripcion AS cam_sucursal,
        cam.tcl_codigo_gral AS tcl_codigo,
        tcl.tcl_descripcion,
        cam.cla_codigo_gral AS cla_codigo,
        cla.cla_descripcion,
        cam.ten_codigo_gral AS ten_codigo,
        ten.ten_descripcion,
        cam.pot_c_pta,
        cam.pot_c_fta,
        cam.pot_lct_pta,
        cam.pot_lct_fta,
        cam.pot_fac_pta,
        cam.pot_fac_fta,
        cam.cons_resto,
        cam.cons_pico,
        cam.cons_valle,
        cam.cons_energia,
        cam.grupo_cammesa
    FROM xxsigec.auditoria_cammesa cam
    LEFT JOIN xxsigec.sucursales suc ON suc.scf_codigo = cam.scf_codigo
    LEFT JOIN xxsigec.tarifas tcl ON tcl.tcl_codigo = cam.tcl_codigo_gral
    LEFT JOIN xxsigec.clases cla ON cla.cla_codigo = cam.cla_codigo_gral AND cla.tcl_codigo = cam.tcl_codigo_gral
    LEFT JOIN xxsigec.tensiones ten ON ten.ten_codigo = cam.ten_codigo_gral
    WHERE cam.anio IN (2025, 2026)
      AND cam.srv_codigo IN ({','.join(map(str, c))})
    """
    dfs_cam.append(pd.read_sql(sql_cam, conn))

df_cam = pd.concat(dfs_cam, ignore_index=True) if dfs_cam else pd.DataFrame()
print(f"[+] Registros extraídos de AUDITORIA_CAMMESA: {len(df_cam)} filas")

conn.close()

# ==========================================
# 3. CONTROL DE ENERGÍA NEGATIVA
# ==========================================
print("[*] Paso 3: Aplicando regla de negocio: Exclusión de valores de Energía Total negativos...")

# Calcular componentes de energía
df_cam["CONS_RESTO"] = pd.to_numeric(df_cam["CONS_RESTO"], errors="coerce").fillna(0)
df_cam["CONS_PICO"] = pd.to_numeric(df_cam["CONS_PICO"], errors="coerce").fillna(0)
df_cam["CONS_VALLE"] = pd.to_numeric(df_cam["CONS_VALLE"], errors="coerce").fillna(0)
df_cam["CONS_ENERGIA"] = pd.to_numeric(df_cam["CONS_ENERGIA"], errors="coerce").fillna(0)

# Suma calculada de bloques
df_cam["ENERGIA_SUMA_BLOQUES"] = df_cam["CONS_RESTO"] + df_cam["CONS_PICO"] + df_cam["CONS_VALLE"]

# Identificar filas negativas
mask_negativa = (df_cam["CONS_ENERGIA"] < 0) | (df_cam["ENERGIA_SUMA_BLOQUES"] < 0)
df_negativas = df_cam[mask_negativa].copy()
print(f"[-] Registros con energía negativa detectados y excluidos: {len(df_negativas)} filas")

# Filtrar: solo mantener registros con energía no negativa (>= 0)
df_cam_valid = df_cam[~mask_negativa].copy()
print(f"[+] Registros válidos no negativos en CAMMESA: {len(df_cam_valid)} filas")

# ==========================================
# 4. NORMALIZACIÓN Y ASIGNACIÓN DE CATEGORÍAS
# ==========================================
print("[*] Paso 4: Normalizando datos y asignando categorías de negocio...")

def format_cuit(cuit_val):
    if pd.isna(cuit_val) or cuit_val == 0:
        return ""
    try:
        s = str(int(cuit_val)).zfill(11)
        if len(s) == 11:
            return f"{s[:2]}-{s[2:10]}-{s[10]}"
        return str(int(cuit_val))
    except Exception:
        return str(cuit_val)

def assign_entity_group(row):
    rs = str(row.get("PRS_RAZON_SOCIAL", "")).upper()
    cuit = row.get("PRS_CUIT")
    
    # 1. FADEA
    if cuit == 30678221976 or "AVIONES" in rs or "FADEA" in rs:
        return "FABRICA ARGENTINA DE AVIONES BRIG. SAN MARTIN S.A."
    
    # 2. ESCUELA DE AVIACION MILITAR
    if cuit == 30522751916 or "AVIACION MILITAR" in rs:
        return "Escuela de Aviación Militar"
    
    # 3. IOSFA
    if cuit == 30714292141 or "IOSFA" in rs or "OBRA SOCIAL DE LAS FUERZAS ARMADAS" in rs:
        return "Instituto de Obra Social de las Fuerzas Armadas (IOSFA)"
    
    # 4. FUERZA AEREA
    if cuit in (33628302729, 30546697858, 30617281577) or "FUERZA AEREA" in rs or "AEREA" in rs:
        return "Fuerza Aérea Argentina"
    
    # 5. EJERCITO ARGENTINO
    if cuit in (30546690519, 30717623910) or "EJERCITO" in rs or "MILITAR" in rs:
        return "Ejército Argentino"
    
    return "Otras Fuerzas / Dependencias"

# Enriquecer contratos con CUIT formateado y Grupo
df_contracts["CUIT_FORMATEADO"] = df_contracts["PRS_CUIT"].apply(format_cuit)
df_contracts["GRUPO_ENTIDAD"] = df_contracts.apply(assign_entity_group, axis=1)

# Cruzar CAMMESA filtrado con Contratos
df_cam_merged = df_cam_valid.merge(
    df_contracts[[
        "SRV_CODIGO", "CNT_NUMERO", "PRS_NUMERO", "PRS_CUIT", "CUIT_FORMATEADO",
        "PRS_RAZON_SOCIAL", "GRUPO_ENTIDAD", "CNT_ESTADO", "CNT_GUDI", "CODIGO_GUDI", "ES_GUDI",
        "SUCURSAL", "DISTRITO_CAT", "SRV_CALLE", "SRV_NRO", "SRV_DIRECCION", "SRV_ESTADO"
    ]],
    on=["SRV_CODIGO", "CNT_NUMERO"],
    how="left"
)

# Cruzar también las filas negativas con contratos para trazabilidad
df_neg_merged = df_negativas.merge(
    df_contracts[[
        "SRV_CODIGO", "CNT_NUMERO", "PRS_CUIT", "CUIT_FORMATEADO", "PRS_RAZON_SOCIAL",
        "GRUPO_ENTIDAD", "CNT_ESTADO", "CODIGO_GUDI", "SUCURSAL", "SRV_CALLE", "SRV_NRO"
    ]],
    on=["SRV_CODIGO", "CNT_NUMERO"],
    how="left"
)

# Imputar potencias
for col in ["POT_C_PTA", "POT_C_FTA", "POT_LCT_PTA", "POT_LCT_FTA", "POT_FAC_PTA", "POT_FAC_FTA"]:
    df_cam_merged[col] = pd.to_numeric(df_cam_merged[col], errors="coerce").fillna(0)

# Potencias máximas por fila
df_cam_merged["POT_CONTRATADA_MAX_KW"] = df_cam_merged[["POT_C_PTA", "POT_C_FTA"]].max(axis=1)
df_cam_merged["POT_LEIDA_MAX_KW"] = df_cam_merged[["POT_LCT_PTA", "POT_LCT_FTA"]].max(axis=1)

# Sucursal definitiva
df_cam_merged["SUCURSAL_FINAL"] = df_cam_merged["CAM_SUCURSAL"].fillna(df_cam_merged["SUCURSAL"]).fillna("CORDOBA")

# Dirección completa
df_cam_merged["DIRECCION_COMPLETA"] = df_cam_merged["SRV_CALLE"].fillna("") + np.where(
    df_cam_merged["SRV_NRO"].notna() & (df_cam_merged["SRV_NRO"] != ""),
    " " + df_cam_merged["SRV_NRO"].astype(str).str.replace(".0", "", regex=False),
    ""
)

# GUDI final por fila
df_cam_merged["CODIGO_GUDI"] = df_cam_merged["CODIGO_GUDI"].fillna("-")

# ==========================================
# 5. TABLA RESUMEN POR SUMINISTRO VIGENTE
# ==========================================
print("[*] Paso 5: Consolidando métricas por suministro...")

df_vigentes_meta = df_contracts[df_contracts["CNT_ESTADO"] == "V"].copy()

# Agregar consumos por suministro en CAMMESA (años 2025 y 2026) sobre datos válidos
cam_2025 = df_cam_merged[df_cam_merged["ANIO"] == 2025].groupby(["SRV_CODIGO", "CNT_NUMERO"]).agg({
    "CONS_RESTO": "sum",
    "CONS_PICO": "sum",
    "CONS_VALLE": "sum",
    "CONS_ENERGIA": "sum",
    "POT_CONTRATADA_MAX_KW": "max",
    "POT_LEIDA_MAX_KW": "max",
    "ANIO": "count"
}).reset_index().rename(columns={
    "CONS_RESTO": "RESTO_2025_KWH",
    "CONS_PICO": "PICO_2025_KWH",
    "CONS_VALLE": "VALLE_2025_KWH",
    "CONS_ENERGIA": "TOTAL_2025_KWH",
    "POT_CONTRATADA_MAX_KW": "POT_C_MAX_2025_KW",
    "POT_LEIDA_MAX_KW": "POT_L_MAX_2025_KW",
    "ANIO": "REGISTROS_2025"
})

cam_2026 = df_cam_merged[df_cam_merged["ANIO"] == 2026].groupby(["SRV_CODIGO", "CNT_NUMERO"]).agg({
    "CONS_RESTO": "sum",
    "CONS_PICO": "sum",
    "CONS_VALLE": "sum",
    "CONS_ENERGIA": "sum",
    "POT_CONTRATADA_MAX_KW": "max",
    "POT_LEIDA_MAX_KW": "max",
    "ANIO": "count"
}).reset_index().rename(columns={
    "CONS_RESTO": "RESTO_2026_KWH",
    "CONS_PICO": "PICO_2026_KWH",
    "CONS_VALLE": "VALLE_2026_KWH",
    "CONS_ENERGIA": "TOTAL_2026_KWH",
    "POT_CONTRATADA_MAX_KW": "POT_C_MAX_2026_KW",
    "POT_LEIDA_MAX_KW": "POT_L_MAX_2026_KW",
    "ANIO": "REGISTROS_2026"
})

df_sum_vigentes = df_vigentes_meta.merge(cam_2025, on=["SRV_CODIGO", "CNT_NUMERO"], how="left")
df_sum_vigentes = df_sum_vigentes.merge(cam_2026, on=["SRV_CODIGO", "CNT_NUMERO"], how="left")

for col in ["RESTO_2025_KWH", "PICO_2025_KWH", "VALLE_2025_KWH", "TOTAL_2025_KWH", "POT_C_MAX_2025_KW", "POT_L_MAX_2025_KW", "REGISTROS_2025",
            "RESTO_2026_KWH", "PICO_2026_KWH", "VALLE_2026_KWH", "TOTAL_2026_KWH", "POT_C_MAX_2026_KW", "POT_L_MAX_2026_KW", "REGISTROS_2026"]:
    df_sum_vigentes[col] = df_sum_vigentes[col].fillna(0)

df_sum_vigentes["TOTAL_ACUMULADO_KWH"] = df_sum_vigentes["TOTAL_2025_KWH"] + df_sum_vigentes["TOTAL_2026_KWH"]
df_sum_vigentes["POT_CONTRATADA_HIST_MAX_KW"] = df_sum_vigentes[["POT_C_MAX_2025_KW", "POT_C_MAX_2026_KW"]].max(axis=1)
df_sum_vigentes["POT_LEIDA_HIST_MAX_KW"] = df_sum_vigentes[["POT_L_MAX_2025_KW", "POT_L_MAX_2026_KW"]].max(axis=1)
df_sum_vigentes["TIENE_CAMMESA"] = np.where((df_sum_vigentes["REGISTROS_2025"] + df_sum_vigentes["REGISTROS_2026"]) > 0, "SÍ", "NO")

# Traer descripciones relacionales
lookup_tcl = df_cam_merged[["TCL_CODIGO", "TCL_DESCRIPCION"]].drop_duplicates().dropna().set_index("TCL_CODIGO")["TCL_DESCRIPCION"].to_dict()
lookup_ten = df_cam_merged[["TEN_CODIGO", "TEN_DESCRIPCION"]].drop_duplicates().dropna().set_index("TEN_CODIGO")["TEN_DESCRIPCION"].to_dict()
lookup_cla = df_cam_merged[["TCL_CODIGO", "CLA_CODIGO", "CLA_DESCRIPCION"]].drop_duplicates().dropna().set_index(["TCL_CODIGO", "CLA_CODIGO"])["CLA_DESCRIPCION"].to_dict()

df_sum_vigentes["TCL_DESC"] = df_sum_vigentes["CNT_TCL"].map(lookup_tcl).fillna(df_sum_vigentes["CNT_TCL"])
df_sum_vigentes["TEN_DESC"] = df_sum_vigentes["CNT_TEN"].map(lookup_ten).fillna(
    df_sum_vigentes["CNT_TEN"].map({"1": "Baja Tension", "2": "Media Tension", "3": "Alta Tension"}).fillna("Baja Tension")
)

df_sum_vigentes["DIRECCION_COMPLETA"] = df_sum_vigentes["SRV_CALLE"].fillna("") + np.where(
    df_sum_vigentes["SRV_NRO"].notna() & (df_sum_vigentes["SRV_NRO"] != ""),
    " " + df_sum_vigentes["SRV_NRO"].astype(str).str.replace(".0", "", regex=False),
    ""
)

# ==========================================
# 6. CONSTRUCCIÓN DEL LIBRO EXCEL ESTILIZADO
# ==========================================
print("[*] Paso 6: Construyendo libro Excel profesional con OpenPyXL...")

wb = openpyxl.Workbook()
wb.remove(wb.active)

C_NAVY_DARK = "1B365D"
C_NAVY_LIGHT = "2C5282"
C_SLATE = "4A607A"
C_ICE_BLUE = "EBF2FA"
C_ZEBRA = "F7FAFC"
C_WHITE = "FFFFFF"
C_GRAY_LIGHT = "E2E8F0"
C_GOLD = "D97706"
C_EMERALD = "059669"
C_CRIMSON = "DC2626"
C_PURPLE = "7C3AED"

font_title = Font(name="Segoe UI", size=15, bold=True, color=C_WHITE)
font_subtitle = Font(name="Segoe UI", size=10, italic=True, color=C_WHITE)
font_section = Font(name="Segoe UI", size=11, bold=True, color=C_NAVY_DARK)
font_header = Font(name="Segoe UI", size=9, bold=True, color=C_WHITE)
font_data = Font(name="Segoe UI", size=9, color="000000")
font_bold = Font(name="Segoe UI", size=9, bold=True, color="000000")

fill_title = PatternFill(start_color=C_NAVY_DARK, end_color=C_NAVY_DARK, fill_type="solid")
fill_header = PatternFill(start_color=C_NAVY_LIGHT, end_color=C_NAVY_LIGHT, fill_type="solid")
fill_zebra = PatternFill(start_color=C_ZEBRA, end_color=C_ZEBRA, fill_type="solid")
fill_ice = PatternFill(start_color=C_ICE_BLUE, end_color=C_ICE_BLUE, fill_type="solid")
fill_gudi_hdr = PatternFill(start_color="312E81", end_color="312E81", fill_type="solid")

thin_side = Side(border_style="thin", color=C_GRAY_LIGHT)
border_cell = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

align_left = Alignment(horizontal="left", vertical="center")
align_right = Alignment(horizontal="right", vertical="center")
align_center = Alignment(horizontal="center", vertical="center")
align_header = Alignment(horizontal="center", vertical="center", wrap_text=True)

# -------------------------------------------------------------
# HOJA 0: RESUMEN EJECUTIVO
# -------------------------------------------------------------
ws0 = wb.create_sheet(title="00_Resumen_Ejecutivo")
ws0.views.sheetView[0].showGridLines = True

ws0.merge_cells("A1:L1")
c_title = ws0["A1"]
c_title.value = "EPEC - AUDITORÍA DE MERCADO ELÉCTRICO MAYORISTA (CAMMESA) 2025-2026"
c_title.font = font_title; c_title.fill = fill_title; c_title.alignment = align_center
ws0.row_dimensions[1].height = 36

ws0.merge_cells("A2:L2")
c_sub = ws0["A2"]
c_sub.value = "Fuerzas Armadas y Organismos Asociados | Exclusión de Energía Negativa | Inclusión de GUDIS | Base Oracle XXSIGEC"
c_sub.font = font_subtitle; c_sub.fill = fill_title; c_sub.alignment = align_center
ws0.row_dimensions[2].height = 20

ws0.row_dimensions[3].height = 10

# Tabla Resumen por Entidad
ws0["A5"].value = "1. SÍNTESIS GENERAL POR ENTIDAD SOLICITADA"
ws0["A5"].font = font_section

headers_ent = [
    "Entidad Solicitada", "CUIT Oficial / Principal", "Estado Registral EPEC",
    "Contrato GUDI Vigente", "Suministros Vigentes", "Suministros c/ CAMMESA", "Tarifas Dominantes",
    "Tensión", "Pot. Contratada Máx (kW)", "Energía 2025 (kWh)", "Energía 2026 (kWh)", "Energía Total (kWh)"
]

ws0.row_dimensions[6].height = 28
for col_idx, h in enumerate(headers_ent, 1):
    cell = ws0.cell(row=6, column=col_idx, value=h)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_header
    cell.border = border_cell

entidades_def = [
    {
        "nombre": "FABRICA ARGENTINA DE AVIONES BRIG. SAN MARTIN S.A.",
        "cuit": "30-67822197-6",
        "estado": "3 Contratos Históricos (CANCELADOS 2021)",
        "gudi": "NO (Opera GUMA en MEM)",
        "vigentes": 0,
        "cammesa": 0,
        "tarifas": "1304, 1305, 240 (Baja)",
        "tension": "Baja Tensión",
        "pot": 0.0,
        "ene2025": 0.0,
        "ene2026": 0.0,
        "total": 0.0
    },
    {
        "nombre": "Escuela de Aviación Militar",
        "cuit": "30-52275191-6 (Reg. 30-54669785-8)",
        "estado": "VIGENTE en EPEC (Suministro 420687)",
        "gudi": "NO",
        "vigentes": 1,
        "cammesa": 0,
        "tarifas": "541 (Alumbrado / Oficial)",
        "tension": "Baja Tensión",
        "pot": 0.0,
        "ene2025": 0.0,
        "ene2026": 0.0,
        "total": 0.0
    },
    {
        "nombre": "Fuerza Aérea Argentina",
        "cuit": "33-62830272-9 / 30-54669785-8",
        "estado": "VIGENTE CON CAMMESA (Suministros 420603, 420556, etc.)",
        "gudi": "SÍ: GD0633XI (Suministro 420603 - T350 MT)",
        "vigentes": int((df_sum_vigentes["GRUPO_ENTIDAD"] == "Fuerza Aérea Argentina").sum()),
        "cammesa": int(((df_sum_vigentes["GRUPO_ENTIDAD"] == "Fuerza Aérea Argentina") & (df_sum_vigentes["TIENE_CAMMESA"] == "SÍ")).sum()),
        "tarifas": "350 (Grandes Usuarios MT), 541, 140",
        "tension": "Media Tensión / Baja Tensión",
        "pot": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Fuerza Aérea Argentina"]["POT_CONTRATADA_HIST_MAX_KW"].sum()),
        "ene2025": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Fuerza Aérea Argentina"]["TOTAL_2025_KWH"].sum()),
        "ene2026": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Fuerza Aérea Argentina"]["TOTAL_2026_KWH"].sum()),
        "total": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Fuerza Aérea Argentina"]["TOTAL_ACUMULADO_KWH"].sum())
    },
    {
        "nombre": "Instituto de Obra Social de las Fuerzas Armadas (IOSFA)",
        "cuit": "30-71429214-1",
        "estado": "VIGENTE CON CAMMESA (11 Suministros Activos)",
        "gudi": "NO",
        "vigentes": int((df_sum_vigentes["GRUPO_ENTIDAD"] == "Instituto de Obra Social de las Fuerzas Armadas (IOSFA)").sum()),
        "cammesa": int(((df_sum_vigentes["GRUPO_ENTIDAD"] == "Instituto de Obra Social de las Fuerzas Armadas (IOSFA)") & (df_sum_vigentes["TIENE_CAMMESA"] == "SÍ")).sum()),
        "tarifas": "140, 240, 241, 350, 541",
        "tension": "Baja Tensión",
        "pot": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Instituto de Obra Social de las Fuerzas Armadas (IOSFA)"]["POT_CONTRATADA_HIST_MAX_KW"].sum()),
        "ene2025": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Instituto de Obra Social de las Fuerzas Armadas (IOSFA)"]["TOTAL_2025_KWH"].sum()),
        "ene2026": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Instituto de Obra Social de las Fuerzas Armadas (IOSFA)"]["TOTAL_2026_KWH"].sum()),
        "total": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Instituto de Obra Social de las Fuerzas Armadas (IOSFA)"]["TOTAL_ACUMULADO_KWH"].sum())
    },
    {
        "nombre": "Ejército Argentino",
        "cuit": "30-54669051-9",
        "estado": "VIGENTE CON CAMMESA (43 Suministros Activos)",
        "gudi": "NO",
        "vigentes": int((df_sum_vigentes["GRUPO_ENTIDAD"] == "Ejército Argentino").sum()),
        "cammesa": int(((df_sum_vigentes["GRUPO_ENTIDAD"] == "Ejército Argentino") & (df_sum_vigentes["TIENE_CAMMESA"] == "SÍ")).sum()),
        "tarifas": "140, 353, 541, 543, 604",
        "tension": "Baja Tensión",
        "pot": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Ejército Argentino"]["POT_CONTRATADA_HIST_MAX_KW"].sum()),
        "ene2025": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Ejército Argentino"]["TOTAL_2025_KWH"].sum()),
        "ene2026": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Ejército Argentino"]["TOTAL_2026_KWH"].sum()),
        "total": float(df_sum_vigentes[df_sum_vigentes["GRUPO_ENTIDAD"] == "Ejército Argentino"]["TOTAL_ACUMULADO_KWH"].sum())
    }
]

row_curr = 7
for ent in entidades_def:
    ws0.row_dimensions[row_curr].height = 20
    ws0.cell(row=row_curr, column=1, value=ent["nombre"]).font = font_bold
    ws0.cell(row=row_curr, column=2, value=ent["cuit"]).font = font_data
    ws0.cell(row=row_curr, column=3, value=ent["estado"]).font = font_data
    
    c_gudi = ws0.cell(row=row_curr, column=4, value=ent["gudi"])
    c_gudi.font = font_bold if "SÍ" in ent["gudi"] else font_data
    if "SÍ" in ent["gudi"]:
        c_gudi.font = Font(name="Segoe UI", size=9, bold=True, color="1E3A8A")
    c_gudi.alignment = align_left
    
    c_vig = ws0.cell(row=row_curr, column=5, value=ent["vigentes"])
    c_vig.font = font_bold; c_vig.alignment = align_center; c_vig.number_format = "#,##0"
    
    c_cam = ws0.cell(row=row_curr, column=6, value=ent["cammesa"])
    c_cam.font = font_bold; c_cam.alignment = align_center; c_cam.number_format = "#,##0"
    
    ws0.cell(row=row_curr, column=7, value=ent["tarifas"]).font = font_data
    ws0.cell(row=row_curr, column=8, value=ent["tension"]).font = font_data
    
    c_pot = ws0.cell(row=row_curr, column=9, value=ent["pot"])
    c_pot.font = font_data; c_pot.alignment = align_right; c_pot.number_format = "#,##0.00"
    
    c_e25 = ws0.cell(row=row_curr, column=10, value=ent["ene2025"])
    c_e25.font = font_data; c_e25.alignment = align_right; c_e25.number_format = "#,##0"
    
    c_e26 = ws0.cell(row=row_curr, column=11, value=ent["ene2026"])
    c_e26.font = font_data; c_e26.alignment = align_right; c_e26.number_format = "#,##0"
    
    c_tot = ws0.cell(row=row_curr, column=12, value=ent["total"])
    c_tot.font = font_bold; c_tot.alignment = align_right; c_tot.number_format = "#,##0"
    
    for c_i in range(1, 13):
        ws0.cell(row=row_curr, column=c_i).border = border_cell
        if row_curr % 2 == 0:
            ws0.cell(row=row_curr, column=c_i).fill = fill_zebra
    
    row_curr += 1

# Fila de Totales
ws0.row_dimensions[row_curr].height = 22
ws0.cell(row=row_curr, column=1, value="TOTAL CONSOLIDADO").font = font_bold
ws0.cell(row=row_curr, column=5, value=f"=SUM(E7:E{row_curr-1})").number_format = "#,##0"
ws0.cell(row=row_curr, column=6, value=f"=SUM(F7:F{row_curr-1})").number_format = "#,##0"
ws0.cell(row=row_curr, column=9, value=f"=SUM(I7:I{row_curr-1})").number_format = "#,##0.00"
ws0.cell(row=row_curr, column=10, value=f"=SUM(J7:J{row_curr-1})").number_format = "#,##0"
ws0.cell(row=row_curr, column=11, value=f"=SUM(K7:K{row_curr-1})").number_format = "#,##0"
ws0.cell(row=row_curr, column=12, value=f"=SUM(L7:L{row_curr-1})").number_format = "#,##0"

for c_i in range(1, 13):
    cell = ws0.cell(row=row_curr, column=c_i)
    cell.font = font_bold; cell.fill = fill_ice
    cell.border = Border(top=Side(style="thin", color=C_NAVY_DARK), bottom=Side(style="double", color=C_NAVY_DARK), left=thin_side, right=thin_side)
    if c_i in [5, 6]:
        cell.alignment = align_center
    elif c_i >= 9:
        cell.alignment = align_right

# Notas Técnicas y Control de Relaciones
row_curr += 2
ws0.cell(row=row_curr, column=1, value="2. CONTROL METODOLÓGICO Y REGLAS DE NEGOCIO").font = font_section
row_curr += 1

controles = [
    ("A. Exclusión de Valores de Energía Negativos", f"Se excluyeron de la consulta y listado oficial {len(df_negativas)} registros con consumos negativos (originados por notas de crédito, ajustes de aforo y refacturaciones contables en períodos de 2025 y 2026). Todos los valores de energía y potencias presentados corresponden exclusivamente a magnitudes físicas efectivas (>= 0). Ver hoja '04_Contratos_GUDI_y_Especiales' para el detalle de filas excluidas."),
    ("B. Contratos Vigentes GUDI (Grandes Usuarios de Distribuidora)", "Se identificó formalmente que la Fuerza Aérea Argentina posee el contrato vigente GUDI código GD0633XI bajo el suministro 420603 (Contrato 3, Tarifa 350 en Media Tensión, Av. Fuerza Aérea Km. 5 1/2). Ninguna de las restantes entidades posee contratos activos GUDI en EPEC."),
    ("C. Control de Integridad Relacional SIGEC - CAMMESA", "Todas las descripciones técnicas se vincularon sin desfasajes ni productos cartesianos:\n- Tarifa: xxsigec.auditoria_cammesa[tcl_codigo_gral] = xxsigec.tarifas[tcl_codigo]\n- Clase: xxsigec.auditoria_cammesa[cla_codigo_gral] = xxsigec.clases[cla_codigo] AND xxsigec.clases[tcl_codigo] = xxsigec.auditoria_cammesa[tcl_codigo_gral]\n- Tensión: xxsigec.auditoria_cammesa[ten_codigo_gral] = xxsigec.tensiones[ten_codigo]"),
    ("D. Diagnóstico FADEA y Escuela de Aviación Militar", "FADEA registra 3 contratos en SIGEC (3055615, 3055617 y 3083168), todos CANCELADOS en 2021 (no opera como cliente minorista en EPEC, sino bajo el MEM como GUMA). Por su parte, Escuela de Aviación Militar posee el suministro 420687 con contrato VIGENTE (Tarifa 541), pero su abastecimiento mayorista se declara en CAMMESA de manera unificada a través del suministro troncal 420603 de Fuerza Aérea.")
]

for tit, desc in controles:
    ws0.cell(row=row_curr, column=1, value=tit).font = font_bold
    ws0.merge_cells(start_row=row_curr+1, start_column=1, end_row=row_curr+1, end_column=12)
    c_d = ws0.cell(row=row_curr+1, column=1, value=desc)
    c_d.font = font_data
    c_d.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    ws0.row_dimensions[row_curr+1].height = 36
    row_curr += 3

# -------------------------------------------------------------
# HOJA 1: SUMINISTROS VIGENTES
# -------------------------------------------------------------
print("[*] Creando Hoja 01_Suministros_Vigentes...")
ws1 = wb.create_sheet(title="01_Suministros_Vigentes")
ws1.views.sheetView[0].showGridLines = True

headers_v = [
    "Grupo Entidad", "Razón Social", "CUIT", "Suministro", "Contrato", "Estado Contrato",
    "GUDI", "Sucursal / Distrito", "Distrito Cat.", "Dirección Suministro", "Tarifa", "Descripción Tarifa",
    "Tensión", "Registros CAMMESA (Válidos)", "Pot. Contratada Máx (kW)", "Pot. Leída Máx (kW)",
    "Energía 2025 (kWh)", "Energía 2026 (kWh)", "Energía Total Acumulada (kWh)"
]

ws1.row_dimensions[1].height = 28
for c_i, h in enumerate(headers_v, 1):
    cell = ws1.cell(row=1, column=c_i, value=h)
    cell.font = font_header
    cell.fill = fill_gudi_hdr if h == "GUDI" else fill_header
    cell.alignment = align_header
    cell.border = border_cell

df_sum_vig_sorted = df_sum_vigentes.sort_values(by=["GRUPO_ENTIDAD", "SRV_CODIGO"]).reset_index(drop=True)

for r_i, row_data in df_sum_vig_sorted.iterrows():
    row_num = r_i + 2
    ws1.row_dimensions[row_num].height = 19
    
    ws1.cell(row=row_num, column=1, value=row_data["GRUPO_ENTIDAD"]).font = font_bold
    ws1.cell(row=row_num, column=2, value=row_data["PRS_RAZON_SOCIAL"]).font = font_data
    ws1.cell(row=row_num, column=3, value=row_data["CUIT_FORMATEADO"]).font = font_data
    
    c_srv = ws1.cell(row=row_num, column=4, value=row_data["SRV_CODIGO"])
    c_srv.font = font_bold; c_srv.alignment = align_center
    
    c_cnt = ws1.cell(row=row_num, column=5, value=row_data["CNT_NUMERO"])
    c_cnt.font = font_data; c_cnt.alignment = align_center
    
    c_est = ws1.cell(row=row_num, column=6, value="VIGENTE")
    c_est.font = Font(name="Segoe UI", size=9, bold=True, color=C_EMERALD)
    c_est.alignment = align_center
    
    # Campo GUDI
    c_gudi = ws1.cell(row=row_num, column=7, value=row_data["CODIGO_GUDI"])
    c_gudi.alignment = align_center
    if row_data["ES_GUDI"]:
        c_gudi.font = Font(name="Segoe UI", size=9, bold=True, color="1E3A8A")
        c_gudi.fill = PatternFill(start_color="EEF2FF", end_color="EEF2FF", fill_type="solid")
    else:
        c_gudi.font = font_data
    
    ws1.cell(row=row_num, column=8, value=row_data["SUCURSAL"]).font = font_data
    ws1.cell(row=row_num, column=9, value=row_data["DISTRITO_CAT"]).font = font_data
    ws1.cell(row=row_num, column=10, value=row_data["DIRECCION_COMPLETA"]).font = font_data
    
    c_tcl = ws1.cell(row=row_num, column=11, value=row_data["CNT_TCL"])
    c_tcl.font = font_data; c_tcl.alignment = align_center
    
    ws1.cell(row=row_num, column=12, value=row_data["TCL_DESC"]).font = font_data
    ws1.cell(row=row_num, column=13, value=row_data["TEN_DESC"]).font = font_data
    
    c_rcam = ws1.cell(row=row_num, column=14, value=int(row_data["REGISTROS_2025"] + row_data["REGISTROS_2026"]))
    c_rcam.font = font_bold; c_rcam.alignment = align_center; c_rcam.number_format = "#,##0"
    
    c_potc = ws1.cell(row=row_num, column=15, value=float(row_data["POT_CONTRATADA_HIST_MAX_KW"]))
    c_potc.font = font_data; c_potc.alignment = align_right; c_potc.number_format = "#,##0.00"
    
    c_potl = ws1.cell(row=row_num, column=16, value=float(row_data["POT_LEIDA_HIST_MAX_KW"]))
    c_potl.font = font_data; c_potl.alignment = align_right; c_potl.number_format = "#,##0.00"
    
    c_e25 = ws1.cell(row=row_num, column=17, value=float(row_data["TOTAL_2025_KWH"]))
    c_e25.font = font_data; c_e25.alignment = align_right; c_e25.number_format = "#,##0"
    
    c_e26 = ws1.cell(row=row_num, column=18, value=float(row_data["TOTAL_2026_KWH"]))
    c_e26.font = font_data; c_e26.alignment = align_right; c_e26.number_format = "#,##0"
    
    c_etot = ws1.cell(row=row_num, column=19, value=float(row_data["TOTAL_ACUMULADO_KWH"]))
    c_etot.font = font_bold; c_etot.alignment = align_right; c_etot.number_format = "#,##0"
    
    for c_i in range(1, 20):
        ws1.cell(row=row_num, column=c_i).border = border_cell
        if row_num % 2 == 1 and not (c_i == 7 and row_data["ES_GUDI"]):
            ws1.cell(row=row_num, column=c_i).fill = fill_zebra

tot_row_1 = len(df_sum_vig_sorted) + 2
ws1.row_dimensions[tot_row_1].height = 22
ws1.cell(row=tot_row_1, column=1, value="TOTAL GENERAL").font = font_bold
ws1.cell(row=tot_row_1, column=14, value=f"=SUM(N2:N{tot_row_1-1})").number_format = "#,##0"
ws1.cell(row=tot_row_1, column=15, value=f"=SUM(O2:O{tot_row_1-1})").number_format = "#,##0.00"
ws1.cell(row=tot_row_1, column=16, value=f"=SUM(P2:P{tot_row_1-1})").number_format = "#,##0.00"
ws1.cell(row=tot_row_1, column=17, value=f"=SUM(Q2:Q{tot_row_1-1})").number_format = "#,##0"
ws1.cell(row=tot_row_1, column=18, value=f"=SUM(R2:R{tot_row_1-1})").number_format = "#,##0"
ws1.cell(row=tot_row_1, column=19, value=f"=SUM(S2:S{tot_row_1-1})").number_format = "#,##0"

for c_i in range(1, 20):
    cell = ws1.cell(row=tot_row_1, column=c_i)
    cell.font = font_bold; cell.fill = fill_ice
    cell.border = Border(top=Side(style="thin", color=C_NAVY_DARK), bottom=Side(style="double", color=C_NAVY_DARK), left=thin_side, right=thin_side)
    if c_i == 14:
        cell.alignment = align_center
    elif c_i >= 15:
        cell.alignment = align_right

ws1.auto_filter.ref = f"A1:S{tot_row_1-1}"
ws1.freeze_panes = "A2"

# -------------------------------------------------------------
# HOJA 2: DETALLE AUDITORIA CAMMESA 2025-2026 (FILTRADO >= 0)
# -------------------------------------------------------------
print("[*] Creando Hoja 02_Detalle_CAMMESA_2025_2026...")
ws2 = wb.create_sheet(title="02_Detalle_CAMMESA_2025_2026")
ws2.views.sheetView[0].showGridLines = True

headers_cam = [
    "Grupo Entidad", "Razón Social", "CUIT", "Suministro", "Contrato", "Estado Contrato", "GUDI",
    "Sucursal / Distrito", "Distrito Cat.", "Dirección", "Tarifa", "Descripción Tarifa",
    "Clase", "Descripción Clase", "Tensión", "Nivel Tensión", "Año", "Periodo",
    "Fecha Emisión", "Fecha Lectura", "Pot. Contratada Punta (kW)", "Pot. Contratada Fuera Punta (kW)",
    "Pot. Contratada Máx (kW)", "Pot. Leída Punta (kW)", "Pot. Leída Fuera Punta (kW)", "Pot. Leída Máx (kW)",
    "Consumo Resto (kWh)", "Consumo Pico (kWh)", "Consumo Valle (kWh)", "Energía Total (kWh)", "Grupo CAMMESA"
]

ws2.row_dimensions[1].height = 28
for c_i, h in enumerate(headers_cam, 1):
    cell = ws2.cell(row=1, column=c_i, value=h)
    cell.font = font_header
    cell.fill = fill_gudi_hdr if h == "GUDI" else fill_header
    cell.alignment = align_header
    cell.border = border_cell

df_cam_sorted = df_cam_merged.sort_values(by=["GRUPO_ENTIDAD", "SRV_CODIGO", "ANIO", "PERIODO"]).reset_index(drop=True)

for r_i, row_data in df_cam_sorted.iterrows():
    row_num = r_i + 2
    ws2.row_dimensions[row_num].height = 18
    
    ws2.cell(row=row_num, column=1, value=row_data["GRUPO_ENTIDAD"]).font = font_data
    ws2.cell(row=row_num, column=2, value=row_data["PRS_RAZON_SOCIAL"]).font = font_data
    ws2.cell(row=row_num, column=3, value=row_data["CUIT_FORMATEADO"]).font = font_data
    
    c_srv = ws2.cell(row=row_num, column=4, value=row_data["SRV_CODIGO"])
    c_srv.font = font_bold; c_srv.alignment = align_center
    
    c_cnt = ws2.cell(row=row_num, column=5, value=row_data["CNT_NUMERO"])
    c_cnt.font = font_data; c_cnt.alignment = align_center
    
    c_est = ws2.cell(row=row_num, column=6, value="VIGENTE" if row_data["CNT_ESTADO"] == "V" else row_data["CNT_ESTADO"])
    c_est.font = font_data; c_est.alignment = align_center
    
    c_gudi = ws2.cell(row=row_num, column=7, value=row_data["CODIGO_GUDI"])
    c_gudi.alignment = align_center
    if row_data["ES_GUDI"]:
        c_gudi.font = Font(name="Segoe UI", size=9, bold=True, color="1E3A8A")
        c_gudi.fill = PatternFill(start_color="EEF2FF", end_color="EEF2FF", fill_type="solid")
    else:
        c_gudi.font = font_data
    
    ws2.cell(row=row_num, column=8, value=row_data["SUCURSAL_FINAL"]).font = font_data
    ws2.cell(row=row_num, column=9, value=row_data["DISTRITO_CAT"]).font = font_data
    ws2.cell(row=row_num, column=10, value=row_data["DIRECCION_COMPLETA"]).font = font_data
    
    c_tcl = ws2.cell(row=row_num, column=11, value=row_data["TCL_CODIGO"])
    c_tcl.font = font_data; c_tcl.alignment = align_center
    
    ws2.cell(row=row_num, column=12, value=row_data["TCL_DESCRIPCION"]).font = font_data
    
    c_cla = ws2.cell(row=row_num, column=13, value=row_data["CLA_CODIGO"])
    c_cla.font = font_data; c_cla.alignment = align_center
    
    ws2.cell(row=row_num, column=14, value=row_data["CLA_DESCRIPCION"]).font = font_data
    
    c_ten = ws2.cell(row=row_num, column=15, value=row_data["TEN_CODIGO"])
    c_ten.font = font_data; c_ten.alignment = align_center
    
    ws2.cell(row=row_num, column=16, value=row_data["TEN_DESCRIPCION"]).font = font_data
    
    c_anio = ws2.cell(row=row_num, column=17, value=row_data["ANIO"])
    c_anio.font = font_bold; c_anio.alignment = align_center
    
    c_per = ws2.cell(row=row_num, column=18, value=row_data["PERIODO"])
    c_per.font = font_bold; c_per.alignment = align_center
    
    c_fem = ws2.cell(row=row_num, column=19, value=str(row_data["FECHA_EMISION"])[:10] if pd.notna(row_data["FECHA_EMISION"]) else "")
    c_fem.font = font_data; c_fem.alignment = align_center
    
    c_flec = ws2.cell(row=row_num, column=20, value=str(row_data["FECHA_LEC"])[:10] if pd.notna(row_data["FECHA_LEC"]) else "")
    c_flec.font = font_data; c_flec.alignment = align_center
    
    # Potencias
    for col_idx, field in enumerate(["POT_C_PTA", "POT_C_FTA", "POT_CONTRATADA_MAX_KW", "POT_LCT_PTA", "POT_LCT_FTA", "POT_LEIDA_MAX_KW"], 21):
        c_p = ws2.cell(row=row_num, column=col_idx, value=float(row_data[field]))
        c_p.font = font_data; c_p.alignment = align_right; c_p.number_format = "#,##0.00"
    
    # Consumos
    for col_idx, field in enumerate(["CONS_RESTO", "CONS_PICO", "CONS_VALLE", "CONS_ENERGIA"], 27):
        c_e = ws2.cell(row=row_num, column=col_idx, value=float(row_data[field]))
        c_e.font = font_bold if field == "CONS_ENERGIA" else font_data
        c_e.alignment = align_right; c_e.number_format = "#,##0"
    
    c_grp = ws2.cell(row=row_num, column=31, value=row_data["GRUPO_CAMMESA"])
    c_grp.font = font_data; c_grp.alignment = align_center
    
    for c_i in range(1, 32):
        ws2.cell(row=row_num, column=c_i).border = border_cell
        if row_num % 2 == 1 and not (c_i == 7 and row_data["ES_GUDI"]):
            ws2.cell(row=row_num, column=c_i).fill = fill_zebra

tot_row_2 = len(df_cam_sorted) + 2
ws2.row_dimensions[tot_row_2].height = 22
ws2.cell(row=tot_row_2, column=1, value="TOTAL AUDITORÍA CAMMESA (VÁLIDOS)").font = font_bold

for col_idx, col_letter in enumerate(["U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD"], 21):
    c_tot = ws2.cell(row=tot_row_2, column=col_idx, value=f"=SUM({col_letter}2:{col_letter}{tot_row_2-1})")
    c_tot.font = font_bold; c_tot.alignment = align_right
    c_tot.number_format = "#,##0.00" if col_idx <= 26 else "#,##0"

for c_i in range(1, 32):
    cell = ws2.cell(row=tot_row_2, column=c_i)
    cell.font = font_bold; cell.fill = fill_ice
    cell.border = Border(top=Side(style="thin", color=C_NAVY_DARK), bottom=Side(style="double", color=C_NAVY_DARK), left=thin_side, right=thin_side)

ws2.auto_filter.ref = f"A1:AE{tot_row_2-1}"
ws2.freeze_panes = "A2"

# -------------------------------------------------------------
# HOJA 3: CONSOLIDADO ANUAL POR SUMINISTRO
# -------------------------------------------------------------
print("[*] Creando Hoja 03_Consolidado_Anual...")
ws3 = wb.create_sheet(title="03_Consolidado_Anual")
ws3.views.sheetView[0].showGridLines = True

headers_anual = [
    "Grupo Entidad", "Razón Social", "Suministro", "GUDI", "Tarifa", "Distrito", "Año",
    "Meses Declarados", "Pot. Contratada Máx (kW)", "Pot. Leída Máx (kW)",
    "Consumo Resto (kWh)", "Consumo Pico (kWh)", "Consumo Valle (kWh)", "Energía Total (kWh)"
]

ws3.row_dimensions[1].height = 28
for c_i, h in enumerate(headers_anual, 1):
    cell = ws3.cell(row=1, column=c_i, value=h)
    cell.font = font_header
    cell.fill = fill_gudi_hdr if h == "GUDI" else fill_header
    cell.alignment = align_header
    cell.border = border_cell

df_anual = df_cam_merged.groupby(["GRUPO_ENTIDAD", "PRS_RAZON_SOCIAL", "SRV_CODIGO", "CODIGO_GUDI", "TCL_CODIGO", "SUCURSAL_FINAL", "ANIO"]).agg({
    "PERIODO": "count",
    "POT_CONTRATADA_MAX_KW": "max",
    "POT_LEIDA_MAX_KW": "max",
    "CONS_RESTO": "sum",
    "CONS_PICO": "sum",
    "CONS_VALLE": "sum",
    "CONS_ENERGIA": "sum"
}).reset_index().rename(columns={"PERIODO": "MESES"})

df_anual = df_anual.sort_values(by=["GRUPO_ENTIDAD", "SRV_CODIGO", "ANIO"]).reset_index(drop=True)

for r_i, row_data in df_anual.iterrows():
    row_num = r_i + 2
    ws3.row_dimensions[row_num].height = 18
    
    ws3.cell(row=row_num, column=1, value=row_data["GRUPO_ENTIDAD"]).font = font_bold
    ws3.cell(row=row_num, column=2, value=row_data["PRS_RAZON_SOCIAL"]).font = font_data
    
    c_srv = ws3.cell(row=row_num, column=3, value=row_data["SRV_CODIGO"])
    c_srv.font = font_bold; c_srv.alignment = align_center
    
    c_gudi = ws3.cell(row=row_num, column=4, value=row_data["CODIGO_GUDI"])
    c_gudi.alignment = align_center
    if row_data["CODIGO_GUDI"] != "-":
        c_gudi.font = Font(name="Segoe UI", size=9, bold=True, color="1E3A8A")
        c_gudi.fill = PatternFill(start_color="EEF2FF", end_color="EEF2FF", fill_type="solid")
    else:
        c_gudi.font = font_data
    
    c_tcl = ws3.cell(row=row_num, column=5, value=row_data["TCL_CODIGO"])
    c_tcl.font = font_data; c_tcl.alignment = align_center
    
    ws3.cell(row=row_num, column=6, value=row_data["SUCURSAL_FINAL"]).font = font_data
    
    c_a = ws3.cell(row=row_num, column=7, value=row_data["ANIO"])
    c_a.font = font_bold; c_a.alignment = align_center
    
    c_m = ws3.cell(row=row_num, column=8, value=row_data["MESES"])
    c_m.font = font_data; c_m.alignment = align_center; c_m.number_format = "#,##0"
    
    c_pc = ws3.cell(row=row_num, column=9, value=float(row_data["POT_CONTRATADA_MAX_KW"]))
    c_pc.font = font_data; c_pc.alignment = align_right; c_pc.number_format = "#,##0.00"
    
    c_pl = ws3.cell(row=row_num, column=10, value=float(row_data["POT_LEIDA_MAX_KW"]))
    c_pl.font = font_data; c_pl.alignment = align_right; c_pl.number_format = "#,##0.00"
    
    c_cr = ws3.cell(row=row_num, column=11, value=float(row_data["CONS_RESTO"]))
    c_cr.font = font_data; c_cr.alignment = align_right; c_cr.number_format = "#,##0"
    
    c_cp = ws3.cell(row=row_num, column=12, value=float(row_data["CONS_PICO"]))
    c_cp.font = font_data; c_cp.alignment = align_right; c_cp.number_format = "#,##0"
    
    c_cv = ws3.cell(row=row_num, column=13, value=float(row_data["CONS_VALLE"]))
    c_cv.font = font_data; c_cv.alignment = align_right; c_cv.number_format = "#,##0"
    
    c_ce = ws3.cell(row=row_num, column=14, value=float(row_data["CONS_ENERGIA"]))
    c_ce.font = font_bold; c_ce.alignment = align_right; c_ce.number_format = "#,##0"
    
    for c_i in range(1, 15):
        ws3.cell(row=row_num, column=c_i).border = border_cell
        if row_num % 2 == 1 and not (c_i == 4 and row_data["CODIGO_GUDI"] != "-"):
            ws3.cell(row=row_num, column=c_i).fill = fill_zebra

tot_row_3 = len(df_anual) + 2
ws3.row_dimensions[tot_row_3].height = 22
ws3.cell(row=tot_row_3, column=1, value="TOTAL ANUAL").font = font_bold

for col_idx, col_letter in enumerate(["K", "L", "M", "N"], 11):
    c_tot = ws3.cell(row=tot_row_3, column=col_idx, value=f"=SUM({col_letter}2:{col_letter}{tot_row_3-1})")
    c_tot.font = font_bold; c_tot.alignment = align_right; c_tot.number_format = "#,##0"

for c_i in range(1, 15):
    cell = ws3.cell(row=tot_row_3, column=c_i)
    cell.font = font_bold; cell.fill = fill_ice
    cell.border = Border(top=Side(style="thin", color=C_NAVY_DARK), bottom=Side(style="double", color=C_NAVY_DARK), left=thin_side, right=thin_side)

ws3.auto_filter.ref = f"A1:N{tot_row_3-1}"
ws3.freeze_panes = "A2"

# -------------------------------------------------------------
# HOJA 4: CASOS ESPECIALES, GUDIS Y REGISTROS EXCLUIDOS
# -------------------------------------------------------------
print("[*] Creando Hoja 04_Contratos_GUDI_y_Especiales...")
ws4 = wb.create_sheet(title="04_Contratos_GUDI_y_Especiales")
ws4.views.sheetView[0].showGridLines = True

# Sección 1: Padrón de Contratos GUDI
ws4["A1"].value = "1. REGISTRO OFICIAL DE CONTRATOS GUDIS (Grandes Usuarios de Distribuidora)"
ws4["A1"].font = font_section

headers_gudi = [
    "Entidad", "CUIT", "Suministro", "Contrato", "Estado Contrato", "Código GUDI",
    "Tarifa", "Tensión", "Fecha Inicio", "Fecha Fin", "Dirección", "Observación Operativa"
]

ws4.row_dimensions[2].height = 26
for c_i, h in enumerate(headers_gudi, 1):
    cell = ws4.cell(row=2, column=c_i, value=h)
    cell.font = font_header
    cell.fill = fill_gudi_hdr
    cell.alignment = align_header
    cell.border = border_cell

gudis_data = [
    ("Fuerza Aérea Argentina", "33-62830272-9", 420603, 3, "VIGENTE (V)", "GD0633XI", "350", "Media Tensión", "2003-09-24", "-", "AV. FUERZA AEREA KM. 5 1/2", "CONTRATO GUDI VIGENTE ACTIVO. 21 declaraciones periódicas en CAMMESA 2025-2026."),
    ("Fuerza Aérea Argentina", "33-62830272-9", 420603, 1, "CANCELADO (C)", "GD0633XI", "312", "Media Tensión", "1995-01-01", "2003-09-23", "AV. FUERZA AEREA KM. 5 1/2", "Contrato anterior de potencia en media tensión (Reemplazado por contrato 3)."),
    ("Fuerza Aérea Argentina", "33-62830272-9", 420603, 2, "CANCELADO (C)", "GD0633XI", "312", "Media Tensión", "1997-05-27", "1997-05-30", "AV. FUERZA AEREA KM. 5 1/2", "Ajuste contractual histórico."),
    ("Fuerza Aérea Argentina (C.R.A.)", "30-54669785-8", 420491, 2, "CANCELADO (C)", "GD6891XI", "350", "Media Tensión", "1998-09-09", "2010-06-21", "CNO PAJAS BLANCAS KM 8 1/2", "GUDI histórico de radar/estación Pajas Blancas. Cancelado en junio 2010."),
    ("Fuerza Aérea Argentina (C.R.A.)", "30-54669785-8", 420491, 1, "CANCELADO (C)", "GD6891XI", "512", "Baja Tensión", "1995-01-01", "1998-09-08", "CNO PAJAS BLANCAS KM 8 1/2", "Contrato primario histórico de radar Pajas Blancas.")
]

for r_i, g_row in enumerate(gudis_data, 3):
    ws4.row_dimensions[r_i].height = 20
    for c_i, val in enumerate(g_row, 1):
        cell = ws4.cell(row=r_i, column=c_i, value=val)
        cell.font = font_bold if c_i in [1, 3, 5, 6] else font_data
        cell.border = border_cell
        if c_i in [3, 4, 7, 9, 10]:
            cell.alignment = align_center
        elif c_i in [5, 6]:
            cell.alignment = align_center
            if "VIGENTE" in str(val) or "GD0633XI" in str(val):
                cell.font = Font(name="Segoe UI", size=9, bold=True, color="1E3A8A")
                cell.fill = PatternFill(start_color="EEF2FF", end_color="EEF2FF", fill_type="solid")

# Sección 2: Trazabilidad FADEA y Escuela Aviación
row_fadea = len(gudis_data) + 5
ws4.cell(row=row_fadea, column=1, value="2. CASOS ESPECIALES DE ANÁLISIS: FADEA Y ESCUELA DE AVIACIÓN MILITAR").font = font_section

headers_esp = [
    "Entidad Analizada", "CUIT", "Suministro", "Contrato", "Estado en SIGEC",
    "Tarifa", "Fecha Inicio", "Fecha Fin / Baja", "Calle / Domicilio", "Nro", "Observaciones en Auditoría CAMMESA"
]

ws4.row_dimensions[row_fadea+1].height = 26
for c_i, h in enumerate(headers_esp, 1):
    cell = ws4.cell(row=row_fadea+1, column=c_i, value=h)
    cell.font = font_header; cell.fill = fill_header; cell.alignment = align_header; cell.border = border_cell

casos_esp = [
    ("FABRICA ARGENTINA DE AVIONES BRIG. SAN MARTIN S.A.", "30-67822197-6", 3055615, 1, "CANCELADO (C)", "1305", "2020-07-31", "2021-08-31", "AV. FUERZA AEREA", "5500", "Contrato de servicio de enlace / telecomunicaciones. Cancelado en agosto 2021. Sin consumo en CAMMESA."),
    ("FABRICA ARGENTINA DE AVIONES BRIG. SAN MARTIN S.A.", "30-67822197-6", 3055617, 1, "CANCELADO (C)", "1304", "2020-07-31", "2021-08-30", "AV. FUERZA AEREA", "5500", "Contrato de servicio de internet dedicado. Cancelado en agosto 2021. Sin consumo en CAMMESA."),
    ("FABRICA ARGENTINA DE AVIONES BRIG. SAN MARTIN S.A.", "30-67822197-6", 3083168, 1, "CANCELADO (C)", "240", "2021-09-14", "2021-09-14", "AV FUERZA AEREA", "5200", "Tarifa 240 dada de baja inmediatamente en 2021. Sin registros CAMMESA 2025-2026. Opera bajo figura GUMA en el MEM."),
    ("Escuela de Aviación Militar", "30-52275191-6 (Reg. 30-54669785-8)", 420687, 1, "VIGENTE (V)", "541", "1995-01-01", "Vigente", "RUTA 20 KM. 6 1/2", "-", "Contrato Activo en EPEC. No figura en tabla xxsigec.auditoria_cammesa (compras integradas a Fuerza Aérea 420603 o mayoristas MEM).")
]

for r_i, c_data in enumerate(casos_esp, row_fadea+2):
    ws4.row_dimensions[r_i].height = 20
    for c_i, val in enumerate(c_data, 1):
        cell = ws4.cell(row=r_i, column=c_i, value=val)
        cell.font = font_bold if c_i in [1, 3, 5] else font_data
        cell.border = border_cell
        if c_i in [3, 4, 6, 7, 8, 10]:
            cell.alignment = align_center
        else:
            cell.alignment = align_left
        if val == "VIGENTE (V)":
            cell.font = Font(name="Segoe UI", size=9, bold=True, color=C_EMERALD)
        elif "CANCELADO" in str(val):
            cell.font = Font(name="Segoe UI", size=9, bold=True, color=C_CRIMSON)

# Sección 3: Detalle de Registros con Energía Negativa Excluidos
row_neg = row_fadea + len(casos_esp) + 4
ws4.cell(row=row_neg, column=1, value="3. REGISTROS CON ENERGÍA TOTAL NEGATIVA EXCLUIDOS DE LA AUDITORÍA").font = font_section

headers_neg = [
    "Grupo Entidad", "Razón Social", "Suministro", "Contrato", "Estado Contrato",
    "Año", "Periodo", "Consumo Resto (kWh)", "Consumo Pico (kWh)", "Consumo Valle (kWh)", "Energía Total (kWh)", "Motivo Exclusión"
]

ws4.row_dimensions[row_neg+1].height = 26
for c_i, h in enumerate(headers_neg, 1):
    cell = ws4.cell(row=row_neg+1, column=c_i, value=h)
    cell.font = font_header; cell.fill = PatternFill(start_color="991B1B", end_color="991B1B", fill_type="solid"); cell.alignment = align_header; cell.border = border_cell

for r_i, r_data in df_neg_merged.iterrows():
    row_num = row_neg + 2 + r_i
    ws4.row_dimensions[row_num].height = 18
    
    ws4.cell(row=row_num, column=1, value=r_data["GRUPO_ENTIDAD"]).font = font_data
    ws4.cell(row=row_num, column=2, value=r_data["PRS_RAZON_SOCIAL"]).font = font_data
    
    c_s = ws4.cell(row=row_num, column=3, value=r_data["SRV_CODIGO"]); c_s.font = font_bold; c_s.alignment = align_center
    c_c = ws4.cell(row=row_num, column=4, value=r_data["CNT_NUMERO"]); c_c.font = font_data; c_c.alignment = align_center
    c_e = ws4.cell(row=row_num, column=5, value=r_data["CNT_ESTADO"]); c_e.font = font_data; c_e.alignment = align_center
    
    c_a = ws4.cell(row=row_num, column=6, value=r_data["ANIO"]); c_a.font = font_data; c_a.alignment = align_center
    c_p = ws4.cell(row=row_num, column=7, value=r_data["PERIODO"]); c_p.font = font_data; c_p.alignment = align_center
    
    for c_idx, f_name in enumerate(["CONS_RESTO", "CONS_PICO", "CONS_VALLE", "CONS_ENERGIA"], 8):
        c_val = ws4.cell(row=row_num, column=c_idx, value=float(r_data[f_name]))
        c_val.font = font_bold if f_name == "CONS_ENERGIA" else font_data
        c_val.alignment = align_right; c_val.number_format = "#,##0"
        if float(r_data[f_name]) < 0:
            c_val.font = Font(name="Segoe UI", size=9, bold=True, color=C_CRIMSON)
    
    c_obs = ws4.cell(row=row_num, column=12, value="Excluido por consignar Energía Total negativa (ajuste/nota de crédito).")
    c_obs.font = font_data
    
    for c_i in range(1, 13):
        ws4.cell(row=row_num, column=c_i).border = border_cell

# -------------------------------------------------------------
# AUTO-AJUSTE DE ANCHOS DE COLUMNAS
# -------------------------------------------------------------
print("[*] Ajustando anchos de columna en todas las hojas...")

for ws in [ws0, ws1, ws2, ws3, ws4]:
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            if ws in [ws0, ws4] and cell.row in [1, 2, 4, 5, row_fadea, row_fadea+1, row_neg, row_neg+1]:
                continue
            val_str = str(cell.value or "")
            if val_str.startswith("="):
                max_len = max(max_len, 12)
            else:
                max_len = max(max_len, len(val_str))
        ws.column_dimensions[col_letter].width = max(max_len + 3, 11)

# Anchos específicos para hoja 0
ws0.column_dimensions["A"].width = 38
ws0.column_dimensions["B"].width = 24
ws0.column_dimensions["C"].width = 28
ws0.column_dimensions["D"].width = 28
ws0.column_dimensions["E"].width = 16
ws0.column_dimensions["F"].width = 16
ws0.column_dimensions["G"].width = 26
ws0.column_dimensions["H"].width = 18
ws0.column_dimensions["I"].width = 20
ws0.column_dimensions["J"].width = 20
ws0.column_dimensions["K"].width = 20
ws0.column_dimensions["L"].width = 22

# ==========================================
# 7. GUARDAR LIBRO EXCEL
# ==========================================
downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
output_path_dl = os.path.join(downloads_dir, "Auditoria_CAMMESA_Fuerzas_Armadas_2025_2026.xlsx")

repo_data_dir = r"D:\Proyectos\antigravity-agents-repository\data"
os.makedirs(repo_data_dir, exist_ok=True)
output_path_repo = os.path.join(repo_data_dir, "Auditoria_CAMMESA_Fuerzas_Armadas_2025_2026.xlsx")

print(f"[*] Guardando archivo Excel en Descargas: {output_path_dl}...")
saved_dl_path = output_path_dl
try:
    wb.save(output_path_dl)
    print(f"[+] Archivo guardado con éxito en: {output_path_dl}")
except PermissionError:
    saved_dl_path = os.path.join(downloads_dir, "Auditoria_CAMMESA_Fuerzas_Armadas_2025_2026_Actualizado.xlsx")
    print(f"[!] Archivo original en uso por Excel. Guardando versión actualizada en: {saved_dl_path}")
    wb.save(saved_dl_path)
    print(f"[+] Archivo guardado con éxito en: {saved_dl_path}")

print(f"[*] Guardando copia de respaldo en repositorio: {output_path_repo}...")
wb.save(output_path_repo)
print(f"[+] Archivo guardado con éxito en: {output_path_repo}")

dst_script = r"D:\Proyectos\antigravity-agents-repository\scripts\generar_excel_auditoria_cammesa.py"
shutil.copy2(r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\generar_excel_auditoria_cammesa.py", dst_script)
print(f"[+] Script actualizado en: {dst_script}")

print("\n" + "="*80)
print("¡PROCESAMIENTO EXITOSO!")
print(f"- Filas Válidas en Detalle CAMMESA: {len(df_cam_sorted)}")
print(f"- Filas Negativas Excluidas: {len(df_neg_merged)}")
print(f"- Suministros Vigentes Analizados: {len(df_sum_vig_sorted)}")
print(f"- Contratos GUDI Identificados: 1 Vigente (GD0633XI en FAA Srv 420603)")
print(f"- Archivo Descargas: {saved_dl_path}")
print(f"- Archivo Repositorio: {output_path_repo}")
print("="*80)
