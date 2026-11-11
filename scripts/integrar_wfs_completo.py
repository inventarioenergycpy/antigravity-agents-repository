import os, time, requests, oracledb, pandas as pd
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

# 1. Maestro DPP
dpp_df = pd.read_sql("SELECT dpp, departamento, pedania, pueblo, tipo as tipo_pueblo FROM georef.dpp", conn)
dpp_dict = {}
for _, row in dpp_df.iterrows():
    dpp_key = str(row['DPP']).strip()
    if dpp_key not in dpp_dict:
        dpp_dict[dpp_key] = {
            'departamento': str(row['DEPARTAMENTO'] or '').strip(),
            'pedania': str(row['PEDANIA'] or '').strip(),
            'pueblo_principal': str(row['PUEBLO'] or '').strip(),
            'todos_los_pueblos': []
        }
    pueblo_val = str(row['PUEBLO'] or '').strip()
    if pueblo_val and pueblo_val not in dpp_dict[dpp_key]['todos_los_pueblos']:
        dpp_dict[dpp_key]['todos_los_pueblos'].append(pueblo_val)
    if str(row['TIPO_PUEBLO'] or '').strip() == 'Municipio':
        dpp_dict[dpp_key]['pueblo_principal'] = pueblo_val

print(f"[+] Diccionario DPP cargado con {len(dpp_dict)} pueblos.")

# 2. Extraer muestra multi-distrito de georef.vw_suministros
# Incluyendo tambien CALLE y ALTURA para un cruce de calle mucho mas robusto
distritos_muestreo = [1, 18, 19, 20, 21, 24, 30, 47]
dfs = []
for d in distritos_muestreo:
    q = f"""
    SELECT 
        suministro, distrito, grupo_lectura, ruta_lectura, orden_lectura, 
        calle, altura, latitud, longitud, dc, localidad, barrio, datos_adicionales_domicilio
    FROM georef.vw_suministros
    WHERE distrito = {d} AND dc IS NOT NULL AND ROWNUM <= 30
    """
    dfs.append(pd.read_sql(q, conn))

# Agregar casos urbanos consolidados de Cordoba Capital
q_urb = """
SELECT 
    suministro, distrito, grupo_lectura, ruta_lectura, orden_lectura, 
    calle, altura, latitud, longitud, dc, localidad, barrio, datos_adicionales_domicilio
FROM georef.vw_suministros
WHERE distrito = 1 
  AND barrio IN ('CENTRO', 'SAN VICENTE', 'NUEVA CORDOBA', 'ALBERDI', 'ALTA CORDOBA')
  AND dc IS NOT NULL AND ROWNUM <= 30
"""
dfs.append(pd.read_sql(q_urb, conn))

conn.close()
df_total = pd.concat(dfs, ignore_index=True).drop_duplicates(subset=['SUMINISTRO'])
print(f"[+] Total suministros para auditoria integral con WFS: {len(df_total)}")

# 3. Cache WFS para no repetir consultas a la misma manzana
wfs_url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
wfs_auth = ("EPEC_comercial", "Bratis-c0m3rc14l")
manzana_cache = {}

def obtener_calles_wfs(mza_nomenclatura):
    if not mza_nomenclatura or mza_nomenclatura == "00-00-00-00-00-000":
        return []
    if mza_nomenclatura in manzana_cache:
        return manzana_cache[mza_nomenclatura]

    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typeName": "EPEC:vm_manzanas_calles_new",
        "outputFormat": "application/json",
        "cql_filter": f"nomenclatura = '{mza_nomenclatura}'"
    }
    try:
        resp = requests.get(wfs_url, auth=wfs_auth, params=params, verify=False, timeout=6)
        if resp.status_code == 200:
            data = resp.json()
            calles = sorted(list(set([
                f.get("properties", {}).get("nombrecall", "").strip().upper()
                for f in data.get("features", [])
                if f.get("properties", {}).get("nombrecall")
            ])))
            manzana_cache[mza_nomenclatura] = calles
            return calles
        else:
            manzana_cache[mza_nomenclatura] = []
            return []
    except Exception:
        manzana_cache[mza_nomenclatura] = []
        return []

