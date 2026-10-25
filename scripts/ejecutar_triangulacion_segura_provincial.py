# -*- coding: utf-8 -*-
import os, sys, time, re
import pandas as pd
import numpy as np
from collections import Counter
from scipy.spatial import cKDTree

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

repo_dir = r"D:\Proyectos\antigravity-agents-repository"
data_dir = os.path.join(repo_dir, "data")
conv_path = os.path.join(data_dir, "convergencia_suministros_provincial_final.parquet")
mzas_path = os.path.join(data_dir, "manzanas_alta_resolucion_provincial.parquet")
out_parquet = os.path.join(data_dir, "padron_suministros_triangulado_provincial.parquet")

def norm_calle(c):
    if not c or pd.isna(c):
        return ""
    s = str(c).strip().upper()
    s = re.sub(r'^(CALLE|AV\.?|AVENIDA|PASAJE|PJE\.?|BV\.?|BOULEVARD|RUTA)\s+', '', s)
    s = re.sub(r'[^A-Z0-9\s]', '', s)
    return ' '.join(s.split())

def ejecutar_triangulacion():
    print("=" * 90)
    print("🚀 ETAPA A: MOTOR DE TRIANGULACIÓN SEGURA (2 VECINOS + CALLE + ALTURA + GEOREF)")
    print("=" * 90)
    
    t0 = time.time()
    print("1. Cargando datasets de suministros y manzanas sintéticas...")
    df = pd.read_parquet(conv_path)
    df_mzas = pd.read_parquet(mzas_path)
    
    total_prov = len(df)
    print(f"  Total suministros provinciales: {total_prov:,}")
    print(f"  Total manzanas sintéticas provinciales: {len(df_mzas):,}")
    
    # Distritos comerciales que cuentan con cartografía de manzanas
    covered_distritos = [1, 8, 18, 23, 24, 28, 45, 47]
    print(f"  Distritos con cobertura parcelaria: {covered_distritos}")
    
    # Diccionario de manzanas con calles y centroides
    mza_dict = {}
    for _, r in df_mzas.iterrows():
        m_k = r['mza_wfs']
        calles_raw = r['calles_perimetrales'] or ''
        c_set = set([norm_calle(c) for c in calles_raw.split(',') if c.strip()])
        mza_dict[m_k] = {
            'depto': r['depto'],
            'calles': c_set,
            'lat': r['centro_lat'],
            'lon': r['centro_lon']
        }
        
    # Identificar suministros pendientes en distritos cubiertos
    mask_covered = df['distrito'].isin(covered_distritos)
    mask_pending = mask_covered & (df['manzana_asignada'].isna() | (df['manzana_asignada'] == ''))
    
    print(f"\n2. Analizando suministros en distritos con cartografía:")
    print(f"  Total en distritos cubiertos: {mask_covered.sum():,}")
    print(f"  Con manzana ya asignada: {(mask_covered & ~mask_pending).sum():,} ({(mask_covered & ~mask_pending).mean()*100:.1f}%)")
    print(f"  Pendientes de triangulación segura: {mask_pending.sum():,}")
    
    # -------------------------------------------------------------------------
    # PASO 1: Triangulación por 2 Vecinos Inmediatos de Lectura + Calle + Altura
    # -------------------------------------------------------------------------
    print("\n3. Ejecutando Triangulación Segura por 2 Vecinos de Lectura (+-5) con Calle Coincidente...")
    t1 = time.time()
    
    # Pre-calcular calles normalizadas
    df['calle_norm'] = [norm_calle(c) for c in df['calle'].values]
    
    indices_triangulados = []
    mzas_trianguladas = []
    
    # Agrupar por ruta operativa
    grupos_ruta = df[mask_covered].groupby(['distrito', 'grupo_lectura', 'ruta_lectura'])
    
    for (dist, grp, ruta), gdf in grupos_ruta:
        if len(gdf) < 3:
            continue
            
        gdf_sorted = gdf.sort_values('orden_lectura')
        sub_indices = gdf_sorted.index.values
        mzas = gdf_sorted['manzana_asignada'].values
        calles = gdf_sorted['calle_norm'].values
        alturas = gdf_sorted['altura'].values
        lats = gdf_sorted['latitud'].values
        lons = gdf_sorted['longitud'].values
        
        n_pts = len(sub_indices)
        for pos in range(n_pts):
            if mzas[pos] != '':
                continue
                
            c_i = calles[pos]
            alt_i = alturas[pos]
            lat_i = lats[pos]
            lon_i = lons[pos]
            
            # Ventana de lectura +-5 vecinos
            w_start = max(0, pos - 5)
            w_end = min(n_pts, pos + 6)
            
            # Buscar vecinos con manzana válida y misma calle
            vecinos_mza = []
            for k in range(w_start, w_end):
                if k == pos or mzas[k] == '':
                    continue
                # Coincidencia de calle
                if c_i and calles[k] and (c_i == calles[k] or c_i in calles[k] or calles[k] in c_i):
                    # Validar altura si existe (diferencia razonable <= 400 números)
                    if pd.notna(alt_i) and pd.notna(alturas[k]):
                        if abs(alt_i - alturas[k]) <= 400:
                            vecinos_mza.append(mzas[k])
                    else:
                        vecinos_mza.append(mzas[k])
                        
            # Si al menos 2 vecinos coinciden en la manzana
            if len(vecinos_mza) >= 2:
                mza_propuesta, cnt = Counter(vecinos_mza).most_common(1)[0]
                if cnt >= 2:
                    # Validar con georreferencia si existen coordenadas
                    geo_ok = True
                    if pd.notna(lat_i) and pd.notna(lon_i) and mza_propuesta in mza_dict:
                        m_lat = mza_dict[mza_propuesta]['lat']
                        m_lon = mza_dict[mza_propuesta]['lon']
                        d_m = ((lat_i - m_lat)**2 + ((lon_i - m_lon)*0.85)**2)**0.5 * 111139.0
                        if d_m > 150.0:
                            geo_ok = False
                            
                    if geo_ok:
                        indices_triangulados.append(sub_indices[pos])
                        mzas_trianguladas.append(mza_propuesta)
                        
    # Aplicar asignaciones del Paso 1
    for idx, mza in zip(indices_triangulados, mzas_trianguladas):
        df.at[idx, 'manzana_asignada'] = mza
        df.at[idx, 'nivel_certeza'] = 'NIVEL_1C_ALTA_REVALIDADA_TRIANGULACION'
        df.at[idx, 'metodo_asignacion'] = 'TRIANGULACION_2_VECINOS_CALLE_ALTURA'
        
    print(f"  ✅ Triangulados con 2 vecinos y calle: {len(indices_triangulados):,} suministros en {time.time()-t1:.2f}s.")

    # -------------------------------------------------------------------------
    # PASO 2: Proximidad Espacial Segura (k-NN <= 70m) con Calle Coincidente
    # -------------------------------------------------------------------------
    print("\n4. Ejecutando Proximidad Espacial Segura (k-NN <= 70m) con validación de calle...")
    t2 = time.time()
    
    mask_pending2 = mask_covered & (df['manzana_asignada'] == '') & df['latitud'].notna() & df['longitud'].notna()
    print(f"  Suministros pendientes con coordenadas: {mask_pending2.sum():,}")
    
    knn_resueltos = 0
    # Agrupar manzanas por departamento / distrito
    # Para Distrito 1 (Capital)
    d1_mzas = df_mzas[df_mzas['depto'] == '11']
    d1_coords = d1_mzas[['centro_lat', 'centro_lon']].values
    d1_keys = d1_mzas['mza_wfs'].values
    
    lat0 = -31.42
    def to_xy(lats, lons):
        ys = (lats - lat0) * 111139.0
        xs = (lons - (-64.18)) * 111139.0 * np.cos(np.radians(lat0))
        return np.column_stack([xs, ys])
        
    d1_xy = to_xy(d1_coords[:, 0], d1_coords[:, 1])
    d1_tree = cKDTree(d1_xy)
    
    sub_pend_d1 = df[mask_pending2 & (df['distrito'] == 1)]
    if len(sub_pend_d1) > 0:
        s_xy = to_xy(sub_pend_d1['latitud'].values, sub_pend_d1['longitud'].values)
        dists, idxs = d1_tree.query(s_xy, k=3)
        
        sub_indices = sub_pend_d1.index.values
        sub_calles = sub_pend_d1['calle_norm'].values
        
        for p in range(len(sub_indices)):
            c_val = sub_calles[p]
            assigned = False
            
            # Revisar los 3 vecinos más cercanos
            for k in range(3):
                d_m = dists[p, k]
                if d_m > 70.0: # Regla estricta: <= 70 metros
                    continue
                cand_mza = d1_keys[idxs[p, k]]
                m_calles = mza_dict[cand_mza]['calles']
                
                # Si comparte la calle o está a menos de 45m del centroide
                if c_val and any(c_val in mc or mc in c_val for mc in m_calles) or d_m <= 45.0:
                    orig_idx = sub_indices[p]
                    df.at[orig_idx, 'manzana_asignada'] = cand_mza
                    df.at[orig_idx, 'nivel_certeza'] = 'NIVEL_1C_ALTA_REVALIDADA_GEOREF'
                    df.at[orig_idx, 'metodo_asignacion'] = 'GEOREF_PROXIMIDAD_70M'
                    knn_resueltos += 1
                    assigned = True
                    break

    print(f"  ✅ Asignados por proximidad espacial <= 70m: {knn_resueltos:,} suministros en {time.time()-t2:.2f}s.")
    
    # -------------------------------------------------------------------------
    # Balance Consolidado Post-Triangulación
    # -------------------------------------------------------------------------
    print("\n" + "=" * 90)
    print(f"📊 BALANCE FINAL POST-TRIANGULACIÓN SEGURA ({time.time()-t0:.2f}s):")
    total_con_mza = (df['manzana_asignada'] != '').sum()
    total_alta = df['nivel_certeza'].str.startswith('NIVEL_1').sum()
    print(f"  Total Suministros con Manzana Sintética Oficial: {total_con_mza:,} ({total_con_mza/total_prov*100:.2f}%)")
    print(f"  Total Suministros en ALTA CERTEZA: {total_alta:,} ({total_alta/total_prov*100:.2f}%)")
    
    # En Distrito 1 (Capital)
    d1_final = df[df['distrito'] == 1]
    d1_alta = d1_final['nivel_certeza'].str.startswith('NIVEL_1').sum()
    d1_mza = (d1_final['manzana_asignada'] != '').sum()
    print(f"\n  🎯 EN DISTRITO 1 (CAPITAL - {len(d1_final):,} suministros):")
    print(f"    Con Manzana Asignada: {d1_mza:,} ({d1_mza/len(d1_final)*100:.2f}%)")
    print(f"    En Alta Certeza: {d1_alta:,} ({d1_alta/len(d1_final)*100:.2f}%)")
    print("=" * 90)
    
    # Guardar dataset Parquet
    print(f"\n💾 Guardando dataset triangulado en: {out_parquet}...")
    df.drop(columns=['calle_norm'], inplace=True, errors='ignore')
    df.to_parquet(out_parquet, index=False, engine='pyarrow', compression='snappy')
    size_mb = os.path.getsize(out_parquet) / (1024 * 1024)
    print(f"✅ Guardado exitoso: {size_mb:.2f} MB en {time.time()-t0:.2f} segundos.")

if __name__ == "__main__":
    ejecutar_triangulacion()
