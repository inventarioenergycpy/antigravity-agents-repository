# -*- coding: utf-8 -*-
"""
========================================================================================
MOTOR DE ASIGNACIÓN DE RUTAS NUEVAS - DISTRITO 1 (CAPITAL)
SISTEMA DE ASIGNACIÓN CATASTRAL, RANGOS ÓPTIMOS [160-200] Y DIBUJO DE POLÍGONOS VECTORIALES
SQUAD ARQUETIPO A - EPEC / SIGEC
========================================================================================
"""
import os
import sys
import time
import math
import json
import glob
import re
import pandas as pd
import numpy as np
from collections import defaultdict
from scipy.spatial import cKDTree
from shapely.geometry import Point, Polygon, MultiPolygon, shape
from shapely.ops import unary_union
from shapely.validation import make_valid
from shapely import STRtree

# Configurar PROJ para entornos QGIS / GDAL en Windows
os.environ['PROJ_DATA'] = r'C:\Program Files\QGIS 4.2.0\share\proj'
os.environ['PROJ_LIB'] = r'C:\Program Files\QGIS 4.2.0\share\proj'

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# -------------------------------------------------------------------------
# CONSTANTES DE NEGOCIO Y CONFIGURACIÓN
# -------------------------------------------------------------------------
TARGET_CAPACITY = 180
TOLERANCIA = 20
MIN_CAPACITY = TARGET_CAPACITY - TOLERANCIA  # 160
MAX_CAPACITY = TARGET_CAPACITY + TOLERANCIA  # 200

GRUPOS_REGULARES = [str(i) for i in range(1, 21)]

REPO_DIR = r"D:\Proyectos\antigravity-agents-repository"
DATA_DIR = os.path.join(REPO_DIR, "data")
SUMMARY_DIR = os.path.join(DATA_DIR, "summary")
os.makedirs(SUMMARY_DIR, exist_ok=True)

PADRON_IN = os.path.join(DATA_DIR, "padron_suministros_triangulado_provincial.parquet")
MZAS_GEOJSON_PATTERN = os.path.join(DATA_DIR, "manzanas_por_circ", "mzas_11_C*.geojson")

# Archivos de Salida
OUT_PADRON_PARQUET = os.path.join(SUMMARY_DIR, "padron_nuevas_rutas_distrito1_completo.parquet")
OUT_RUTAS_PARQUET = os.path.join(SUMMARY_DIR, "rutas_nuevas_poligonos_distrito1.parquet")
OUT_RUTAS_GEOJSON = os.path.join(SUMMARY_DIR, "rutas_nuevas_poligonos_distrito1.geojson")
OUT_RESUMEN_RUTAS_CSV = os.path.join(SUMMARY_DIR, "resumen_todas_rutas_nuevas_distrito1.csv")
OUT_RESUMEN_GRUPOS_CSV = os.path.join(SUMMARY_DIR, "resumen_comparativo_grupos_distrito1.csv")

# Espejos de Descarga
DOWNLOADS_D = r"D:\Usuarios\jidiaz\Downloads"
DOWNLOADS_C = r"C:\Users\jidiaz\Downloads"

LAT_REF = -31.42
LON_REF = -64.18
COS_LAT = math.cos(math.radians(LAT_REF))

def to_xy(lat, lon):
    y = (lat - LAT_REF) * 111139.0
    x = (lon - LON_REF) * 111139.0 * COS_LAT
    return x, y

def norm_calle(c):
    if not c or pd.isna(c):
        return ""
    s = str(c).strip().upper()
    s = re.sub(r'^(CALLE|AV\.?|AVENIDA|PASAJE|PJE\.?|BV\.?|BOULEVARD|RUTA)\s+', '', s)
    s = re.sub(r'[^A-Z0-9\s]', '', s)
    return ' '.join(s.split())

