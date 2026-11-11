import os, time, oracledb, pandas as pd
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

# Catalogo DPP con agregacion de todos los pueblos/barrios asociados a cada DPP
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

print(f"[+] Diccionario DPP optimizado con {len(dpp_dict)} claves unicas.")

distritos_muestreo = [1, 18, 19, 20, 21, 24, 30, 47]
dfs = []
for d in distritos_muestreo:
    q = f"""
    SELECT 
        suministro, distrito, grupo_lectura, ruta_lectura, orden_lectura, 
        latitud, longitud, dc, localidad, barrio, datos_adicionales_domicilio
    FROM georef.vw_suministros
    WHERE distrito = {d} AND dc IS NOT NULL AND ROWNUM <= 50
    """
    dfs.append(pd.read_sql(q, conn))

q_gen = """
SELECT 
    suministro, distrito, grupo_lectura, ruta_lectura, orden_lectura, 
    latitud, longitud, dc, localidad, barrio, datos_adicionales_domicilio
FROM georef.vw_suministros
WHERE dc IS NOT NULL AND ROWNUM <= 100
"""
dfs.append(pd.read_sql(q_gen, conn))
conn.close()

df_total = pd.concat(dfs, ignore_index=True).drop_duplicates(subset=['SUMINISTRO'])

def descomponer_y_validar_dc(row):
    raw_dc = str(row['DC']).strip() if pd.notnull(row['DC']) else ""
    localidad = str(row['LOCALIDAD']).strip().upper() if pd.notnull(row['LOCALIDAD']) else ""
    barrio = str(row['BARRIO']).strip().upper() if pd.notnull(row['BARRIO']) else ""
    adicional = str(row['DATOS_ADICIONALES_DOMICILIO']).strip().upper() if pd.notnull(row['DATOS_ADICIONALES_DOMICILIO']) else ""

    res = {
        'suministro': row['SUMINISTRO'],
        'distrito': row['DISTRITO'],
        'grupo_lectura': row['GRUPO_LECTURA'],
        'ruta_lectura': row['RUTA_LECTURA'],
        'orden_lectura': row['ORDEN_LECTURA'],
        'latitud': row['LATITUD'],
        'longitud': row['LONGITUD'],
        'dc_original': raw_dc,
        'longitud_dc': len(raw_dc),
        'es_numerico': raw_dc.isdigit(),
        'dpto_cod': '',
        'pedania_cod': '',
        'pueblo_cod': '',
        'dpp_cod': '',
        'circ_cod': '',
        'secc_cod': '',
        'manzana_cod': '',
        'parcela_cod': '',
        'ph_cod': '',
        'dpto_nombre': '',
        'pedania_nombre': '',
        'pueblo_nombre': '',
        'localidad_origen': localidad,
        'barrio_origen': barrio,
        'adicional_origen': adicional,
        'coincidencia_geografica': 'SIN_VALIDAR',
        'cumple_normativa_rentas': False,
        'diagnostico_anomalia': []
    }

    if len(raw_dc) == 16:
        res['cumple_normativa_rentas'] = True
        res['dpto_cod'] = raw_dc[0:2]
        res['pedania_cod'] = raw_dc[2:4]
        res['pueblo_cod'] = raw_dc[4:6]
        res['dpp_cod'] = raw_dc[0:6]
        res['circ_cod'] = raw_dc[6:8]
        res['secc_cod'] = raw_dc[8:10]
        res['manzana_cod'] = raw_dc[10:13]
        res['parcela_cod'] = raw_dc[13:16]

    if res['dpp_cod'] in dpp_dict:
        info_dpp = dpp_dict[res['dpp_cod']]
        res['dpto_nombre'] = info_dpp['departamento']
        res['pedania_nombre'] = info_dpp['pedania']
        res['pueblo_nombre'] = info_dpp['pueblo_principal']

        pueblos = [p.upper() for p in info_dpp['todos_los_pueblos']]
        dpto = res['dpto_nombre'].upper()

        texto_comparacion = f"{localidad} {barrio} {adicional}".upper()
        
        # Evaluar coincidencia con cualquiera de los pueblos o barrios asociados al DPP
        coincide = False
        for p in pueblos:
            if p in texto_comparacion or localidad in p:
                coincide = True
                break
        
        if coincide:
            res['coincidencia_geografica'] = 'COINCIDENCIA_EXACTA_LOCALIDAD'
        elif dpto and (dpto in texto_comparacion or localidad in dpto):
            res['coincidencia_geografica'] = 'COINCIDENCIA_DEPARTAMENTO'
        else:
            res['coincidencia_geografica'] = 'DISCREPANCIA_O_REVISION'
            res['diagnostico_anomalia'].append(f"DPP_{res['dpp_cod']}_{res['pueblo_nombre']}_VS_{localidad}")

    if res['manzana_cod'] == '000' and res['parcela_cod'] == '000':
        res['diagnostico_anomalia'].append("MANZANA_Y_PARCELA_EN_CERO_GENERICA")

    res['diagnostico_str'] = "; ".join(res['diagnostico_anomalia']) if res['diagnostico_anomalia'] else "CONFORME_OK"
    return res