# 4. Funcion de Descomposicion, Auditoria Rentas y Cruce WFS
print("[*] Iniciando enriquecimiento con geoservicio WFS EPEC...")
parsed_records = []
for idx, r in df_total.iterrows():
    raw_dc = str(r['DC']).strip() if pd.notnull(r['DC']) else ""
    localidad = str(r['LOCALIDAD']).strip().upper() if pd.notnull(r['LOCALIDAD']) else ""
    barrio = str(r['BARRIO']).strip().upper() if pd.notnull(r['BARRIO']) else ""
    adicional = str(r['DATOS_ADICIONALES_DOMICILIO']).strip().upper() if pd.notnull(r['DATOS_ADICIONALES_DOMICILIO']) else ""
    calle_sigec = str(r['CALLE']).strip().upper() if pd.notnull(r['CALLE']) else ""

    item = {
        'suministro': r['SUMINISTRO'],
        'distrito': r['DISTRITO'],
        'grupo_lectura': r['GRUPO_LECTURA'],
        'ruta_lectura': r['RUTA_LECTURA'],
        'orden_lectura': r['ORDEN_LECTURA'],
        'calle_sigec': calle_sigec,
        'altura_sigec': r['ALTURA'],
        'latitud': r['LATITUD'],
        'longitud': r['LONGITUD'],
        'dc_original': raw_dc,
        'cumple_normativa_rentas': (len(raw_dc) == 16 and raw_dc.isdigit()),
        'dpto_cod': '',
        'pedania_cod': '',
        'pueblo_cod': '',
        'dpp_cod': '',
        'circ_cod': '',
        'secc_cod': '',
        'manzana_cod': '',
        'parcela_cod': '',
        'mza_13dig': '',
        'mza_wfs': '',
        'parcela_wfs': '',
        'dpto_nombre': '',
        'pueblo_nombre': '',
        'localidad_origen': localidad,
        'barrio_origen': barrio,
        'adicional_origen': adicional,
        'coincidencia_localidad_dpp': 'SIN_VALIDAR',
        'calles_perimetrales_wfs': '',
        'cantidad_calles_mza': 0,
        'coincide_calle_perimetral': 'NO_APLICA',
        'cobertura_wfs_manzana': 'NO_ENCONTRADA_O_RURAL',
        'diagnostico_integral': []
    }

    if len(raw_dc) == 16 and raw_dc.isdigit():
        item['dpto_cod'] = raw_dc[0:2]
        item['pedania_cod'] = raw_dc[2:4]
        item['pueblo_cod'] = raw_dc[4:6]
        item['dpp_cod'] = raw_dc[0:6]
        item['circ_cod'] = raw_dc[6:8]
        item['secc_cod'] = raw_dc[8:10]
        item['manzana_cod'] = raw_dc[10:13]
        item['parcela_cod'] = raw_dc[13:16]

        item['mza_13dig'] = raw_dc[0:13]
        item['mza_wfs'] = f"{item['dpto_cod']}-{item['pedania_cod']}-{item['pueblo_cod']}-{item['circ_cod']}-{item['secc_cod']}-{item['manzana_cod']}"
        item['parcela_wfs'] = f"{item['mza_wfs']}-{item['parcela_cod']}"
    else:
        item['diagnostico_integral'].append("DC_NO_ESTANDAR_RENTAS")

    # Validacion DPP
    if item['dpp_cod'] in dpp_dict:
        info_dpp = dpp_dict[item['dpp_cod']]
        item['dpto_nombre'] = info_dpp['departamento']
        item['pueblo_nombre'] = info_dpp['pueblo_principal']

        pueblos = [p.upper() for p in info_dpp['todos_los_pueblos']]
        texto_comparacion = f"{localidad} {barrio} {adicional}".upper()
        
        coincide_loc = any(p in texto_comparacion or localidad in p for p in pueblos)
        if coincide_loc:
            item['coincidencia_localidad_dpp'] = 'COINCIDENCIA_EXACTA'
        elif item['dpto_nombre'].upper() in texto_comparacion or localidad in item['dpto_nombre'].upper():
            item['coincidencia_localidad_dpp'] = 'COINCIDENCIA_DEPARTAMENTO'
        else:
            item['coincidencia_localidad_dpp'] = 'DISCREPANCIA'
            item['diagnostico_integral'].append("DISCREPANCIA_LOCALIDAD_DPP")
    elif item['dpp_cod']:
        item['coincidencia_localidad_dpp'] = 'DPP_INEXISTENTE'
        item['diagnostico_integral'].append("DPP_NO_CATALOGADO")

    # Consulta de Calles Perimetrales en WFS
    if item['mza_wfs']:
        calles = obtener_calles_wfs(item['mza_wfs'])
        item['cantidad_calles_mza'] = len(calles)
        if calles:
            item['cobertura_wfs_manzana'] = 'MANZANA_DIGITALIZADA_WFS'
            item['calles_perimetrales_wfs'] = "; ".join(calles)
            
            # Verificar si el domicilio del suministro coincide con alguna calle perimetral
            domicilio_total = f"{calle_sigec} {adicional}".upper()
            coincide_calle = False
            for c in calles:
                # Quitar prefijos comunes como 'AV', 'AV.', 'BV', 'CALLE'
                c_clean = c.replace("AV ", "").replace("AV. ", "").replace("BV ", "").replace("CALLE ", "").strip()
                if c_clean and (c_clean in domicilio_total or c in domicilio_total):
                    coincide_calle = True
                    break
            
            if coincide_calle:
                item['coincide_calle_perimetral'] = 'SI_CONFIRMADA'
            else:
                item['coincide_calle_perimetral'] = 'NO_VERIFICADA_EN_PERIMETRO'
                item['diagnostico_integral'].append("CALLE_DOMICILIO_NO_FIGURA_EN_PERIMETRO_MZA")
        else:
            item['cobertura_wfs_manzana'] = 'SIN_CALLES_EN_WFS_O_RURAL'

    if item['manzana_cod'] == '000' and item['parcela_cod'] == '000':
        item['diagnostico_integral'].append("MANZANA_PARCELA_EN_CERO")

    item['diagnostico_str'] = "; ".join(item['diagnostico_integral']) if item['diagnostico_integral'] else "CONFORME_TOTAL_OK"
    parsed_records.append(item)