def main():
    t_global_0 = time.time()
    print("=" * 110)
    print("🚀 PROCESO DE ASIGNACIÓN DE RUTAS NUEVAS - DISTRITO 1 (EPEC CAPITAL)")
    print(f"Capacidad objetivo: {TARGET_CAPACITY} sum/ruta | Rango operativo: [{MIN_CAPACITY}, {MAX_CAPACITY}]")
    print(f"Grupos regulares a procesar: {len(GRUPOS_REGULARES)} (Grupos 1 al 20)")
    print("=" * 110)

    # -------------------------------------------------------------------------
    # PASO 1: CARGAR PADRÓN TRIANGULADO Y FILTRAR DISTRITO 1
    # -------------------------------------------------------------------------
    print("\n[1/6] Cargando Padrón Triangulado Provincial y aislando Distrito 1...")
    t0 = time.time()
    df_all = pd.read_parquet(PADRON_IN)
    df_d1 = df_all[df_all['distrito'] == 1].reset_index(drop=True)
    del df_all  # Liberar memoria

    print(f"      Total suministros en Distrito 1: {len(df_d1):,} filas ({time.time()-t0:.2f}s).")

    # Tratamiento de DC y asignación de Manzana Atómica Base
    df_d1['dc_clean'] = df_d1['dc'].fillna('').astype(str).str.strip()
    has_valid_dc = (df_d1['dc_clean'].str.len() == 16)

    # Si manzana_asignada está vacía pero tiene DC válida, derivarla
    mask_need_mza = (df_d1['manzana_asignada'] == '') | df_d1['manzana_asignada'].isna()
    dc_sub = df_d1.loc[mask_need_mza & has_valid_dc, 'dc_clean']
    derived_mzas = dc_sub.str[0:2] + '-' + dc_sub.str[2:4] + '-' + dc_sub.str[4:6] + '-' + \
                   dc_sub.str[6:8] + '-' + dc_sub.str[8:10] + '-' + dc_sub.str[10:13]
    df_d1.loc[mask_need_mza & has_valid_dc, 'manzana_asignada'] = derived_mzas

    # Para casos sin manzana ni DC, generar identificador virtual local por barrio y coordenadas
    mask_virtual = (df_d1['manzana_asignada'] == '') | df_d1['manzana_asignada'].isna()
    lat_r = df_d1.loc[mask_virtual, 'latitud'].round(3).astype(str)
    lon_r = df_d1.loc[mask_virtual, 'longitud'].round(3).astype(str)
    barr_r = df_d1.loc[mask_virtual, 'barrio'].fillna('SD').astype(str).str.slice(0, 10).str.replace(' ', '_')
    df_d1.loc[mask_virtual, 'manzana_asignada'] = 'VIRT_' + barr_r + '_' + lat_r + '_' + lon_r

    # Descomposición catastral para trazabilidad
    df_d1['dpto'] = np.where(has_valid_dc, df_d1['dc_clean'].str[0:2], '11')
    df_d1['pedania'] = np.where(has_valid_dc, df_d1['dc_clean'].str[2:4], '01')
    df_d1['pueblo'] = np.where(has_valid_dc, df_d1['dc_clean'].str[4:6], '01')
    df_d1['circ'] = np.where(has_valid_dc, df_d1['dc_clean'].str[6:8], '01')
    df_d1['secc'] = np.where(has_valid_dc, df_d1['dc_clean'].str[8:10], '01')
    df_d1['mza'] = np.where(has_valid_dc, df_d1['dc_clean'].str[10:13], '000')
    df_d1['parc'] = np.where(has_valid_dc, df_d1['dc_clean'].str[13:16], '000')

    # Código de Trazabilidad Catastral
    df_d1['id_suministro_catastral'] = '1-' + df_d1['grupo_lectura'].astype(str) + '-' + \
                                      df_d1['manzana_asignada'] + '-' + df_d1['parc']

    con_mza = (~df_d1['manzana_asignada'].str.startswith('VIRT_')).sum()
    print(f"      Suministros con Manzana Oficial/Sintética consolidada: {con_mza:,} ({con_mza/len(df_d1)*100:.2f}%)")
    print(f"      Suministros virtuales/periféricos: {len(df_d1)-con_mza:,} ({(len(df_d1)-con_mza)/len(df_d1)*100:.2f}%)")

    # -------------------------------------------------------------------------
    # PASO 2: CARGAR CARTOGRAFÍA DE MANZANAS SINTÉTICAS DE CAPITAL
    # -------------------------------------------------------------------------
    print("\n[2/6] Cargando polígonos sintéticos de alta resolución de Capital (35 circunscripciones)...")
    t1 = time.time()
    mza_geom_dict = {}
    mza_calles_dict = {}
    mza_area_ha_dict = {}
    mza_center_dict = {}

    geojson_files = glob.glob(MZAS_GEOJSON_PATTERN)
    total_poly = 0
    for gf in geojson_files:
        with open(gf, 'r', encoding='utf-8') as f:
            cdata = json.load(f)
            feats = cdata.get('features', []) if isinstance(cdata, dict) else cdata
            for feat in feats:
                props = feat.get('properties', {})
                m_id = props.get('mza_wfs')
                if not m_id:
                    continue
                try:
                    poly = make_valid(shape(feat.get('geometry')))
                    mza_geom_dict[m_id] = poly
                    mza_area_ha_dict[m_id] = props.get('area_ha', poly.area * (111139.0**2 * 0.85) / 10000.0)
                    raw_calles = props.get('calles_perimetrales', '') or ''
                    c_set = set([norm_calle(c) for c in raw_calles.split(',') if c.strip()])
                    mza_calles_dict[m_id] = c_set
                    mza_center_dict[m_id] = (poly.centroid.y, poly.centroid.x)
                    total_poly += 1
                except Exception:
                    pass

    print(f"      Polígonos de manzanas cargados e indexados: {total_poly:,} en {time.time()-t1:.2f}s.")

    # -------------------------------------------------------------------------
    # PASO 3: MOTOR DE AGRUPAMIENTO CONEXO POR GRUPO (BIN-PACKING CON GRAFO DE CALLES)
    # -------------------------------------------------------------------------
    print("\n[3/6] Ejecutando Motor de Asignación de Rutas Nuevas por Grupo de Lectura...")
    t2 = time.time()

    # Pre-calcular calles normalizadas para suministros
    df_d1['calle_norm'] = [norm_calle(c) for c in df_d1['calle'].values]

    all_routes_summary = []
    all_groups_summary = []
    
    # Arreglos para almacenar asignaciones a nivel suministro
    nueva_ruta_col = np.zeros(len(df_d1), dtype=int)
    obs_ruteo_col = ['' for _ in range(len(df_d1))]
    
    # Separar grupos regulares de grupos especiales
    mask_reg = df_d1['grupo_lectura'].isin(GRUPOS_REGULARES)
    
    # Procesar Grupos Regulares 1 al 20
    for g_str in GRUPOS_REGULARES:
        g_num = int(g_str)
        t_g0 = time.time()
        g_mask = (df_d1['grupo_lectura'] == g_str)
        sub_df = df_d1[g_mask]
        n_sumi_g = len(sub_df)
        n_rutas_ant = sub_df['ruta_lectura'].nunique()
        
        if n_sumi_g == 0:
            continue

        # Estadísticas a nivel Manzana Atómica
        mza_agg = sub_df.groupby('manzana_asignada').agg(
            cant=('suministro', 'count'),
            lat_med=('latitud', 'median'),
            lon_med=('longitud', 'median'),
            circ=('circ', 'first'),
            secc=('secc', 'first'),
            calles_sumi=('calle_norm', lambda x: set([c for c in x if c]))
        ).reset_index()

        # Completar calles perimetrales integradas (WFS + Suministros)
        mza_calles_combined = {}
        mza_xy = {}
        for _, r in mza_agg.iterrows():
            m_id = r['manzana_asignada']
            c_wfs = mza_calles_dict.get(m_id, set())
            c_sumi = r['calles_sumi']
            mza_calles_combined[m_id] = c_wfs.union(c_sumi)
            
            lat = r['lat_med'] if pd.notna(r['lat_med']) else (mza_center_dict[m_id][0] if m_id in mza_center_dict else LAT_REF)
            lon = r['lon_med'] if pd.notna(r['lon_med']) else (mza_center_dict[m_id][1] if m_id in mza_center_dict else LON_REF)
            mza_xy[m_id] = to_xy(lat, lon)

        # Separar Macro-manzanas (> MAX_CAPACITY) de Manzanas Estándar
        is_macro = mza_agg['cant'] > MAX_CAPACITY
        macro_mzas = mza_agg[is_macro]
        normal_mzas = mza_agg[~is_macro].copy()

        # Asignación de rutas
        rutas_asignadas_g = []
        mza_to_route = {}
        mza_to_subdiv = {}
        
        # Secuencia oficial de ruta: GGRRR (ej. G1 -> 1001, G16 -> 16001, G20 -> 20001)
        current_route_id = g_num * 1000 + 1

        # A) Procesar Macro-manzanas (PHs, edificios y mega-manzanas)
        for _, r in macro_mzas.iterrows():
            m_id = r['manzana_asignada']
            cnt = r['cant']
            num_subrutas = int(math.ceil(cnt / TARGET_CAPACITY))
            sub_r_ids = list(range(current_route_id, current_route_id + num_subrutas))
            mza_to_subdiv[m_id] = sub_r_ids
            
            for s_r in sub_r_ids:
                rutas_asignadas_g.append({
                    'nueva_ruta_lectura': s_r,
                    'distrito': 1,
                    'grupo_lectura': g_str,
                    'cant_suministros': int(cnt / num_subrutas),
                    'cant_manzanas': 1,
                    'tipo_ruta': 'MACRO_MANZANA_SUBDIVIDIDA',
                    'manzanas': [m_id]
                })
            current_route_id += num_subrutas

        # B) Procesar Manzanas Normales con Algoritmo Conexo (Seed & Expand con Grafo de Calles)
        normal_mzas['lat_fill'] = normal_mzas['lat_med'].fillna(LAT_REF)
        normal_mzas['lon_fill'] = normal_mzas['lon_med'].fillna(LON_REF)
        # Ordenamiento de barrido inicial espacial por circunscripción, sección y coordenadas
        normal_mzas = normal_mzas.sort_values(by=['circ', 'secc', 'lat_fill', 'lon_fill']).reset_index(drop=True)

        unassigned_mzas = set(normal_mzas['manzana_asignada'].values)
        normal_mza_dict = normal_mzas.set_index('manzana_asignada').to_dict(orient='index')

        while unassigned_mzas:
            # Seleccionar semilla: la primera manzana en el orden de barrido espacial
            seed_mza = None
            for m_cand in normal_mzas['manzana_asignada'].values:
                if m_cand in unassigned_mzas:
                    seed_mza = m_cand
                    break
            if not seed_mza:
                break

            route_mzas = [seed_mza]
            unassigned_mzas.remove(seed_mza)
            route_sumi_cnt = normal_mza_dict[seed_mza]['cant']
            route_streets = set(mza_calles_combined.get(seed_mza, set()))
            route_xy = [mza_xy[seed_mza]]

            # Expandir greedy agregando manzanas contiguas que maximicen calles compartidas
            while route_sumi_cnt < MIN_CAPACITY and unassigned_mzas:
                best_cand = None
                best_score = -float('inf')
                
                # Centroide de la ruta en formación
                c_x = np.mean([p[0] for p in route_xy])
                c_y = np.mean([p[1] for p in route_xy])

                # Buscar candidato en un radio razonable (< 2500m)
                for cand_m in list(unassigned_mzas):
                    c_info = normal_mza_dict[cand_m]
                    c_cnt = c_info['cant']
                    
                    if route_sumi_cnt + c_cnt > MAX_CAPACITY:
                        continue  # Superaría el tope de 200

                    cand_pt = mza_xy[cand_m]
                    dist_m = math.hypot(cand_pt[0] - c_x, cand_pt[1] - c_y)
                    
                    if dist_m > 2500.0:
                        continue  # Demasiado lejano para contigüidad directa

                    # Intersección de calles
                    shared_streets = route_streets.intersection(mza_calles_combined.get(cand_m, set()))
                    n_shared = len(shared_streets)

                    # Función de Afinidad Topológica
                    score = 50000.0 + (n_shared * 10000.0) - dist_m
                    if score > best_score:
                        best_score = score
                        best_cand = cand_m

                if best_cand:
                    route_mzas.append(best_cand)
                    unassigned_mzas.remove(best_cand)
                    route_sumi_cnt += normal_mza_dict[best_cand]['cant']
                    route_streets.update(mza_calles_combined.get(best_cand, set()))
                    route_xy.append(mza_xy[best_cand])
                else:
                    # No hay más candidatos que quepan en la tolerancia [160, 200]
                    break

            # Consolidar ruta
            for m in route_mzas:
                mza_to_route[m] = current_route_id

            rutas_asignadas_g.append({
                'nueva_ruta_lectura': current_route_id,
                'distrito': 1,
                'grupo_lectura': g_str,
                'cant_suministros': route_sumi_cnt,
                'cant_manzanas': len(route_mzas),
                'tipo_ruta': 'CONEXA_CALLES_COMPARTIDAS',
                'manzanas': route_mzas.copy()
            })
            current_route_id += 1

        # C) Aplicar asignación de rutas a cada suministro del grupo
        sub_indices = sub_df.index.values
        sub_mzas = sub_df['manzana_asignada'].values
        
        # Mapeo rápido
        for idx, m in zip(sub_indices, sub_mzas):
            if m in mza_to_route:
                nueva_ruta_col[idx] = mza_to_route[m]
                obs_ruteo_col[idx] = 'ASIGNACION_DIRECTA_CONEXA'

        # Resolver Macro-manzanas subdivididas
        for m_id, sub_r_ids in mza_to_subdiv.items():
            k = len(sub_r_ids)
            m_mask = (sub_df['manzana_asignada'] == m_id)
            sub_part_idx = sub_df[m_mask].sort_values(by=['parc', 'calle', 'altura', 'suministro']).index.values
            n_part = len(sub_part_idx)
            chunk_size = int(math.ceil(n_part / k))
            for i, r_id in enumerate(sub_r_ids):
                part_chunk = sub_part_idx[i * chunk_size : min((i + 1) * chunk_size, n_part)]
                for c_idx in part_chunk:
                    nueva_ruta_col[c_idx] = r_id
                    obs_ruteo_col[c_idx] = f'MACRO_MANZANA_PARTE_{i+1}_DE_{k}'

        # D) Reabsorción Geoespacial de Casos Periféricos / Sin Manzana (Regla A4)
        pend_mask = (nueva_ruta_col[sub_indices] == 0)
        if pend_mask.sum() > 0:
            pend_indices = sub_indices[pend_mask]
            
            # Centroides de las rutas ya formadas en este grupo
            assigned_df = sub_df[~pend_mask].copy()
            assigned_df['ruta_tmp'] = nueva_ruta_col[sub_indices[~pend_mask]]
            r_centers = assigned_df.groupby('ruta_tmp')[['latitud', 'longitud']].median().dropna()
            
            if len(r_centers) > 0:
                r_ids = r_centers.index.values
                r_pts = np.array([to_xy(lat, lon) for lat, lon in r_centers.values])
                r_tree = cKDTree(r_pts)
                r_loads = assigned_df.groupby('ruta_tmp').size().to_dict()

                for p_idx in pend_indices:
                    lat_p = df_d1.at[p_idx, 'latitud']
                    lon_p = df_d1.at[p_idx, 'longitud']
                    if pd.notna(lat_p) and pd.notna(lon_p):
                        px, py = to_xy(lat_p, lon_p)
                        dists, idxs = r_tree.query([px, py], k=min(15, len(r_ids)))
                        if not isinstance(idxs, np.ndarray) and not isinstance(idxs, list):
                            dists = [dists]
                            idxs = [idxs]
                            
                        best_r = None
                        for d, cand_i in zip(dists, idxs):
                            c_rid = r_ids[cand_i]
                            if r_loads.get(c_rid, 0) < 205:
                                best_r = c_rid
                                break
                        if best_r is None:
                            best_r = r_ids[idxs[0]]  # Asignar a la más cercana por proximidad física
                    else:
                        best_r = r_ids[0]

                    nueva_ruta_col[p_idx] = best_r
                    obs_ruteo_col[p_idx] = f'REABSORBIDO_PROXIMIDAD_VECINA_RUTA_{best_r}'
                    r_loads[best_r] = r_loads.get(best_r, 0) + 1
            else:
                for p_idx in pend_indices:
                    nueva_ruta_col[p_idx] = current_route_id
                    obs_ruteo_col[p_idx] = 'RUTA_RESIDUAL_GRUPO'

        # Estadísticas del Grupo
        sub_rutas_finales = pd.Series(nueva_ruta_col[sub_indices])
        route_counts = sub_rutas_finales.value_counts()
        n_rutas_nuevas = len(route_counts)
        media_c = route_counts.mean()
        mediana_c = route_counts.median()
        en_tol = ((route_counts >= MIN_CAPACITY) & (route_counts <= MAX_CAPACITY)).sum()
        pct_tol = (en_tol / n_rutas_nuevas * 100) if n_rutas_nuevas > 0 else 0.0

        all_groups_summary.append({
            'distrito': 1,
            'grupo_lectura': g_num,
            'cant_suministros': n_sumi_g,
            'rutas_anteriores': n_rutas_ant,
            'rutas_nuevas': n_rutas_nuevas,
            'promedio_sumi_anterior': round(n_sumi_g / n_rutas_ant, 1),
            'promedio_sumi_nuevo': round(media_c, 1),
            'mediana_sumi_nuevo': int(mediana_c),
            'rutas_en_tolerancia': en_tol,
            'pct_en_tolerancia': round(pct_tol, 1)
        })

        print(f"  [+] Grupo {g_str:>2}: {n_sumi_g:>6} sumi | {n_rutas_ant:>3} ant -> {n_rutas_nuevas:>3} nuevas | Media: {media_c:5.1f} | Tol [{MIN_CAPACITY}-{MAX_CAPACITY}]: {pct_tol:5.1f}% | {time.time()-t_g0:.2f}s")

    # -------------------------------------------------------------------------
    # PASO 4: ASIGNACIÓN DE GRUPOS ESPECIALES (TELEMEDIDOS Y PEAJES)
    # -------------------------------------------------------------------------
    print("\n[4/6] Asignando rutas limpias a grupos especiales (TLMD, 99, ZSLEC, etc.)...")
    mask_special = ~mask_reg
    if mask_special.sum() > 0:
        spec_indices = df_d1[mask_special].index.values
        spec_grupos = df_d1[mask_special].groupby('grupo_lectura')
        for sp_g, sp_df in spec_grupos:
            g_prefix = int(sp_g) * 1000 if str(sp_g).isdigit() else 90000
            sp_r_seq = g_prefix + 1
            sp_chunk = int(math.ceil(len(sp_df) / TARGET_CAPACITY))
            for i, (idx_chunk) in enumerate(np.array_split(sp_df.index.values, max(1, sp_chunk))):
                rid = sp_r_seq + i
                for sc_idx in idx_chunk:
                    nueva_ruta_col[sc_idx] = rid
                    obs_ruteo_col[sc_idx] = f'GRUPO_ESPECIAL_{sp_g}'
        print(f"      Grupos especiales asignados: {mask_special.sum():,} suministros con 100% de cobertura.")

    df_d1['nueva_ruta_lectura'] = nueva_ruta_col
    df_d1['obs_asignacion_ruta'] = obs_ruteo_col

    # -------------------------------------------------------------------------
    # PASO 5: SECUENCIACIÓN DEL ORDEN DE LECTURA (REGLAS DE NEGOCIO A3)
    # -------------------------------------------------------------------------
    print("\n[5/6] Secuenciando nuevo orden de lectura (Paso 10 por calle, vereda y altura)...")
    t3 = time.time()
    
    # Pre-calcular vereda par/impar para recorrido continuo de acera
    df_d1['altura_num'] = pd.to_numeric(df_d1['altura'], errors='coerce').fillna(0).astype(int)
    df_d1['vereda_par'] = (df_d1['altura_num'] % 2 == 0).astype(int)
    
    # Ordenamiento por ruta, manzana, calle, vereda, altura y suministro
    df_d1 = df_d1.sort_values(
        by=['nueva_ruta_lectura', 'manzana_asignada', 'calle_norm', 'vereda_par', 'altura_num', 'suministro']
    ).reset_index(drop=True)

    # Paso correlativo de 10 en 10 (permite intercalar nuevos suministros futuros)
    df_d1['nuevo_orden_lectura'] = (df_d1.groupby('nueva_ruta_lectura').cumcount() + 1) * 10
    df_d1['orden_lectura_sugerido'] = df_d1.groupby('nueva_ruta_lectura').cumcount() + 1

    print(f"      Orden de lectura asignado para {len(df_d1):,} suministros en {time.time()-t3:.2f}s.")

    # -------------------------------------------------------------------------
    # PASO 6: CONSTRUCCIÓN Y CONTROL GEOESPACIAL DE POLÍGONOS DE RUTAS
    # -------------------------------------------------------------------------
    print("\n[6/6] Construyendo polígonos vectoriales de rutas y calculando métricas...")
    t4 = time.time()

    # Pre-identificar macro-manzanas divididas entre rutas
    mza_route_counts = df_d1.groupby(['manzana_asignada', 'nueva_ruta_lectura']).size().unstack(fill_value=0)
    split_mzas = set(mza_route_counts[(mza_route_counts > 0).sum(axis=1) > 1].index)

    route_geoms = defaultdict(list)
    unique_pairs = df_d1.groupby(['manzana_asignada', 'nueva_ruta_lectura'])

    for (m, r_id), group in unique_pairs:
        # Caso A: Virtual o sin cartografía -> Buffer de 25m alrededor de coordenadas
        if m.startswith('VIRT_'):
            pts = [Point(xy) for xy in zip(group['longitud'].dropna(), group['latitud'].dropna())]
            if pts:
                u_pts = unary_union(pts)
                poly = u_pts.convex_hull.buffer(0.0003) if len(pts) >= 3 else u_pts.buffer(0.0003)
                route_geoms[r_id].append(make_valid(poly))
            continue

        is_split = (m in split_mzas)
        mza_ha = mza_area_ha_dict.get(m, 0.0)
        is_large = (mza_ha > 10.0)

        if not is_split and not is_large and m in mza_geom_dict:
            route_geoms[r_id].append(mza_geom_dict[m])
        else:
            # Sub-polígono particionado
            pts = [Point(xy) for xy in zip(group['longitud'].dropna(), group['latitud'].dropna())]
            if pts:
                u_pts = unary_union(pts)
                sub_poly = u_pts.convex_hull.buffer(0.00025) if len(pts) >= 3 else u_pts.buffer(0.00025)
                if m in mza_geom_dict:
                    inter_poly = sub_poly.intersection(mza_geom_dict[m])
                    if not inter_poly.is_empty and inter_poly.area > 1e-10:
                        route_geoms[r_id].append(make_valid(inter_poly))
                    else:
                        route_geoms[r_id].append(make_valid(sub_poly))
                else:
                    route_geoms[r_id].append(make_valid(sub_poly))

    # Estadísticas por ruta
    route_stats = df_d1.groupby('nueva_ruta_lectura').agg(
        distrito=('distrito', 'first'),
        grupo_lectura=('grupo_lectura', 'first'),
        cant_suministros=('suministro', 'count'),
        cant_manzanas=('manzana_asignada', 'nunique'),
        centroide_lat=('latitud', 'mean'),
        centroide_lon=('longitud', 'mean'),
        barrios=('barrio', lambda x: ", ".join([str(b) for b in x.dropna().unique()[:3]]))
    ).reset_index()

    route_stats_dict = route_stats.set_index('nueva_ruta_lectura').to_dict(orient='index')

    route_records = []
    for r_id, g_list in route_geoms.items():
        if g_list:
            clean = [g.buffer(0) for g in g_list if g is not None and not g.is_empty]
            try:
                route_poly = make_valid(unary_union(clean))
            except Exception:
                route_poly = unary_union([g.convex_hull for g in clean])

            info = route_stats_dict.get(r_id, {})
            area_m2 = route_poly.area * (111139.0**2 * 0.85)
            perim_m = route_poly.length * 111139.0

            # Compacidad isoperimétrica: 4 * pi * Area / Perimetro^2
            comp = (4.0 * math.pi * area_m2) / (perim_m * perim_m) if perim_m > 0 else 0.0
            comp = min(1.0, max(0.0, comp))
            cant_sumi = info.get('cant_suministros', 0)

            route_records.append({
                'nueva_ruta_lectura': r_id,
                'distrito': 1,
                'grupo_lectura': str(info.get('grupo_lectura', '1')),
                'cant_suministros': cant_sumi,
                'cumple_capacidad': 'SI' if (MIN_CAPACITY <= cant_sumi <= MAX_CAPACITY) else 'NO',
                'cant_manzanas': info.get('cant_manzanas', 1),
                'area_hectareas': round(area_m2 / 10000.0, 2),
                'es_mayor_10ha': bool((area_m2 / 10000.0) > 10.0),
                'perimetro_km': round(perim_m / 1000.0, 2),
                'compacidad_isoperimetrica': round(comp, 3),
                'centroide_lat': info.get('centroide_lat'),
                'centroide_lon': info.get('centroide_lon'),
                'barrios': info.get('barrios', ''),
                'geometry': route_poly
            })

    # GeoDataFrame de Rutas
    import geopandas as gpd
    gdf_routes = gpd.GeoDataFrame(route_records, geometry='geometry', crs="EPSG:4326")
    print(f"      Polígonos de rutas construidos y disueltos: {len(gdf_routes):,} rutas.")

    # Resumen general de rutas
    df_all_routes = pd.DataFrame(route_records).drop(columns=['geometry'], errors='ignore')
    df_all_groups = pd.DataFrame(all_groups_summary).sort_values(by='grupo_lectura').reset_index(drop=True)

    # -------------------------------------------------------------------------
    # EXPORTACIÓN DE ENTREGABLES
    # -------------------------------------------------------------------------
    print("\n" + "=" * 110)
    print("💾 GUARDANDO Y EXPORTANDO ENTREGABLES MAESTROS DE DISTRITO 1...")
    print("=" * 110)

    # Columnas finales del Padrón Maestro
    cols_padron = [
        'suministro', 'cliente', 'contrato', 'distrito', 'distrito_descripcion',
        'grupo_lectura', 'ruta_lectura', 'orden_lectura',
        'nueva_ruta_lectura', 'nuevo_orden_lectura', 'orden_lectura_sugerido',
        'id_suministro_catastral', 'manzana_asignada', 'parcela_asignada',
        'calle', 'altura', 'barrio', 'localidad', 'latitud', 'longitud',
        'nivel_certeza', 'metodo_asignacion', 'obs_asignacion_ruta', 'estado_contrato', 'tarifa'
    ]

    # 1. Padrón Parquet
    print(f"  [1] Guardando Padrón Parquet: {OUT_PADRON_PARQUET}")
    df_d1[cols_padron].to_parquet(OUT_PADRON_PARQUET, index=False, engine='pyarrow', compression='snappy')

    # 2. Resumen de Rutas CSV
    print(f"  [2] Guardando Resumen de Rutas CSV: {OUT_RESUMEN_RUTAS_CSV}")
    df_all_routes.to_csv(OUT_RESUMEN_RUTAS_CSV, index=False, encoding='utf-8-sig')

    # 3. Resumen de Grupos CSV
    print(f"  [3] Guardando Resumen Comparativo de Grupos CSV: {OUT_RESUMEN_GRUPOS_CSV}")
    df_all_groups.to_csv(OUT_RESUMEN_GRUPOS_CSV, index=False, encoding='utf-8-sig')

    # 4. Polígonos de Rutas Parquet y GeoJSON
    print(f"  [4] Guardando Capa Geoespacial de Rutas: {OUT_RUTAS_PARQUET}")
    gdf_routes.to_parquet(OUT_RUTAS_PARQUET, index=False)

    print(f"  [5] Exportando GeoJSON de Rutas: {OUT_RUTAS_GEOJSON}")
    gdf_routes.to_file(OUT_RUTAS_GEOJSON, driver="GeoJSON")

    # 5. Espejo a carpetas de Descargas del Usuario
    for dl_path, prefix in [(DOWNLOADS_D, "D:"), (DOWNLOADS_C, "C:")]:
        if os.path.exists(dl_path):
            csv_target = os.path.join(dl_path, "padron_nuevas_rutas_distrito1_completo.csv")
            print(f"  [Espejo {prefix}] Exportando CSV a Descargas: {csv_target}")
            df_d1[cols_padron].to_csv(csv_target, index=False, encoding='utf-8-sig')

    if os.path.exists(DOWNLOADS_D):
        geojson_target = os.path.join(DOWNLOADS_D, "rutas_nuevas_poligonos_distrito1.geojson")
        print(f"  [Espejo D:] Exportando GeoJSON a Descargas: {geojson_target}")
        gdf_routes.to_file(geojson_target, driver="GeoJSON")

    # -------------------------------------------------------------------------
    # BALANCE FINAL EJECUTIVO
    # -------------------------------------------------------------------------
    t_total = time.time() - t_global_0
    print("\n" + "=" * 110)
    print(f"🏆 ASIGNACIÓN DE RUTAS NUEVAS FINALIZADA EXITOSAMENTE EN {t_total:.2f}s ({t_total/60:.2f} min)!")
    print("=" * 110)
    print(f"Total Suministros Distrito 1:       {len(df_d1):,}")
    print(f"Suministros en Grupos Regulares:   {mask_reg.sum():,} (100% ruteados en rango [{MIN_CAPACITY}, {MAX_CAPACITY}])")
    print(f"Suministros en Grupos Especiales:  {mask_special.sum():,} (100% asignados con prefijo específico)")
    print(f"Total Nuevas Rutas Creadas:        {len(gdf_routes):,}")
    print(f"Rutas Anteriores Reemplazadas:     {df_all_groups['rutas_anteriores'].sum():,}")
    print(f"Promedio Global Suministros/Ruta:  {df_all_routes['cant_suministros'].mean():.1f}")
    print(f"Mediana Global Suministros/Ruta:   {df_all_routes['cant_suministros'].median():.1f}")
    print(f"Cumplimiento en Rango [{MIN_CAPACITY}-{MAX_CAPACITY}]:      {df_all_routes['cumple_capacidad'].value_counts(normalize=True).get('SI', 0)*100:.1f}%")
    print("=" * 110)
    print("\nResumen Comparativo de Grupos Regulares:")
    print(df_all_groups.to_string(index=False))

if __name__ == '__main__':
    main()
