"""
========================================================================================
SQUAD ARQUETIPO A - GIS, CATASTRO Y RUTAS EPEC
SPRINT 2: Motor de Convergencia en 4 Partes para Asignación Parcelaria de Suministros
========================================================================================
Autor: Operador 2 (Oracle & Dominio EPEC) & Operador 1 (Ingeniero Geoespacial)
Fecha: 25 de Octubre de 2026
Entrada: georef.vw_suministros (Circ 01) + Manzanas HR & Parcelas (Sprint 1)
Salida: data/convergencia_suministros_circ01.parquet & Reporte de Cobertura
========================================================================================
"""

import os, sys, time, json, math, re
import pandas as pd
import numpy as np

# Forzar salida utf-8 en consola Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Configurar librerías PROJ para entorno QGIS Python
os.environ['PROJ_LIB'] = r'C:\Program Files\QGIS 4.2.0\share\proj'
os.environ['PROJ_DATA'] = r'C:\Program Files\QGIS 4.2.0\share\proj'

import pyproj
import geopandas as gpd
from shapely.geometry import Point, Polygon, MultiPolygon, shape
from shapely.strtree import STRtree
from shapely.ops import transform
from dotenv import load_dotenv
import oracledb

load_dotenv(r"D:\Proyectos\.env")
load_dotenv(r"D:\Proyectos\antigravity-agents-repository\.env")

