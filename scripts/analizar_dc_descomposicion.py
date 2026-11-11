import os, oracledb, pandas as pd, re
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

# 1. Cargar catalogo DPP oficial
dpp_df = pd.read_sql("SELECT dpp, departamento, pedania, pueblo, tipo as tipo_pueblo FROM georef.dpp", conn)
dpp_dict = {}
for _, row in dpp_df.iterrows():
    dpp_dict[str(row['DPP']).strip()] = {
        'departamento': row['DEPARTAMENTO'],
        'pedania': row['PEDANIA'],
        'pueblo': row['PUEBLO'],
        'tipo': row['TIPO_PUEBLO']
    }

print(f"[+] Catalogo oficial GEOREF.DPP cargado: {len(dpp_dict)} localidades/pueblos.")

# 2. Consultar muestra representativa de suministros de diferentes distritos
sql_sample = """
WITH ranked_suministros AS (
    SELECT 
        suministro,
        distrito,
        grupo_lectura,
        ruta_lectura,
        orden_lectura,
        latitud,
        longitud,
        dc,
        localidad,
        barrio,
        datos_adicionales_domicilio,
        ROW_NUMBER() OVER (PARTITION BY distrito ORDER BY suministro) as rn
    FROM georef.vw_suministros
    WHERE dc IS NOT NULL
)
SELECT 
    suministro,
    distrito,
    grupo_lectura,
    ruta_lectura,
    orden_lectura,
    latitud,
    longitud,
    dc,
    localidad,
    barrio,
    datos_adicionales_domicilio
FROM ranked_suministros
WHERE rn <= 20
ORDER BY distrito, suministro
"""

print("[*] Ejecutando consulta estratificada por distrito...")
df = pd.read_sql(sql_sample, conn)
conn.close()
print(f"[+] Registros extraidos: {len(df)} distribuidos en {df['DISTRITO'].nunique()} distritos.")

# 3. Funcion de descomposicion y validacion segun normativa Rentas de Cordoba
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

    if not raw_dc:
        res['diagnostico_anomalia'].append("DC_NULO")
        return res

    if not raw_dc.isdigit():
        res['diagnostico_anomalia'].append("CONTIENE_CARACTERES_NO_NUMERICOS")

    # Evaluacion de Estructura de 16 digitos (Normativa Rentas Cordoba: DD-PP-LL-CC-SS-MMM-PPP)
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
    elif len(raw_dc) == 15:
        # Formato Municipal Catastro Cordoba (CC-SS-MMM-PPP-PH)
        res['circ_cod'] = raw_dc[0:2]
        res['secc_cod'] = raw_dc[2:4]
        res['manzana_cod'] = raw_dc[4:7]
        res['parcela_cod'] = raw_dc[7:10]
        res['ph_cod'] = raw_dc[10:15]
        res['diagnostico_anomalia'].append("FORMATO_MUNICIPAL_15_DIGITOS")
    elif len(raw_dc) in (19, 20):
        # Formato Extendido con PH
        res['dpto_cod'] = raw_dc[0:2]
        res['pedania_cod'] = raw_dc[2:4]
        res['pueblo_cod'] = raw_dc[4:6]
        res['dpp_cod'] = raw_dc[0:6]
        res['circ_cod'] = raw_dc[6:8]
        res['secc_cod'] = raw_dc[8:10]
        res['manzana_cod'] = raw_dc[10:13]
        res['parcela_cod'] = raw_dc[13:16]
        res['ph_cod'] = raw_dc[16:]
        res['cumple_normativa_rentas'] = True
    else:
        res['diagnostico_anomalia'].append(f"LONGITUD_ATIPICA_{len(raw_dc)}")

    # Validacion contra catalogo oficial DPP
    if res['dpp_cod'] in dpp_dict:
        info_dpp = dpp_dict[res['dpp_cod']]
        res['dpto_nombre'] = info_dpp['departamento'] or ''
        res['pedania_nombre'] = info_dpp['pedania'] or ''
        res['pueblo_nombre'] = info_dpp['pueblo'] or ''

        pueblo = res['pueblo_nombre'].upper()
        dpto = res['dpto_nombre'].upper()

        # Constatacion con Localidad, Barrio y Datos Adicionales
        texto_comparacion = f"{localidad} {barrio} {adicional}"
        if pueblo in texto_comparacion or localidad in pueblo:
            res['coincidencia_geografica'] = 'COINCIDENCIA_EXACTA_LOCALIDAD'
        elif dpto in texto_comparacion or localidad in dpto:
            res['coincidencia_geografica'] = 'COINCIDENCIA_DEPARTAMENTO'
        else:
            res['coincidencia_geografica'] = 'DISCREPANCIA_O_REVISION'
            res['diagnostico_anomalia'].append("DISCREPANCIA_LOCALIDAD_VS_DPP")
    elif res['dpp_cod']:
        res['coincidencia_geografica'] = 'DPP_NO_ENCONTRADO_EN_CATALOGO'
        res['diagnostico_anomalia'].append("DPP_INEXISTENTE")

    # Deteccion de ceros ficticios (manzanas o parcelas vacias)
    if res['manzana_cod'] == '000' and res['parcela_cod'] == '000':
        res['diagnostico_anomalia'].append("MANZANA_Y_PARCELA_EN_CERO_GENERICA")

    res['diagnostico_str'] = "; ".join(res['diagnostico_anomalia']) if res['diagnostico_anomalia'] else "CONFORME_OK"
    return res

parsed_data = [descomponer_y_validar_dc(r) for _, r in df.iterrows()]
pdf = pd.DataFrame(parsed_data)

print("\n=== RESUMEN DE CONFORMIDAD NORMATIVA ===")
print("Cumple formato Rentas (16/19 dgitos):", pdf['cumple_normativa_rentas'].value_counts().to_dict())
print("Coincidencia geogrfica con Localidad/Barrio/Adicional:", pdf['coincidencia_geografica'].value_counts().to_dict())
print("Diagnsticos de anomala detectados:")
print(pdf['diagnostico_str'].value_counts().head(10))

# Exportar a CSV y MD en Descargas
descargas = os.path.expanduser(r"~\Downloads")
csv_out = os.path.join(descargas, "analisis_descomposicion_dc_rentas_cordoba.csv")
pdf.to_csv(csv_out, index=False, encoding="utf-8-sig")
print(f"\n[+] Exportado CSV completo a: {csv_out}")

# Guardar muestra en markdown
md_muestra = pdf[['suministro', 'distrito', 'localidad_origen', 'dc_original', 'dpp_cod', 'pueblo_nombre', 'circ_cod', 'secc_cod', 'manzana_cod', 'parcela_cod', 'coincidencia_geografica', 'diagnostico_str']].head(20)
md_out = os.path.join(descargas, "muestra_analisis_dc.md")
md_muestra.to_markdown(md_out, index=False)
print(f"[+] Exportada muestra MD a: {md_out}")
