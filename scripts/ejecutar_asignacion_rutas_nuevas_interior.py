# -*- coding: utf-8 -*-
"""
========================================================================================
MOTOR DE ASIGNACIÓN DE RUTAS NUEVAS - DISTRITOS DEL INTERIOR CON COBERTURA PARCELARIA
RÍO CUARTO, VILLA MARÍA, CARLOS PAZ, ALTA GRACIA, SAN FRANCISCO, RÍO CEBALLOS, VILLA ALLENDE,
LA CALERA Y SANTIAGO TEMPLE (~362.000 SUMINISTROS / 9 DISTRITOS / RANGOS ÓPTIMOS [160-200])
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

# Distritos del interior con cobertura parcelaria
COVERED_INTERIOR_DISTRITOS = [28, 8, 47, 45, 18, 22, 23, 24, 21]

REPO_DIR = r"D:\Proyectos\antigravity-agents-repository"
DATA_DIR = os.path.join(REPO_DIR, "data")
SUMMARY_DIR = os.path.join(DATA_DIR, "summary")
os.makedirs(SUMMARY_DIR, exist_ok=True)

PADRON_IN = os.path.join(DATA_DIR, "padron_suministros_triangulado_provincial.parquet")
PADRON_D1_IN = os.path.join(SUMMARY_DIR, "padron_nuevas_rutas_distrito1_completo.parquet")
RUTAS_D1_GEOJSON = os.path.join(SUMMARY_DIR, "rutas_nuevas_poligonos_distrito1.geojson")
MZAS_GEOJSON_PATTERN = os.path.join(DATA_DIR, "manzanas_por_circ", "*.geojson")

# Archivos de Salida Interior
OUT_PADRON_INTERIOR_PARQUET = os.path.join(SUMMARY_DIR, "padron_nuevas_rutas_interior_completo.parquet")
OUT_RUTAS_INTERIOR_PARQUET = os.path.join(SUMMARY_DIR, "rutas_nuevas_poligonos_interior.parquet")
OUT_RUTAS_INTERIOR_GEOJSON = os.path.join(SUMMARY_DIR, "rutas_nuevas_poligonos_interior.geojson")
OUT_RESUMEN_RUTAS_CSV = os.path.join(SUMMARY_DIR, "resumen_todas_rutas_nuevas_interior.csv")
OUT_RESUMEN_COMPARATIVO_CSV = os.path.join(SUMMARY_DIR, "resumen_comparativo_interior.csv")

# Archivos Consolidados Provinciales (D1 + Interior)
OUT_PADRON_PROVINCIAL_PARQUET = os.path.join(SUMMARY_DIR, "padron_nuevas_rutas_provincial_consolidado.parquet")
OUT_RESUMEN_RUTAS_PROVINCIAL_CSV = os.path.join(SUMMARY_DIR, "resumen_todas_rutas_nuevas_provincial.csv")
OUT_RUTAS_PROVINCIAL_GEOJSON = os.path.join(SUMMARY_DIR, "rutas_nuevas_poligonos_provincial.geojson")
OUT_RUTAS_PROVINCIAL_PARQUET = os.path.join(SUMMARY_DIR, "rutas_nuevas_poligonos_provincial.parquet")

# Espejos de Descarga
DOWNLOADS_D = r"D:\Usuarios\jidiaz\Downloads"
DOWNLOADS_C = r"C:\Users\jidiaz\Downloads"

def norm_calle(c):
    if not c or pd.isna(c):
        return ""
    s = str(c).strip().upper()
    s = re.sub(r'^(CALLE|AV\.?|AVENIDA|PASAJE|PJE\.?|BV\.?|BOULEVARD|RUTA)\s+', '', s)
    s = re.sub(r'[^A-Z0-9\s]', '', s)
    return ' '.join(s.split())

def main():
    t_global_0 = time.time()
    print("=" * 115)
    print("🚀 MOTOR DE ASIGNACIÓN DE RUTAS NUEVAS - BLOQUE INTERIOR PROVINCIAL (9 DISTRITOS)")
    print(f"Capacidad objetivo: {TARGET_CAPACITY} sum/ruta | Banda de tolerancia: [{MIN_CAPACITY}, {MAX_CAPACITY}]")
    print(f"Distritos a procesar: {COVERED_INTERIOR_DISTRITOS}")
    print("=" * 115)

    # -------------------------------------------------------------------------
    # PASO 1: CARGAR PADRÓN TRIANGULADO Y AISLAR DISTRITOS DEL INTERIOR CUBIERTOS
    # -------------------------------------------------------------------------
    print("\n[1/6] Cargando Padrón Triangulado Provincial y aislando distritos del interior...")
    t0 = time.time()
    df_all = pd.read_parquet(PADRON_IN)
    df_int = df_all[df_all['distrito'].isin(COVERED_INTERIOR_DISTRITOS)].reset_index(drop=True)
    del df_all

    print(f"      Total suministros interior cubierto: {len(df_int):,} filas ({time.time()-t0:.2f}s).")

    # Tratamiento de DC y asignación de Manzana Atómica Base
    df_int['dc_clean'] = df_int['dc'].fillna('').astype(str).str.strip()
    has_valid_dc = (df_int['dc_clean'].str.len() == 16)

    # Derivar manzana para casos con DC válida de 16 dígitos sin manzana_asignada
    mask_need_mza = (df_int['manzana_asignada'] == '') | df_int['manzana_asignada'].isna()
    dc_sub = df_int.loc[mask_need_mza & has_valid_dc, 'dc_clean']
    derived_mzas = dc_sub.str[0:2] + '-' + dc_sub.str[2:4] + '-' + dc_sub.str[4:6] + '-' + \
                   dc_sub.str[6:8] + '-' + dc_sub.str[8:10] + '-' + dc_sub.str[10:13]
    df_int.loc[mask_need_mza & has_valid_dc, 'manzana_asignada'] = derived_mzas

    # Casos virtuales por barrio y coordenadas locales
    mask_virtual = (df_int['manzana_asignada'] == '') | df_int['manzana_asignada'].isna()
    lat_r = df_int.loc[mask_virtual, 'latitud'].round(3).astype(str)
    lon_r = df_int.loc[mask_virtual, 'longitud'].round(3).astype(str)
    barr_r = df_int.loc[mask_virtual, 'barrio'].fillna('SD').astype(str).str.slice(0, 10).str.replace(' ', '_')
    df_int.loc[mask_virtual, 'manzana_asignada'] = 'VIRT_' + barr_r + '_' + lat_r + '_' + lon_r

    # Descomposición catastral estándar
    df_int['dpto'] = np.where(has_valid_dc, df_int['dc_clean'].str[0:2], '00')
    df_int['pedania'] = np.where(has_valid_dc, df_int['dc_clean'].str[2:4], '01')
    df_int['pueblo'] = np.where(has_valid_dc, df_int['dc_clean'].str[4:6], '01')
    df_int['circ'] = np.where(has_valid_dc, df_int['dc_clean'].str[6:8], '01')
    df_int['secc'] = np.where(has_valid_dc, df_int['dc_clean'].str[8:10], '01')
    df_int['mza'] = np.where(has_valid_dc, df_int['dc_clean'].str[10:13], '000')
    df_int['parc'] = np.where(has_valid_dc, df_int['dc_clean'].str[13:16], '000')

    df_int['id_suministro_catastral'] = df_int['distrito'].astype(str) + '-' + \
                                       df_int['grupo_lectura'].astype(str) + '-' + \
                                       df_int['manzana_asignada'] + '-' + df_int['parc']

    con_mza = (~df_int['manzana_asignada'].str.startswith('VIRT_')).sum()
    print(f"      Suministros con Manzana Oficial/Sintética consolidada: {con_mza:,} ({con_mza/len(df_int)*100:.2f}%)")
    print(f"      Suministros virtuales/periféricos: {len(df_int)-con_mza:,} ({(len(df_int)-con_mza)/len(df_int)*100:.2f}%)")

    # -------------------------------------------------------------------------
    # PASO 2: CARGAR POLÍGONOS SINTÉTICOS DE ALTA RESOLUCIÓN (55 PARTICIONES)
    # -------------------------------------------------------------------------
    print("\n[2/6] Cargando polígonos sintéticos de alta resolución provinciales (55 particiones)...")
    t1 = time.time()
    mza_geom_dict = {}
    mza_calles_dict = {}
    mza_area_ha_dict = {}
    mza_center_dict = {}

    geojson_files = glob.glob(MZAS_GEOJSON_PATTERN)
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
                except Exception:
                    pass

    print(f"      Total polígonos indexados: {len(mza_geom_dict):,} en {time.time()-t1:.2f}s.")

    # -------------------------------------------------------------------------
    # PASO 3: MOTOR DE ASIGNACIÓN CONEXO ITERATIVO POR DISTRITO Y GRUPO
    # -------------------------------------------------------------------------
    print("\n[3/6] Ejecutando Motor de Asignación por Distrito y Grupo de Lectura...")
    t2 = time.time()

    df_int['calle_norm'] = [norm_calle(c) for c in df_int['calle'].values]
    nueva_ruta_col = np.zeros(len(df_int), dtype=int)
    obs_ruteo_col = ['' for _ in range(len(df_int))]

    all_routes_summary = []
    all_comparison_summary = []

    for d_id in COVERED_INTERIOR_DISTRITOS:
        t_d0 = time.time()
        d_mask = (df_int['distrito'] == d_id)
        d_indices_all = df_int[d_mask].index.values
        sub_d_df = df_int[d_mask]
        d_desc = sub_d_df['distrito_descripcion'].iloc[0] if len(sub_d_df) > 0 else f'Distrito {d_id}'

        # Centroide de referencia del distrito para proyección euclidiana local sin distorsión
        lat_ref = sub_d_df['latitud'].dropna().median() if sub_d_df['latitud'].dropna().count() > 0 else -31.42
        lon_ref = sub_d_df['longitud'].dropna().median() if sub_d_df['longitud'].dropna().count() > 0 else -64.18
        cos_lat = math.cos(math.radians(lat_ref))

        def d_to_xy(lat, lon):
            y = (lat - lat_ref) * 111139.0
            x = (lon - lon_ref) * 111139.0 * cos_lat
            return x, y

        grupos_d = sorted(
            sub_d_df['grupo_lectura'].dropna().unique().tolist(),
            key=lambda x: int(x) if str(x).isdigit() else 999
        )

        n_sumi_d = len(sub_d_df)
        n_rutas_ant_d = sub_d_df['ruta_lectura'].nunique()
        n_rutas_nuevas_d = 0

        print(f"\n  🏢 DISTRITO {d_id:2d} - {d_desc:18s} ({n_sumi_d:,} sumis | {len(grupos_d)} grupos | {n_rutas_ant_d} rutas ant):")

        for g_str in grupos_d:
            g_mask = d_mask & (df_int['grupo_lectura'] == g_str)
            sub_g_df = df_int[g_mask]
            sub_indices = sub_g_df.index.values
            n_sumi_g = len(sub_g_df)
            n_rutas_ant_g = sub_g_df['ruta_lectura'].nunique()

            if n_sumi_g == 0:
                continue

            # Prefijo de ruta unívoco por grupo y distrito
            if str(g_str).isdigit():
                g_num = int(g_str)
                route_id_seq = g_num * 1000 + 1
            else:
                route_id_seq = 90000 + abs(hash(g_str)) % 8000 + 1

            # Si es un grupo especial con menos de 100 suministros o grupos Z, agrupar de forma directa
            is_special = (not str(g_str).isdigit()) or (g_str in ['0', '99', '22', '60'])

            if is_special:
                sp_chunks = int(math.ceil(n_sumi_g / TARGET_CAPACITY))
                for i, idx_chunk in enumerate(np.array_split(sub_indices, max(1, sp_chunks))):
                    rid = route_id_seq + i
                    for c_idx in idx_chunk:
                        nueva_ruta_col[c_idx] = rid
                        obs_ruteo_col[c_idx] = f'GRUPO_ESPECIAL_{g_str}'
                n_rutas_nuevas_d += max(1, sp_chunks)
                continue

            # Estadísticas por Manzana Atómica en el grupo
            mza_agg = sub_g_df.groupby('manzana_asignada').agg(
                cant=('suministro', 'count'),
                lat_med=('latitud', 'median'),
                lon_med=('longitud', 'median'),
                circ=('circ', 'first'),
                secc=('secc', 'first'),
                calles_sumi=('calle_norm', lambda x: set([c for c in x if c]))
            ).reset_index()

            mza_calles_combined = {}
            mza_xy = {}
            for _, r in mza_agg.iterrows():
                m_id = r['manzana_asignada']
                c_wfs = mza_calles_dict.get(m_id, set())
                c_sumi = r['calles_sumi']
                mza_calles_combined[m_id] = c_wfs.union(c_sumi)
                lat = r['lat_med'] if pd.notna(r['lat_med']) else (mza_center_dict[m_id][0] if m_id in mza_center_dict else lat_ref)
                lon = r['lon_med'] if pd.notna(r['lon_med']) else (mza_center_dict[m_id][1] if m_id in mza_center_dict else lon_ref)
                mza_xy[m_id] = d_to_xy(lat, lon)

            # Separar macro-manzanas (> MAX_CAPACITY) de manzanas estándar
            is_macro = mza_agg['cant'] > MAX_CAPACITY
            macro_mzas = mza_agg[is_macro]
            normal_mzas = mza_agg[~is_macro].copy()

            mza_to_route = {}
            mza_to_subdiv = {}
            current_route_id = route_id_seq

            # A) Macro-manzanas
            for _, r in macro_mzas.iterrows():
                m_id = r['manzana_asignada']
                cnt = r['cant']
                num_subrutas = int(math.ceil(cnt / TARGET_CAPACITY))
                sub_r_ids = list(range(current_route_id, current_route_id + num_subrutas))
                mza_to_subdiv[m_id] = sub_r_ids
                current_route_id += num_subrutas

            # B) Manzanas Normales con Algoritmo Conexo (Seed & Expand con Grafo de Calles)
            normal_mzas['lat_fill'] = normal_mzas['lat_med'].fillna(lat_ref)
            normal_mzas['lon_fill'] = normal_mzas['lon_med'].fillna(lon_ref)
            normal_mzas = normal_mzas.sort_values(by=['circ', 'secc', 'lat_fill', 'lon_fill']).reset_index(drop=True)

            unassigned_mzas = set(normal_mzas['manzana_asignada'].values)
            normal_mza_dict = normal_mzas.set_index('manzana_asignada').to_dict(orient='index')

            while unassigned_mzas:
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

                while route_sumi_cnt < MIN_CAPACITY and unassigned_mzas:
                    best_cand = None
                    best_score = -float('inf')
                    c_x = np.mean([p[0] for p in route_xy])
                    c_y = np.mean([p[1] for p in route_xy])

                    for cand_m in list(unassigned_mzas):
                        c_info = normal_mza_dict[cand_m]
                        c_cnt = c_info['cant']
                        if route_sumi_cnt + c_cnt > MAX_CAPACITY:
                            continue

                        cand_pt = mza_xy[cand_m]
                        dist_m = math.hypot(cand_pt[0] - c_x, cand_pt[1] - c_y)
                        if dist_m > 3000.0:  # Radio flexible en ciudades del interior
                            continue

                        shared_streets = route_streets.intersection(mza_calles_combined.get(cand_m, set()))
                        score = 50000.0 + (len(shared_streets) * 10000.0) - dist_m
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
                        break

                for m in route_mzas:
                    mza_to_route[m] = current_route_id
                current_route_id += 1

            # C) Asignar a suministros
            sub_mzas = sub_g_df['manzana_asignada'].values
            for idx, m in zip(sub_indices, sub_mzas):
                if m in mza_to_route:
                    nueva_ruta_col[idx] = mza_to_route[m]
                    obs_ruteo_col[idx] = 'ASIGNACION_DIRECTA_CONEXA'

            # Subdivisión de macro-manzanas
            for m_id, sub_r_ids in mza_to_subdiv.items():
                k = len(sub_r_ids)
                m_mask = (sub_g_df['manzana_asignada'] == m_id)
                sub_part_idx = sub_g_df[m_mask].sort_values(by=['parc', 'calle', 'altura', 'suministro']).index.values
                n_part = len(sub_part_idx)
                chunk_size = int(math.ceil(n_part / k))
                for i, r_id in enumerate(sub_r_ids):
                    part_chunk = sub_part_idx[i * chunk_size : min((i + 1) * chunk_size, n_part)]
                    for c_idx in part_chunk:
                        nueva_ruta_col[c_idx] = r_id
                        obs_ruteo_col[c_idx] = f'MACRO_MANZANA_PARTE_{i+1}_DE_{k}'

            # D) Reabsorción Geoespacial de Casos Periféricos (Regla A4)
            pend_mask = (nueva_ruta_col[sub_indices] == 0)
            if pend_mask.sum() > 0:
                pend_indices = sub_indices[pend_mask]
                assigned_df = sub_g_df[~pend_mask].copy()
                assigned_df['ruta_tmp'] = nueva_ruta_col[sub_indices[~pend_mask]]
                r_centers = assigned_df.groupby('ruta_tmp')[['latitud', 'longitud']].median().dropna()

                if len(r_centers) > 0:
                    r_ids = r_centers.index.values
                    r_pts = np.array([d_to_xy(lat, lon) for lat, lon in r_centers.values])
                    r_tree = cKDTree(r_pts)
                    r_loads = assigned_df.groupby('ruta_tmp').size().to_dict()

                    for p_idx in pend_indices:
                        lat_p = df_int.at[p_idx, 'latitud']
                        lon_p = df_int.at[p_idx, 'longitud']
                        if pd.notna(lat_p) and pd.notna(lon_p):
                            px, py = d_to_xy(lat_p, lon_p)
                            dists, idxs = r_tree.query([px, py], k=min(10, len(r_ids)))
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
                                best_r = r_ids[idxs[0]]
                        else:
                            best_r = r_ids[0]

                        nueva_ruta_col[p_idx] = best_r
                        obs_ruteo_col[p_idx] = f'REABSORBIDO_PROXIMIDAD_VECINA_RUTA_{best_r}'
                        r_loads[best_r] = r_loads.get(best_r, 0) + 1
                else:
                    for p_idx in pend_indices:
                        nueva_ruta_col[p_idx] = current_route_id
                        obs_ruteo_col[p_idx] = 'RUTA_RESIDUAL_GRUPO'

            # Métricas del Grupo
            route_counts = pd.Series(nueva_ruta_col[sub_indices]).value_counts()
            n_rutas_nuevas = len(route_counts)
            n_rutas_nuevas_d += n_rutas_nuevas
            media_c = route_counts.mean()
            mediana_c = route_counts.median()
            en_tol = ((route_counts >= MIN_CAPACITY) & (route_counts <= MAX_CAPACITY)).sum()
            pct_tol = (en_tol / n_rutas_nuevas * 100) if n_rutas_nuevas > 0 else 0.0

            all_comparison_summary.append({
                'distrito': d_id,
                'distrito_descripcion': d_desc,
                'grupo_lectura': str(g_str),
                'cant_suministros': n_sumi_g,
                'rutas_anteriores': n_rutas_ant_g,
                'rutas_nuevas': n_rutas_nuevas,
                'promedio_sumi_anterior': round(n_sumi_g / n_rutas_ant_g, 1) if n_rutas_ant_g > 0 else 0.0,
                'promedio_sumi_nuevo': round(media_c, 1),
                'mediana_sumi_nuevo': int(mediana_c),
                'rutas_en_tolerancia': en_tol,
                'pct_en_tolerancia': round(pct_tol, 1)
            })

            print(f"    G{g_str:>2}: {n_sumi_g:>6} sumi | {n_rutas_ant_g:>3} ant -> {n_rutas_nuevas:>3} nuevas | Med: {media_c:5.1f} | Tol [{MIN_CAPACITY}-{MAX_CAPACITY}]: {pct_tol:5.1f}%")

        print(f"  🏁 Distrito {d_id} finalizado: {n_rutas_nuevas_d} rutas nuevas en {time.time()-t_d0:.2f}s.")

    df_int['nueva_ruta_lectura'] = nueva_ruta_col
    df_int['obs_asignacion_ruta'] = obs_ruteo_col

    # -------------------------------------------------------------------------
    # PASO 4: SECUENCIACIÓN DEL ORDEN DE LECTURA (PASO 10 - REGLA A3)
    # -------------------------------------------------------------------------
    print("\n[4/6] Secuenciando nuevo orden de lectura (Paso 10 por calle, vereda y altura)...")
    t3 = time.time()

    df_int['altura_num'] = pd.to_numeric(df_int['altura'], errors='coerce').fillna(0).astype(int)
    df_int['vereda_par'] = (df_int['altura_num'] % 2 == 0).astype(int)

    df_int = df_int.sort_values(
        by=['distrito', 'nueva_ruta_lectura', 'manzana_asignada', 'calle_norm', 'vereda_par', 'altura_num', 'suministro']
    ).reset_index(drop=True)

    df_int['nuevo_orden_lectura'] = (df_int.groupby(['distrito', 'nueva_ruta_lectura']).cumcount() + 1) * 10
    df_int['orden_lectura_sugerido'] = df_int.groupby(['distrito', 'nueva_ruta_lectura']).cumcount() + 1

    print(f"      Orden de lectura asignado para {len(df_int):,} suministros en {time.time()-t3:.2f}s.")

    # -------------------------------------------------------------------------
    # PASO 5: CONSTRUCCIÓN Y CONTROL GEOESPACIAL DE POLÍGONOS DE RUTAS
    # -------------------------------------------------------------------------
    print("\n[5/6] Construyendo polígonos vectoriales de rutas del interior y calculando métricas...")
    t4 = time.time()

    mza_route_counts = df_int.groupby(['manzana_asignada', 'distrito', 'nueva_ruta_lectura']).size().unstack(fill_value=0)
    split_mzas = set(mza_route_counts[(mza_route_counts > 0).sum(axis=1) > 1].index)

    route_geoms = defaultdict(list)
    unique_pairs = df_int.groupby(['distrito', 'nueva_ruta_lectura', 'manzana_asignada'])

    for (d_id, r_id, m), group in unique_pairs:
        key = (d_id, r_id)
        if m.startswith('VIRT_'):
            pts = [Point(xy) for xy in zip(group['longitud'].dropna(), group['latitud'].dropna())]
            if pts:
                u_pts = unary_union(pts)
                poly = u_pts.convex_hull.buffer(0.00035) if len(pts) >= 3 else u_pts.buffer(0.00035)
                route_geoms[key].append(make_valid(poly))
            continue

        is_split = (m in split_mzas)
        mza_ha = mza_area_ha_dict.get(m, 0.0)
        is_large = (mza_ha > 10.0)

        if not is_split and not is_large and m in mza_geom_dict:
            route_geoms[key].append(mza_geom_dict[m])
        else:
            pts = [Point(xy) for xy in zip(group['longitud'].dropna(), group['latitud'].dropna())]
            if pts:
                u_pts = unary_union(pts)
                sub_poly = u_pts.convex_hull.buffer(0.00025) if len(pts) >= 3 else u_pts.buffer(0.00025)
                if m in mza_geom_dict:
                    inter_poly = sub_poly.intersection(mza_geom_dict[m])
                    if not inter_poly.is_empty and inter_poly.area > 1e-10:
                        route_geoms[key].append(make_valid(inter_poly))
                    else:
                        route_geoms[key].append(make_valid(sub_poly))
                else:
                    route_geoms[key].append(make_valid(sub_poly))

    # Estadísticas por ruta
    route_stats = df_int.groupby(['distrito', 'nueva_ruta_lectura']).agg(
        distrito_descripcion=('distrito_descripcion', 'first'),
        grupo_lectura=('grupo_lectura', 'first'),
        cant_suministros=('suministro', 'count'),
        cant_manzanas=('manzana_asignada', 'nunique'),
        centroide_lat=('latitud', 'mean'),
        centroide_lon=('longitud', 'mean'),
        barrios=('barrio', lambda x: ", ".join([str(b) for b in x.dropna().unique()[:3]]))
    ).reset_index()

    route_stats_dict = route_stats.set_index(['distrito', 'nueva_ruta_lectura']).to_dict(orient='index')

    route_records = []
    for (d_id, r_id), g_list in route_geoms.items():
        if g_list:
            clean = [g.buffer(0) for g in g_list if g is not None and not g.is_empty]
            try:
                route_poly = make_valid(unary_union(clean))
            except Exception:
                route_poly = unary_union([g.convex_hull for g in clean])

            info = route_stats_dict.get((d_id, r_id), {})
            area_m2 = route_poly.area * (111139.0**2 * 0.85)
            perim_m = route_poly.length * 111139.0
            comp = (4.0 * math.pi * area_m2) / (perim_m * perim_m) if perim_m > 0 else 0.0
            comp = min(1.0, max(0.0, comp))
            cant_sumi = info.get('cant_suministros', 0)

            route_records.append({
                'distrito': d_id,
                'distrito_descripcion': str(info.get('distrito_descripcion', '')),
                'nueva_ruta_lectura': r_id,
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

    import geopandas as gpd
    gdf_routes_int = gpd.GeoDataFrame(route_records, geometry='geometry', crs="EPSG:4326")
    print(f"      Polígonos de rutas del interior construidos y disueltos: {len(gdf_routes_int):,} rutas.")

    df_all_routes_int = pd.DataFrame(route_records).drop(columns=['geometry'], errors='ignore')
    df_all_comp_int = pd.DataFrame(all_comparison_summary).sort_values(by=['distrito', 'grupo_lectura']).reset_index(drop=True)

    # -------------------------------------------------------------------------
    # PASO 6: GUARDAR ENTREGABLES DEL INTERIOR Y CONSOLIDACIÓN PROVINCIAL
    # -------------------------------------------------------------------------
    print("\n[6/6] Guardando entregables del interior y consolidando el Padrón Provincial...")

    cols_padron = [
        'suministro', 'cliente', 'contrato', 'distrito', 'distrito_descripcion',
        'grupo_lectura', 'ruta_lectura', 'orden_lectura',
        'nueva_ruta_lectura', 'nuevo_orden_lectura', 'orden_lectura_sugerido',
        'id_suministro_catastral', 'manzana_asignada', 'parcela_asignada',
        'calle', 'altura', 'barrio', 'localidad', 'latitud', 'longitud',
        'nivel_certeza', 'metodo_asignacion', 'obs_asignacion_ruta', 'estado_contrato', 'tarifa'
    ]

    # Guardar Entregables Interior
    print(f"  [1] Guardando Padrón Interior Parquet: {OUT_PADRON_INTERIOR_PARQUET}")
    df_int[cols_padron].to_parquet(OUT_PADRON_INTERIOR_PARQUET, index=False, engine='pyarrow', compression='snappy')

    print(f"  [2] Guardando Resumen de Rutas Interior CSV: {OUT_RESUMEN_RUTAS_CSV}")
    df_all_routes_int.to_csv(OUT_RESUMEN_RUTAS_CSV, index=False, encoding='utf-8-sig')

    print(f"  [3] Guardando Comparativo Interior CSV: {OUT_RESUMEN_COMPARATIVO_CSV}")
    df_all_comp_int.to_csv(OUT_RESUMEN_COMPARATIVO_CSV, index=False, encoding='utf-8-sig')

    print(f"  [4] Guardando Capa Geoespacial Rutas Interior Parquet: {OUT_RUTAS_INTERIOR_PARQUET}")
    gdf_routes_int.to_parquet(OUT_RUTAS_INTERIOR_PARQUET, index=False)

    print(f"  [5] Exportando GeoJSON Rutas Interior: {OUT_RUTAS_INTERIOR_GEOJSON}")
    gdf_routes_int.to_file(OUT_RUTAS_INTERIOR_GEOJSON, driver="GeoJSON")

    # Espejos de Descarga Interior
    for dl_path, prefix in [(DOWNLOADS_D, "D:"), (DOWNLOADS_C, "C:")]:
        if os.path.exists(dl_path):
            csv_t = os.path.join(dl_path, "padron_nuevas_rutas_interior_completo.csv")
            print(f"  [Espejo {prefix}] Exportando CSV Interior a Descargas: {csv_t}")
            df_int[cols_padron].to_csv(csv_t, index=False, encoding='utf-8-sig')

    if os.path.exists(DOWNLOADS_D):
        geo_t = os.path.join(DOWNLOADS_D, "rutas_nuevas_poligonos_interior.geojson")
        print(f"  [Espejo D:] Exportando GeoJSON Interior a Descargas: {geo_t}")
        gdf_routes_int.to_file(geo_t, driver="GeoJSON")

    # -------------------------------------------------------------------------
    # CONSOLIDACIÓN MAESTRA PROVINCIAL (D1 + INTERIOR CUBIERTO)
    # -------------------------------------------------------------------------
    if os.path.exists(PADRON_D1_IN):
        print("\n  🌟 CONSOLIDANDO PADRÓN PROVINCIAL MAESTRO (DISTRITO 1 + INTERIOR CUBIERTO)...")
        df_d1_done = pd.read_parquet(PADRON_D1_IN)
        df_prov_master = pd.concat([df_d1_done[cols_padron], df_int[cols_padron]], ignore_index=True)
        
        print(f"      Total Suministros Padrón Provincial Consolidado: {len(df_prov_master):,}")
        df_prov_master.to_parquet(OUT_PADRON_PROVINCIAL_PARQUET, index=False, engine='pyarrow', compression='snappy')
        print(f"      Padrón Provincial guardado: {OUT_PADRON_PROVINCIAL_PARQUET}")

        # Resumen general de rutas provincial
        res_d1_path = os.path.join(SUMMARY_DIR, "resumen_todas_rutas_nuevas_distrito1.csv")
        if os.path.exists(res_d1_path):
            df_r_d1 = pd.read_csv(res_d1_path)
            df_r_prov = pd.concat([df_r_d1, df_all_routes_int], ignore_index=True)
            df_r_prov.to_csv(OUT_RESUMEN_RUTAS_PROVINCIAL_CSV, index=False, encoding='utf-8-sig')
            print(f"      Resumen de Rutas Provincial guardado: {OUT_RESUMEN_RUTAS_PROVINCIAL_CSV} ({len(df_r_prov):,} rutas)")

        # GeoJSON provincial combinado
        if os.path.exists(RUTAS_D1_GEOJSON):
            gdf_d1_routes = gpd.read_file(RUTAS_D1_GEOJSON)
            gdf_prov_routes = pd.concat([gdf_d1_routes, gdf_routes_int], ignore_index=True)
            gdf_prov_routes = gpd.GeoDataFrame(gdf_prov_routes, geometry='geometry', crs="EPSG:4326")
            gdf_prov_routes.to_parquet(OUT_RUTAS_PROVINCIAL_PARQUET, index=False)
            gdf_prov_routes.to_file(OUT_RUTAS_PROVINCIAL_GEOJSON, driver="GeoJSON")
            print(f"      Capa Provincial de Rutas guardada: {OUT_RUTAS_PROVINCIAL_GEOJSON} ({len(gdf_prov_routes):,} rutas vectoriales)")

    # -------------------------------------------------------------------------
    # BALANCE FINAL EJECUTIVO
    # -------------------------------------------------------------------------
    t_total = time.time() - t_global_0
    print("\n" + "=" * 115)
    print(f"🏆 ASIGNACIÓN DE RUTAS DEL INTERIOR FINALIZADA EXITOSAMENTE EN {t_total:.2f}s ({t_total/60:.2f} min)!")
    print("=" * 115)
    print(f"Total Suministros Interior Cubierto: {len(df_int):,}")
    print(f"Total Nuevas Rutas Creadas:          {len(gdf_routes_int):,}")
    print(f"Promedio Global Suministros/Ruta:    {df_all_routes_int['cant_suministros'].mean():.1f}")
    print(f"Mediana Global Suministros/Ruta:     {df_all_routes_int['cant_suministros'].median():.1f}")
    print(f"Cumplimiento en Rango [{MIN_CAPACITY}-{MAX_CAPACITY}]:        {df_all_routes_int['cumple_capacidad'].value_counts(normalize=True).get('SI', 0)*100:.1f}%")
    print("=" * 115)

    # Tabla resumen por distrito
    d_summary = df_all_comp_int.groupby(['distrito', 'distrito_descripcion']).agg(
        suministros=('cant_suministros', 'sum'),
        rutas_anteriores=('rutas_anteriores', 'sum'),
        rutas_nuevas=('rutas_nuevas', 'sum'),
        promedio_nuevo=('promedio_sumi_nuevo', 'mean'),
        rutas_en_tolerancia=('rutas_en_tolerancia', 'sum')
    ).reset_index()
    d_summary['pct_tolerancia'] = (d_summary['rutas_en_tolerancia'] / d_summary['rutas_nuevas'] * 100).round(1)
    print("\nResumen por Distrito Comercial:")
    print(d_summary.to_string(index=False))

if __name__ == '__main__':
    main()