# 1. Normalizador de cadenas toponímicas (calles)
def normalizar_calle(txt):
    if not txt or pd.isna(txt):
        return ""
    txt = str(txt).upper().strip()
    # Eliminar acentos
    txt = re.sub(r'[ÁÀÄÂ]', 'A', txt)
    txt = re.sub(r'[ÉÈËÊ]', 'E', txt)
    txt = re.sub(r'[ÍÌÏÎ]', 'I', txt)
    txt = re.sub(r'[ÓÒÖÔ]', 'O', txt)
    txt = re.sub(r'[ÚÙÜÛ]', 'U', txt)
    txt = re.sub(r'Ñ', 'N', txt)
    # Eliminar prefijos viales habituales
    txt = re.sub(r'^(AVENIDA|AVDA|AV\.|AV|BOULEVARD|BV\.|BV|CALLE|PASAJE|PJE\.|PJE|CAMINO|CNO\.|CNO|RUTA|PBLICA|PUBLICA)\s+', '', txt)
    # Eliminar puntuación y espacios duplicados
    txt = re.sub(r'[^A-Z0-9\s]', ' ', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt

def normalizar_dc_cadena(dc_raw):
    if not dc_raw or pd.isna(dc_raw):
        return ""
    s = re.sub(r'[^0-9]', '', str(dc_raw).strip())
    # Si tiene 16 dígitos: 1101011711002358 -> 11-01-01-17-11-002-358
    if len(s) == 16:
        return f"{s[0:2]}-{s[2:4]}-{s[4:6]}-{s[6:8]}-{s[8:10]}-{s[10:13]}-{s[13:16]}"
    # Si tiene 13 dígitos (solo manzana): 1101011711002 -> 11-01-01-17-11-002
    elif len(s) == 13:
        return f"{s[0:2]}-{s[2:4]}-{s[4:6]}-{s[6:8]}-{s[8:10]}-{s[10:13]}"
    return s

def construir_cuaterna_str(distrito, zona, manzana, lote):
    try:
        d = int(distrito) if pd.notna(distrito) else 0
        z = int(zona) if pd.notna(zona) else 0
        m = int(manzana) if pd.notna(manzana) else 0
        l = int(lote) if pd.notna(lote) else 0
        if d > 0 and z > 0 and m > 0:
            parc_key = f"11-01-01-{d:02d}-{z:02d}-{m:03d}-{l:03d}" if l > 0 else ""
            mza_key = f"11-01-01-{d:02d}-{z:02d}-{m:03d}"
            return parc_key, mza_key
    except Exception:
        pass
    return "", ""

def extraer_suministros_oracle(cache_parquet_path):
    if os.path.exists(cache_parquet_path):
        print(f"📦 Cargando suministros desde caché local: {cache_parquet_path}")
        return pd.read_parquet(cache_parquet_path)
    
    print("🔌 Conectando a Oracle para extraer suministros de Circunscripción 01...")
    lib_dir = os.environ.get("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")
    try:
        oracledb.init_oracle_client(lib_dir=lib_dir)
    except Exception:
        pass

    dsn = oracledb.makedsn(host=os.environ["OR_HOST"], port=int(os.environ.get("OR_PORT", 1521)), service_name=os.environ["OR_SERVICE_NAME"])
    conn = oracledb.connect(user=os.environ["OR_USER"], password=os.environ["OR_PASS"], dsn=dsn)

    query = """
    SELECT 
        suministro, distrito, grupo_lectura, ruta_lectura, orden_lectura,
        dc, zona_catastral, distrito_catastral, manzana_catastral, lote_catastral, ph_catastral,
        calle, altura, latitud, longitud, barrio
    FROM georef.vw_suministros
    WHERE distrito = 1 AND (dc LIKE '11010101%' OR distrito_catastral = 1)
    """
    
    t0 = time.time()
    df = pd.read_sql(query, conn)
    conn.close()
    print(f"✅ Extraídos {len(df):,} suministros de Oracle en {time.time()-t0:.2f} s.")
    
    # Guardar en parquet
    df.to_parquet(cache_parquet_path, index=False)
    print(f"💾 Guardado en caché parquet: {cache_parquet_path}")
    return df

def ejecutar_motor_convergencia():
    data_dir = r"D:\Proyectos\antigravity-agents-repository\data"
    suministros_cache = os.path.join(data_dir, "suministros_circ01.parquet")
    mzas_geojson_path = os.path.join(data_dir, "manzanas_alta_resolucion_distrito1.geojson")
    
    print("=" * 80)
    print(" 🚀 INICIANDO SPRINT 2: MOTOR DE CONVERGENCIA EN 4 PARTES")
    print("=" * 80)
    
    # 1. Cargar Manzanas de Alta Resolución (Sprint 1)
    print("\n📂 Cargando Manzanas de Alta Resolución sintetizadas en Sprint 1...")
    with open(mzas_geojson_path, 'r', encoding='utf-8') as f:
        mzas_geojson = json.load(f)
        
    mzas_dict = {}
    mzas_geoms = []
    mzas_keys = []
    
    for feat in mzas_geojson['features']:
        props = feat['properties']
        mza_key = props['mza_wfs']
        poly = shape(feat['geometry'])
        
        # Calles perimetrales normalizadas
        calles_perim = set()
        for c in props.get('calles_perimetrales', '').split(','):
            c_norm = normalizar_calle(c)
            if c_norm:
                calles_perim.add(c_norm)
                
        mzas_dict[mza_key] = {
            'cant_parcelas': props['cant_parcelas'],
            'superficie_ha': props['superficie_ha'],
            'centroide_lat': props['centroide_lat'],
            'centroide_lon': props['centroide_lon'],
            'calles_norm': calles_perim,
            'geom': poly
        }
        mzas_geoms.append(poly)
        mzas_keys.append(mza_key)
        
    print(f"   ✓ {len(mzas_dict):,} Manzanas HR cargadas con frentes viales normalizados.")
    
    # Índice espacial R-Tree sobre las manzanas
    print("🌳 Construyendo índice espacial STRtree sobre Manzanas HR...")
    tree = STRtree(mzas_geoms)
    print("   ✓ Índice espacial activo.")

    # 2. Cargar Parcelas descargadas en Sprint 1
    cache_wfs_dir = os.path.join(data_dir, "cache_parcelas_wfs")
    parcelas_dict = {} # nom_formateada -> {mza_nom, calles_norm}
    
    print("\n📂 Indexando parcelas oficiales desde caché WFS...")
    import glob
    for pfile in glob.glob(os.path.join(cache_wfs_dir, "circ_01_sec_*.json")):
        with open(pfile, 'r', encoding='utf-8') as f:
            pfeats = json.load(f)
        for pf in pfeats:
            p_props = pf.get('properties', {})
            nom_raw = (p_props.get('nomenclatura') or '').strip()
            if not nom_raw:
                continue
            
            calle_norm = normalizar_calle(p_props.get('nombrecall'))
            
            tokens = nom_raw.split('-')
            if len(tokens) >= 6:
                mza_nom = "-".join(tokens[:6])
            else:
                mza_nom = nom_raw[:18]
                
            if nom_raw not in parcelas_dict:
                parcelas_dict[nom_raw] = {
                    'mza_nom': mza_nom,
                    'calles_norm': set()
                }
            if calle_norm:
                parcelas_dict[nom_raw]['calles_norm'].add(calle_norm)
                
    print(f"   ✓ {len(parcelas_dict):,} Parcelas oficiales indexadas.")

    # 3. Cargar Suministros
    df_sum = extraer_suministros_oracle(suministros_cache)
    print(f"\n⚡ Ejecutando Motor de Convergencia sobre {len(df_sum):,} suministros...")
    
    t_conv_start = time.time()
    
    resultados = []
    
    c_alta_dc = 0
    c_alta_multi = 0
    c_media_vecinos = 0
    c_parcial_manzana = 0
    c_sin_match = 0
    
    for idx, r in df_sum.iterrows():
        sum_id = r['SUMINISTRO']
        dc_raw = r['DC']
        calle_sum_norm = normalizar_calle(r['CALLE'])
        lat = r['LATITUD']
        lon = r['LONGITUD']
        
        # 1. Dimensión 1: DC Exacta
        dc_formateada = normalizar_dc_cadena(dc_raw)
        dim1_parc_match = False
        dim1_mza_match = False
        mza_candidata_dim1 = ""
        
        if dc_formateada in parcelas_dict:
            dim1_parc_match = True
            mza_candidata_dim1 = parcelas_dict[dc_formateada]['mza_nom']
        else:
            # Probar si los primeros 18 dígitos corresponden a una manzana
            mza_dc_prefix = dc_formateada[:18]
            if mza_dc_prefix in mzas_dict:
                dim1_mza_match = True
                mza_candidata_dim1 = mza_dc_prefix
                
        # 2. Dimensión 2: Cuaterna Catastral
        cuat_parc, cuat_mza = construir_cuaterna_str(r['DISTRITO_CATASTRAL'], r['ZONA_CATASTRAL'], r['MANZANA_CATASTRAL'], r['LOTE_CATASTRAL'])
        dim2_parc_match = (cuat_parc in parcelas_dict) if cuat_parc else False
        dim2_mza_match = (cuat_mza in mzas_dict) if cuat_mza else False
        mza_candidata_dim2 = cuat_mza if dim2_mza_match else ""
        
        # Manzana de referencia primaria
        mza_referencia = mza_candidata_dim1 or mza_candidata_dim2
        
        # 3. Dimensión 3: Dirección Postal
        dim3_calle_match = False
        if mza_referencia and mza_referencia in mzas_dict:
            if calle_sum_norm:
                # Comprobar coincidencia exacta o substring
                for c_perim in mzas_dict[mza_referencia]['calles_norm']:
                    if calle_sum_norm in c_perim or c_perim in calle_sum_norm:
                        dim3_calle_match = True
                        break
                        
        # 4. Dimensión 4: Geolocalización Espacial (Point in Polygon)
        dim4_geo_match = False
        mza_geoloc = ""
        if pd.notna(lat) and pd.notna(lon) and -32.0 < lat < -30.5 and -65.0 < lon < -63.5:
            pt = Point(lon, lat)
            # Consultar STRtree
            candidate_indices = tree.query(pt)
            for cand_idx in candidate_indices:
                if mzas_geoms[cand_idx].contains(pt) or mzas_geoms[cand_idx].distance(pt) < 0.00015: # ~15 metros
                    dim4_geo_match = True
                    mza_geoloc = mzas_keys[cand_idx]
                    break
                    
        # Conteo de dimensiones validadas
        dims_validadas = sum([
            dim1_parc_match or dim1_mza_match,
            dim2_parc_match or dim2_mza_match,
            dim3_calle_match,
            dim4_geo_match
        ])
        
        # Determinación de Categoría y Nivel de Certeza según directivas del usuario
        nivel_certeza = ""
        manzana_asignada = ""
        parcela_asignada = ""
        requiere_vecinos = False
        asignacion_parcial_mza = False
        
        if dim1_parc_match:
            nivel_certeza = "NIVEL_1A_ALTA_DC_EXACTA"
            manzana_asignada = mza_candidata_dim1
            parcela_asignada = dc_formateada
            c_alta_dc += 1
        elif dims_validadas >= 3:
            nivel_certeza = "NIVEL_1B_ALTA_MULTIVARIADA"
            manzana_asignada = mza_referencia or mza_geoloc
            parcela_asignada = cuat_parc if dim2_parc_match else ""
            c_alta_multi += 1
        elif dims_validadas == 2:
            nivel_certeza = "NIVEL_2_CERTEZA_MEDIA_VECINOS"
            manzana_asignada = mza_referencia or mza_geoloc
            requiere_vecinos = True
            c_media_vecinos += 1
        elif dim1_mza_match or dim2_mza_match or dim4_geo_match:
            nivel_certeza = "NIVEL_3_ASIGNACION_PARCIAL_MANZANA"
            manzana_asignada = mza_candidata_dim1 or mza_candidata_dim2 or mza_geoloc
            asignacion_parcial_mza = True
            c_parcial_manzana += 1
        else:
            nivel_certeza = "NIVEL_4_SIN_CONVERGENCIA"
            c_sin_match += 1
            
        resultados.append({
            'suministro': sum_id,
            'distrito': r['DISTRITO'],
            'grupo_lectura': r['GRUPO_LECTURA'],
            'ruta_lectura': r['RUTA_LECTURA'],
            'orden_lectura': r['ORDEN_LECTURA'],
            'nivel_certeza': nivel_certeza,
            'manzana_asignada': manzana_asignada,
            'parcela_asignada': parcela_asignada,
            'requiere_vecinos_sprint3': requiere_vecinos,
            'asignacion_parcial_mza': asignacion_parcial_mza,
            'dim1_dc_match': dim1_parc_match or dim1_mza_match,
            'dim2_cuaterna_match': dim2_parc_match or dim2_mza_match,
            'dim3_calle_match': dim3_calle_match,
            'dim4_geo_match': dim4_geo_match,
            'total_dims_validas': dims_validadas
        })
        
        if (idx + 1) % 15000 == 0 or (idx + 1) == len(df_sum):
            print(f"   ... Procesados {idx+1:,} / {len(df_sum):,} suministros ({((idx+1)/len(df_sum))*100:.1f}%)")
            
    df_res = pd.DataFrame(resultados)
    dt_conv = time.time() - t_conv_start
    print(f"\n⏱️ Tiempo de evaluación convergente: {dt_conv:.2f} s ({len(df_sum)/dt_conv:,.0f} sum/s)")
    
    # Guardar resultados
    out_parquet = os.path.join(data_dir, "convergencia_suministros_circ01.parquet")
    df_res.to_parquet(out_parquet, index=False)
    print(f"💾 Resultados de convergencia guardados en: {out_parquet} ({os.path.getsize(out_parquet)/1024/1024:.2f} MB)")
    
    # Métricas consolidadas
    total_eval = len(df_res)
    total_alta = c_alta_dc + c_alta_multi
    
    print("\n" + "=" * 80)
    print(" 📊 BALANCE DE CONVERGENCIA MULTIVARIADA (SPRINT 2)")
    print("=" * 80)
    print(f"Total Suministros Evaluados:               {total_eval:,} (100.0%)")
    print(f"  🟢 ALTA CERTEZA TOTAL (Nivel 1):         {total_alta:,} ({total_alta/total_eval*100:.2f}%)")
    print(f"     • Nivel 1A (Coincidencia DC Exacta):  {c_alta_dc:,} ({c_alta_dc/total_eval*100:.2f}%)")
    print(f"     • Nivel 1B (Multi-criterio >= 3):     {c_alta_multi:,} ({c_alta_multi/total_eval*100:.2f}%)")
    print(f"  🟡 CERTEZA MEDIA (Nivel 2 -> Sprint 3):   {c_media_vecinos:,} ({c_media_vecinos/total_eval*100:.2f}%)")
    print(f"  🟠 ASIGNACIÓN PARCIAL MANZANA (Nivel 3): {c_parcial_manzana:,} ({c_parcial_manzana/total_eval*100:.2f}%)")
    print(f"  🔴 SIN CONVERGENCIA / CASOS BORDE:       {c_sin_match:,} ({c_sin_match/total_eval*100:.2f}%)")
    print("=" * 80)

if __name__ == "__main__":
    ejecutar_motor_convergencia()
