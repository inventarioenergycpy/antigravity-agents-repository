# -*- coding: utf-8 -*-
import os, sys, json, time, glob, re
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

data_dir = r"D:\Proyectos\antigravity-agents-repository\data"
cache_dir = os.path.join(data_dir, "cache_parcelas_wfs")
suministros_path = os.path.join(data_dir, "suministros_provincial_completo.parquet")
mzas_path = os.path.join(data_dir, "manzanas_alta_resolucion_provincial.parquet")
out_parquet = os.path.join(data_dir, "convergencia_suministros_provincial_final.parquet")

def normalizar_dc_str(dc_raw):
    if not dc_raw or pd.isna(dc_raw):
        return ""
    s = str(dc_raw).strip().upper().replace(" ", "").replace(".", "").replace("-", "")
    if len(s) == 16:
        # DD-PP-MM-CC-SS-MMM-PPP -> 2-2-2-2-2-3-3 = 16 digits
        return f"{s[0:2]}-{s[2:4]}-{s[4:6]}-{s[6:8]}-{s[8:10]}-{s[10:13]}-{s[13:16]}"
    elif len(s) == 18:
        # Formato con sub-lote o PH adicional
        return f"{s[0:2]}-{s[2:4]}-{s[4:6]}-{s[6:8]}-{s[8:10]}-{s[10:13]}-{s[13:16]}"
    return str(dc_raw).strip()

def normalizar_calle(calle_raw):
    if not calle_raw or pd.isna(calle_raw):
        return ""
    c = str(calle_raw).strip().upper()
    c = re.sub(r'^(CALLE|AV\.?|AVENIDA|PASAJE|PJE\.?|BV\.?|BOULEVARD|RUTA)\s+', '', c)
    c = re.sub(r'[^A-Z0-9\s]', '', c)
    return ' '.join(c.split())