parsed = [descomponer_y_validar_dc(r) for _, r in df_total.iterrows()]
pdf = pd.DataFrame(parsed)

print("\n=== RESUMEN REFINADO ===")
print(f"Total registros: {len(pdf)}")
print("Coincidencia geografica:")
for k, v in pdf['coincidencia_geografica'].value_counts().items():
    print(f"  - {k}: {v} ({v*100.0/len(pdf):.1f}%)")

print("\nDiagnosticos de anomalia:")
for k, v in pdf['diagnostico_str'].value_counts().items():
    print(f"  - {k}: {v}")

descargas = os.path.expanduser(r"~\Downloads")
csv_path = os.path.join(descargas, "analisis_descomposicion_dc_rentas_cordoba.csv")
pdf.to_csv(csv_path, index=False, encoding="utf-8-sig")

def to_md_table(df_subset, cols):
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join(["---"] * len(cols)) + " |"
    lines = [header, sep]
    for _, r in df_subset.iterrows():
        row_str = "| " + " | ".join([str(r[c]).replace("\n", " ").replace("|", "-") for c in cols]) + " |"
        lines.append(row_str)
    return "\n".join(lines)

cols_md = ['suministro', 'distrito', 'localidad_origen', 'dc_original', 'dpp_cod', 'pueblo_nombre', 'circ_cod', 'secc_cod', 'manzana_cod', 'parcela_cod', 'coincidencia_geografica', 'diagnostico_str']
md_content = "# Muestra de Auditoría y Descomposición Catastral (Rentas Córdoba)\n\n"
md_content += f"**Total de Registros Analizados**: {len(pdf)}\n"
md_content += f"**Conformes a Estándar Rentas (16 dígitos)**: {pdf['cumple_normativa_rentas'].sum()} ({pdf['cumple_normativa_rentas'].mean()*100:.1f}%)\n"
md_content += f"**Coincidencia Geográfica Confirmada**: {(pdf['coincidencia_geografica'] == 'COINCIDENCIA_EXACTA_LOCALIDAD').sum()} ({(pdf['coincidencia_geografica'] == 'COINCIDENCIA_EXACTA_LOCALIDAD').mean()*100:.1f}%)\n"
md_content += f"**Discrepancias / A Revisar**: {(pdf['coincidencia_geografica'] == 'DISCREPANCIA_O_REVISION').sum()} ({(pdf['coincidencia_geografica'] == 'DISCREPANCIA_O_REVISION').mean()*100:.1f}%)\n\n"
md_content += "## Primeras 25 Filas Descompuestas\n\n"
md_content += to_md_table(pdf.head(25), cols_md)

discrepancias = pdf[pdf['coincidencia_geografica'] == 'DISCREPANCIA_O_REVISION']
if len(discrepancias) > 0:
    md_content += "\n\n## Discrepancias Geográficas Detectadas (Muestra)\n\n"
    md_content += to_md_table(discrepancias.head(15), cols_md)

md_path = os.path.join(descargas, "muestra_analisis_dc.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"\n[+] Archivo CSV actualizado en: {csv_path}")
print(f"[+] Archivo MD actualizado en: {md_path}")