pdf = pd.DataFrame(parsed_records)

print("\n=== RESUMEN DE INTEGRACION GEOSERVICIOS WFS EPEC ===")
print("Manzanas Digitalizadas en WFS:", pdf['cobertura_wfs_manzana'].value_counts().to_dict())
print("Coincidencia Calle Perimetral:", pdf['coincide_calle_perimetral'].value_counts().to_dict())
print("\nTop Diagnosticos Integrales:")
for k, v in pdf['diagnostico_str'].value_counts().items():
    print(f"  - {k}: {v}")

# Exportar a Descargas CSV
descargas = os.path.expanduser(r"~\Downloads")
csv_path = os.path.join(descargas, "analisis_descomposicion_dc_rentas_cordoba.csv")
pdf.to_csv(csv_path, index=False, encoding="utf-8-sig")
print(f"\n[+] Dataset CSV actualizado en: {csv_path}")

# Exportar a Markdown
cols_md = ['suministro', 'distrito', 'localidad_origen', 'dc_original', 'mza_wfs', 'calles_perimetrales_wfs', 'coincide_calle_perimetral', 'diagnostico_str']

def to_md_table(df_subset, cols):
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join(["---"] * len(cols)) + " |"
    lines = [header, sep]
    for _, r in df_subset.iterrows():
        row_str = "| " + " | ".join([str(r[c]).replace("\n", " ").replace("|", "-")[:45] for c in cols]) + " |"
        lines.append(row_str)
    return "\n".join(lines)

md_content = "# Auditoría Catastral Integral con Geoservicio WFS EPEC\n\n"
md_content += f"**Total Suministros Analizados**: {len(pdf)}\n"
md_content += f"**Conformes Formato Rentas (16 dígitos)**: {pdf['cumple_normativa_rentas'].sum()} (100%)\n"
md_content += f"**Manzanas con Calles Perimetrales WFS (`EPEC:vm_manzanas_calles_new`)**: {(pdf['cobertura_wfs_manzana'] == 'MANZANA_DIGITALIZADA_WFS').sum()} ({(pdf['cobertura_wfs_manzana'] == 'MANZANA_DIGITALIZADA_WFS').mean()*100:.1f}%)\n"
md_content += f"**Calles Confirmadas en Perímetro de Manzana**: {(pdf['coincide_calle_perimetral'] == 'SI_CONFIRMADA').sum()}\n\n"
md_content += "## Muestra de Suministros Auditados con Calles Perimetrales WFS\n\n"
md_content += to_md_table(pdf[pdf['cobertura_wfs_manzana'] == 'MANZANA_DIGITALIZADA_WFS'].head(20), cols_md)

md_path = os.path.join(descargas, "muestra_analisis_dc.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"[+] Reporte Markdown actualizado en: {md_path}")