def ejecutar_convergencia():
    print("=" * 80)
    print("🚀 MOTOR DE CONVERGENCIA EN 4 PARTES A ESCALA PROVINCIAL (1.208.097 SUMINISTROS)")
    print("=" * 80)
    
    t0 = time.time()
    
    # 1. Cargar Manzanas Sintéticas de Alta Resolución
    print("📦 Cargando Manzanas Sintéticas provinciales...")
    df_mzas = pd.read_parquet(mzas_path)
    print(f"  Total Manzanas cargadas: {len(df_mzas):,}")
    
    # Set de manzanas válidas y diccionario toponímico
    mzas_set = set(df_mzas['mza_wfs'].unique())
    mza_calles_dict = {}
    for _, row in df_mzas.iterrows():
        m_k = row['mza_wfs']
        calles_str = row['calles_perimetrales'] or ''
        calles_norm = set()
        for cl in calles_str.split(','):
            cn = normalizar_calle(cl)
            if cn:
                calles_norm.add(cn)
        mza_calles_dict[m_k] = {
            "calles": calles_norm,
            "lat": row['centro_lat'],
            "lon": row['centro_lon']
        }
        
    # 2. Cargar Parcelas Oficiales desde cache WFS
    print("📦 Extrayendo claves de parcelas oficiales desde chunks locales...")
    chunk_files = glob.glob(os.path.join(cache_dir, "*.json"))
    parc_set = set()
    for fpath in chunk_files:
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                cdata = json.load(f)
            feats = cdata.get('features', []) if isinstance(cdata, dict) else (cdata if isinstance(cdata, list) else [])
            for feat in feats:
                props = feat.get('properties', {})
                nom = (props.get('nomenclatura') or '').strip()
                if nom:
                    parc_set.add(nom)
        except Exception:
            continue
    print(f"  Total Parcelas oficiales únicas indexadas: {len(parc_set):,}")
    
    # 3. Cargar Suministros
    print("\n📦 Cargando base provincial de suministros...")
    df_sum = pd.read_parquet(suministros_path)
    total_sum = len(df_sum)
    print(f"  Total Suministros a evaluar: {total_sum:,}")
    
    # 4. Evaluación Vectorizada del Motor en 4 Partes
    print("\n⚙️ Evaluando convergencia en 4 partes...")
    
    # Arrays para almacenar resultados
    res_nivel = []
    res_metodo = []
    res_parc = []
    res_mza = []
    
    # Pre-cálculos para velocidad extrema
    dc_norm_arr = [normalizar_dc_str(x) for x in df_sum['dc'].values]
    calle_norm_arr = [normalizar_calle(x) for x in df_sum['calle'].values]
    
    dist_arr = df_sum['distrito'].values
    zc_arr = df_sum['zona_catastral'].values
    dc_cata_arr = df_sum['distrito_catastral'].values
    mc_arr = df_sum['manzana_catastral'].values
    lc_arr = df_sum['lote_catastral'].values
    
    lat_arr = df_sum['latitud'].values
    lon_arr = df_sum['longitud'].values
    
    for i in range(total_sum):
        dc_val = dc_norm_arr[i]
        calle_val = calle_norm_arr[i]
        
        # Dimensión 1: DC Exacta
        c1_parc = dc_val in parc_set
        c1_mza = "-".join(dc_val.split('-')[:6]) in mzas_set if len(dc_val.split('-')) >= 6 else False
        
        # Dimensión 2: Cuaterna Catastral
        c2_match = False
        c2_parc_str = ""
        c2_mza_str = ""
        d_val = dist_arr[i]
        
        try:
            zc = int(zc_arr[i]) if pd.notna(zc_arr[i]) else 0
            d_cat = int(dc_cata_arr[i]) if pd.notna(dc_cata_arr[i]) else 0
            mc = int(mc_arr[i]) if pd.notna(mc_arr[i]) else 0
            lc = int(lc_arr[i]) if pd.notna(lc_arr[i]) else 0
            
            if d_val == 1 and d_cat > 0 and zc > 0 and mc > 0:
                c2_mza_str = f"11-01-01-{d_cat:02d}-{zc:02d}-{mc:03d}"
                c2_parc_str = f"{c2_mza_str}-{lc:03d}" if lc > 0 else ""
                if c2_parc_str in parc_set or c2_mza_str in mzas_set:
                    c2_match = True
        except Exception:
            pass
            
        # Determinar manzana de anclaje candidata
        cand_mza = "-".join(dc_val.split('-')[:6]) if c1_mza else (c2_mza_str if c2_match else "")
        
        # Dimensión 3: Calle / Toponimia
        c3_match = False
        if cand_mza and cand_mza in mza_calles_dict and calle_val:
            mza_info = mza_calles_dict[cand_mza]
            if calle_val in mza_info["calles"]:
                c3_match = True
            else:
                for mc_name in mza_info["calles"]:
                    if len(calle_val) >= 4 and (calle_val in mc_name or mc_name in calle_val):
                        c3_match = True
                        break
                        
        # Dimensión 4: Coordenadas Espaciales
        c4_match = False
        lat_v = lat_arr[i]
        lon_v = lon_arr[i]
        if cand_mza and cand_mza in mza_calles_dict and pd.notna(lat_v) and pd.notna(lon_v):
            mza_info = mza_calles_dict[cand_mza]
            dlat = abs(lat_v - mza_info["lat"])
            dlon = abs(lon_v - mza_info["lon"])
            # Tolerancia ~150 metros (0.0015 grados)
            if dlat < 0.0020 and dlon < 0.0020:
                c4_match = True
                
        # Clasificación en Niveles
        puntos = (1 if (c1_parc or c1_mza) else 0) + (1 if c2_match else 0) + (1 if c3_match else 0) + (1 if c4_match else 0)
        
        if c1_parc:
            res_nivel.append("NIVEL_1A_ALTA_DC_EXACTA")
            res_metodo.append("DC_EXACTA")
            res_parc.append(dc_val)
            res_mza.append("-".join(dc_val.split('-')[:6]))
        elif puntos >= 3:
            res_nivel.append("NIVEL_1B_ALTA_MULTICRITERIO")
            res_metodo.append(f"CONVERGENCIA_{puntos}P")
            res_parc.append(c2_parc_str if c2_parc_str in parc_set else "")
            res_mza.append(cand_mza)
        elif puntos == 2:
            res_nivel.append("NIVEL_2_CERTEZA_MEDIA")
            res_metodo.append("CONVERGENCIA_2P")
            res_parc.append(c2_parc_str if c2_parc_str in parc_set else "")
            res_mza.append(cand_mza)
        elif cand_mza and (cand_mza in mzas_set):
            res_nivel.append("NIVEL_3_PARCIAL_MANZANA")
            res_metodo.append("MANZANA_CONFIRMADA")
            res_parc.append("")
            res_mza.append(cand_mza)
        else:
            res_nivel.append("NIVEL_4_SIN_CONVERGENCIA")
            res_metodo.append("DISCREPANCIA")
            res_parc.append("")
            res_mza.append("")
            
        if (i + 1) % 200000 == 0 or (i + 1) == total_sum:
            print(f"  Evaluados {i+1:,}/{total_sum:,} suministros ({(i+1)/total_sum*100:.1f}%)...", flush=True)

    df_sum['nivel_certeza'] = res_nivel
    df_sum['metodo_asignacion'] = res_metodo
    df_sum['parcela_asignada'] = res_parc
    df_sum['manzana_asignada'] = res_mza
    
    print(f"\n📊 Balance Inicial Motor 4 Partes ({time.time()-t0:.2f}s):")
    print(df_sum['nivel_certeza'].value_counts())
    
    # 5. Segunda Iteración: Propagación por Vecindad de Ruta (+-3)
    print("\n🔄 Ejecutando Segunda Iteración: Propagación de Vecindad de Ruta (orden +-3)...")
    t1 = time.time()
    
    # Agrupar por ruta operativa
    grupos_ruta = df_sum.groupby(['distrito', 'grupo_lectura', 'ruta_lectura'])
    print(f"  Total Rutas de lectura a procesar: {len(grupos_ruta):,}")
    
    promovidos_cnt = 0
    indices_promovidos = []
    
    # Recorrer rutas para inferencia local
    for (dist, grp, ruta), g_df in grupos_ruta:
        if len(g_df) < 3:
            continue
            
        g_df_sorted = g_df.sort_values('orden_lectura')
        indices = g_df_sorted.index.values
        niveles = g_df_sorted['nivel_certeza'].values
        mzas = g_df_sorted['manzana_asignada'].values
        parcs = g_df_sorted['parcela_asignada'].values
        
        n_rut = len(indices)
        for pos in range(n_rut):
            niv = niveles[pos]
            if niv in ['NIVEL_2_CERTEZA_MEDIA', 'NIVEL_3_PARCIAL_MANZANA']:
                # Ventana local +-3
                win_start = max(0, pos - 3)
                win_end = min(n_rut, pos + 4)
                
                vecinos_mza = [mzas[k] for k in range(win_start, win_end) if k != pos and niveles[k] in ['NIVEL_1A_ALTA_DC_EXACTA', 'NIVEL_1B_ALTA_MULTICRITERIO'] and mzas[k]]
                
                if len(vecinos_mza) >= 2:
                    # Encontrar moda de los vecinos
                    from collections import Counter
                    most_common_mza, cnt = Counter(vecinos_mza).most_common(1)[0]
                    if cnt >= 2:
                        idx_orig = indices[pos]
                        df_sum.at[idx_orig, 'nivel_certeza'] = 'NIVEL_1C_ALTA_REVALIDADA_VECINOS'
                        df_sum.at[idx_orig, 'metodo_asignacion'] = 'VECINOS_RUTA_CONSENSO'
                        if not df_sum.at[idx_orig, 'manzana_asignada']:
                            df_sum.at[idx_orig, 'manzana_asignada'] = most_common_mza
                        promovidos_cnt += 1

    print(f"✅ Propagación finalizada en {time.time()-t1:.2f}s:")
    print(f"  Suministros promovidos a Alta Certeza por vecinos: {promovidos_cnt:,}")
    
    print("\n📊 BALANCE FINAL CONSOLIDADO PROVINCIAL:")
    res_final = df_sum['nivel_certeza'].value_counts()
    for cat, val in res_final.items():
        print(f"  {cat}: {val:,} ({val/total_sum*100:.2f}%)")
        
    alta_tot = df_sum['nivel_certeza'].str.startswith('NIVEL_1').sum()
    parcial_tot = (df_sum['nivel_certeza'] == 'NIVEL_3_PARCIAL_MANZANA').sum()
    cobertura_tot = alta_tot + parcial_tot
    print("\n" + "=" * 80)
    print(f"🏆 TOTAL ALTA CERTEZA PROVINCIAL: {alta_tot:,} ({alta_tot/total_sum*100:.2f}%)")
    print(f"🌐 COBERTURA TERRITORIAL ÚTIL: {cobertura_tot:,} ({cobertura_tot/total_sum*100:.2f}%)")
    print("=" * 80)
    
    # 6. Guardar dataset Parquet provincial final
    print(f"\n💾 Guardando dataset final en: {out_parquet}...")
    df_sum.to_parquet(out_parquet, index=False, engine='pyarrow', compression='snappy')
    size_mb = os.path.getsize(out_parquet) / (1024 * 1024)
    print(f"✅ Archivo guardado con éxito: {size_mb:.2f} MB en {time.time()-t0:.2f} segundos.")

if __name__ == "__main__":
    ejecutar_convergencia()
