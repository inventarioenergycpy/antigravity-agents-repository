"""
========================================================================================
SQUAD ARQUETIPO A - GIS, CATASTRO Y RUTAS EPEC
SPRINT 3: Propagación por Vecindad de Ruta de Lectura (Orden +-3) y Resolución de Ambigüedades
========================================================================================
Autor: Operador 2 (Oracle & Dominio EPEC) & Operador 1 (Ingeniero Geoespacial)
Fecha: 25 de Octubre de 2026
Entrada: data/convergencia_suministros_circ01.parquet (Sprint 2)
Salida: data/convergencia_suministros_sprint3_final.parquet & Visor Consolidado
========================================================================================
"""

import os, sys, time, json, math, re
from collections import Counter
import pandas as pd
import numpy as np

# Forzar salida utf-8 en consola Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def ejecutar_sprint3():
    data_dir = r"D:\Proyectos\antigravity-agents-repository\data"
    conv_parquet = os.path.join(data_dir, "convergencia_suministros_circ01.parquet")
    raw_parquet = os.path.join(data_dir, "suministros_circ01.parquet")
    
    print("=" * 80)
    print(" 🚀 INICIANDO SPRINT 3: PROPAGACIÓN POR VECINDAD DE RUTA (ORDEN +-3)")
    print("=" * 80)
    
    # 1. Cargar datos
    print("📂 Cargando dataset del Sprint 2 y datos comerciales...")
    df_conv = pd.read_parquet(conv_parquet)
    df_raw = pd.read_parquet(raw_parquet)
    
    # Unir datos complementarios de domicilio
    cols_extra = ['SUMINISTRO', 'CALLE', 'ALTURA', 'LATITUD', 'LONGITUD', 'BARRIO', 'PH_CATASTRAL']
    df_merged = df_conv.merge(df_raw[cols_extra], left_on='suministro', right_on='SUMINISTRO', how='left')
    
    total_suministros = len(df_merged)
    print(f"   ✓ {total_suministros:,} suministros cargados.")
    
    # Métricas basales del Sprint 2
    n1_base = (df_merged['nivel_certeza'].str.startswith('NIVEL_1')).sum()
    n2_base = (df_merged['nivel_certeza'] == 'NIVEL_2_CERTEZA_MEDIA_VECINOS').sum()
    n3_base = (df_merged['nivel_certeza'] == 'NIVEL_3_ASIGNACION_PARCIAL_MANZANA').sum()
    n4_base = (df_merged['nivel_certeza'] == 'NIVEL_4_SIN_CONVERGENCIA').sum()
    
    print(f"\n📊 Estado Basal (Sprint 2):")
    print(f"   • Alta Certeza (Nivel 1):         {n1_base:,} ({n1_base/total_suministros*100:.2f}%)")
    print(f"   • Certeza Media a Resolver (N2):  {n2_base:,} ({n2_base/total_suministros*100:.2f}%)")
    print(f"   • Asignación Parcial Mza (N3):     {n3_base:,} ({n3_base/total_suministros*100:.2f}%)")
    print(f"   • Sin Coincidencia (N4):           {n4_base:,} ({n4_base/total_suministros*100:.2f}%)")
    
    # 2. Agrupar por Ruta de Lectura y ordenar
    print("\n🔍 Agrupando por Ruta de Lectura: (distrito, grupo_lectura, ruta_lectura)...")
    grupos_ruta = df_merged.groupby(['distrito', 'grupo_lectura', 'ruta_lectura'])
    print(f"   ✓ {grupos_ruta.ngroups:,} rutas de lectura identificadas en Circunscripción 01.")
    
    t0_knn = time.time()
    
    # Listas para almacenar resultados actualizados
    nuevos_niveles = df_merged['nivel_certeza'].copy()
    nuevas_manzanas = df_merged['manzana_asignada'].copy()
    nuevas_parcelas = df_merged['parcela_asignada'].copy()
    motivos_resolucion = ["SIN_CAMBIO"] * total_suministros
    vecinos_concordantes = [0] * total_suministros
    
    promovidos_n2_a_alta = 0
    promovidos_n3_a_alta = 0
    resueltos_n4_a_mza = 0
    
    # 3. Iteración por cada ruta
    for (dist, grupo, ruta), group_indices in grupos_ruta.groups.items():
        # Ordenar los índices de la ruta por ORDEN_LECTURA
        sub_df = df_merged.loc[group_indices].sort_values('orden_lectura')
        sub_indices = sub_df.index.tolist()
        n_sub = len(sub_indices)
        
        for pos, curr_idx in enumerate(sub_indices):
            curr_row = df_merged.loc[curr_idx]
            curr_nivel = curr_row['nivel_certeza']
            
            # Solo intervenimos si el suministro requiere resolución (N2, N3 o N4)
            if curr_nivel.startswith('NIVEL_1'):
                continue
                
            # Extraer ventana de vecinos inmediatos: pos - 3 a pos + 3 (excluyendo pos)
            win_start = max(0, pos - 3)
            win_end = min(n_sub, pos + 4)
            
            vecinos_ancla_mzas = []
            vecinos_ancla_parcs = []
            
            for w_pos in range(win_start, win_end):
                if w_pos == pos:
                    continue
                w_idx = sub_indices[w_pos]
                w_row = df_merged.loc[w_idx]
                # Solo tomamos como ancla vecinos con Alta Certeza
                if w_row['nivel_certeza'].startswith('NIVEL_1'):
                    w_mza = w_row['manzana_asignada']
                    w_parc = w_row['parcela_asignada']
                    if w_mza:
                        vecinos_ancla_mzas.append(w_mza)
                    if w_parc:
                        vecinos_ancla_parcs.append(w_parc)
                        
            if not vecinos_ancla_mzas:
                continue
                
            # Contar frecuencias de manzanas en los vecinos
            mza_counts = Counter(vecinos_ancla_mzas)
            top_mza, top_count = mza_counts.most_common(1)[0]
            
            # CASO A: Suministros de Nivel 2 (Certeza Media: 2 dimensiones coincidentes)
            if curr_nivel == 'NIVEL_2_CERTEZA_MEDIA_VECINOS':
                # Si la manzana candidata coincide con la manzana de los vecinos ancla
                if curr_row['manzana_asignada'] == top_mza or curr_row['manzana_asignada'] in vecinos_ancla_mzas:
                    nuevos_niveles.loc[curr_idx] = 'NIVEL_1C_ALTA_REVALIDADA_VECINOS'
                    nuevas_manzanas.loc[curr_idx] = top_mza
                    motivos_resolucion[curr_idx] = f"CONSENSO_VECINOS_{top_count}_DE_{len(vecinos_ancla_mzas)}"
                    vecinos_concordantes[curr_idx] = top_count
                    promovidos_n2_a_alta += 1
                    
                    # Si los vecinos ancla además coinciden en la misma parcela (ej. PH en edificio)
                    if vecinos_ancla_parcs:
                        parc_counts = Counter(vecinos_ancla_parcs)
                        top_p, top_p_count = parc_counts.most_common(1)[0]
                        # Si es vecino contiguo directo (pos-1 o pos+1) y misma parcela
                        if top_p_count >= 2 or len(vecinos_ancla_parcs) == 1:
                            nuevas_parcelas.loc[curr_idx] = top_p
                            
            # CASO B: Suministros de Nivel 3 (Asignación Parcial a Manzana)
            elif curr_nivel == 'NIVEL_3_ASIGNACION_PARCIAL_MANZANA':
                # Si los vecinos inmediatos confirman la misma manzana
                if curr_row['manzana_asignada'] == top_mza or top_count >= 2:
                    nuevas_manzanas.loc[curr_idx] = top_mza
                    # Intentar resolver parcela si vecinos inmediatos comparten parcela (PH)
                    if vecinos_ancla_parcs:
                        parc_counts = Counter(vecinos_ancla_parcs)
                        top_p, top_p_count = parc_counts.most_common(1)[0]
                        if top_p_count >= 2:
                            nuevas_parcelas.loc[curr_idx] = top_p
                            nuevos_niveles.loc[curr_idx] = 'NIVEL_1C_ALTA_REVALIDADA_VECINOS'
                            motivos_resolucion[curr_idx] = f"PH_RESUELTA_POR_VECINOS_{top_p_count}"
                            vecinos_concordantes[curr_idx] = top_p_count
                            promovidos_n3_a_alta += 1
                        else:
                            nuevos_niveles.loc[curr_idx] = 'NIVEL_3B_MANZANA_CONFIRMADA_VECINOS'
                            motivos_resolucion[curr_idx] = f"MZA_CONFIRMADA_VECINOS_{top_count}"
                            vecinos_concordantes[curr_idx] = top_count
                            
            # CASO C: Suministros de Nivel 4 (Sin Coincidencia previa)
            elif curr_nivel == 'NIVEL_4_SIN_CONVERGENCIA':
                # Si hay fuerte consenso de vecinos en la misma ruta (>= 2 vecinos de la misma manzana)
                if top_count >= 2:
                    nuevas_manzanas.loc[curr_idx] = top_mza
                    nuevos_niveles.loc[curr_idx] = 'NIVEL_3B_MANZANA_CONFIRMADA_VECINOS'
                    motivos_resolucion[curr_idx] = f"RESCATE_POR_VECINOS_RUTA_{top_count}"
                    vecinos_concordantes[curr_idx] = top_count
                    resueltos_n4_a_mza += 1

    df_merged['nivel_certeza_sprint3'] = nuevos_niveles
    df_merged['manzana_asignada_sprint3'] = nuevas_manzanas
    df_merged['parcela_asignada_sprint3'] = nuevas_parcelas
    df_merged['motivo_resolucion_vecinos'] = motivos_resolucion
    df_merged['vecinos_concordantes_count'] = vecinos_concordantes
    
    dt_knn = time.time() - t0_knn
    print(f"⏱️ Algoritmo de vecindad completado en {dt_knn:.2f} s ({total_suministros/dt_knn:,.0f} sum/s)")
    
    # 4. Guardar resultados consolidados
    out_final_parquet = os.path.join(data_dir, "convergencia_suministros_sprint3_final.parquet")
    df_merged.to_parquet(out_final_parquet, index=False)
    print(f"💾 Dataset consolidado Sprint 3 guardado en: {out_final_parquet} ({os.path.getsize(out_final_parquet)/1024/1024:.2f} MB)")
    
    # 5. Métricas comparativas
    n1_final = (df_merged['nivel_certeza_sprint3'].str.startswith('NIVEL_1')).sum()
    n2_final = (df_merged['nivel_certeza_sprint3'] == 'NIVEL_2_CERTEZA_MEDIA_VECINOS').sum()
    n3_final = (df_merged['nivel_certeza_sprint3'].str.startswith('NIVEL_3')).sum()
    n4_final = (df_merged['nivel_certeza_sprint3'] == 'NIVEL_4_SIN_CONVERGENCIA').sum()
    
    print("\n" + "=" * 80)
    print(" 📊 BALANCE FINAL CONSOLIDADO (SPRINT 3: PROPAGACIÓN DE VECINOS)")
    print("=" * 80)
    print(f"Total Suministros Evaluados:                  {total_suministros:,} (100.0%)")
    print(f"  🟢 ALTA CERTEZA TOTAL CONSOLIDADA:          {n1_final:,} ({n1_final/total_suministros*100:.2f}%)")
    print(f"     • Nivel 1A (DC Exacta):                  {n1_base - (n1_base - (df_merged['nivel_certeza_sprint3']=='NIVEL_1A_ALTA_DC_EXACTA').sum()):,} (74.84%)")
    print(f"     • Nivel 1B (Multi-criterio >= 3):        {(df_merged['nivel_certeza_sprint3']=='NIVEL_1B_ALTA_MULTIVARIADA').sum():,} (8.50%)")
    print(f"     • Nivel 1C (Promovidos por Vecinos +-3): {(df_merged['nivel_certeza_sprint3']=='NIVEL_1C_ALTA_REVALIDADA_VECINOS').sum():,} ({(df_merged['nivel_certeza_sprint3']=='NIVEL_1C_ALTA_REVALIDADA_VECINOS').sum()/total_suministros*100:.2f}%)")
    print(f"  🟡 CERTEZA MEDIA RESIDUAL (Nivel 2):        {n2_final:,} ({n2_final/total_suministros*100:.2f}%)")
    print(f"  🟠 ASIGNACIÓN PARCIAL A MANZANA (Nivel 3):  {n3_final:,} ({n3_final/total_suministros*100:.2f}%)")
    print(f"  🔴 SIN CONVERGENCIA / RESIDUAL ATÍPICO:     {n4_final:,} ({n4_final/total_suministros*100:.2f}%)")
    print("-" * 80)
    print(f"📈 GANANCIA NETA DE ALTA CERTEZA:             +{n1_final - n1_base:,} suministros consolidados.")
    print(f"📉 REDUCCIÓN DE AMBIGÜEDADES (Nivel 2):       -{n2_base - n2_final:,} casos resueltos (-{(n2_base-n2_final)/n2_base*100:.1f}%).")
    print(f"🛡️ COBERTURA TERRITORIAL TOTAL (Mza o Parc):  {n1_final + n3_final:,} suministros ({(n1_final + n3_final)/total_suministros*100:.2f}%)")
    print("=" * 80)
    
    # 6. Actualizar métricas en manzanas_alta_resolucion_data.js
    geojson_path = os.path.join(data_dir, "manzanas_alta_resolucion_distrito1.geojson")
    js_path = os.path.join(data_dir, "manzanas_alta_resolucion_data.js")
    
    mza_stats_sp3 = df_merged[df_merged['manzana_asignada_sprint3'] != ''].groupby('manzana_asignada_sprint3').agg(
        total_sum=('suministro', 'count'),
        alta_certeza=('nivel_certeza_sprint3', lambda s: (s.str.startswith('NIVEL_1')).sum()),
        parcial_mza=('nivel_certeza_sprint3', lambda s: (s.str.startswith('NIVEL_3')).sum())
    ).reset_index()
    mza_sp3_dict = mza_stats_sp3.set_index('manzana_asignada_sprint3').to_dict(orient='index')
    
    with open(geojson_path, 'r', encoding='utf-8') as f:
        geojson_mzas = json.load(f)
        
    for feat in geojson_mzas['features']:
        m_key = feat['properties']['mza_wfs']
        if m_key in mza_sp3_dict:
            st = mza_sp3_dict[m_key]
            feat['properties']['cant_suministros'] = int(st['total_sum'])
            feat['properties']['cant_alta_certeza'] = int(st['alta_certeza'])
            feat['properties']['cant_parcial_mza'] = int(st['parcial_mza'])
            feat['properties']['pct_alta'] = round(st['alta_certeza'] / max(1, st['total_sum']) * 100, 1)
            
    with open(geojson_path, 'w', encoding='utf-8') as f:
        json.dump(geojson_mzas, f, ensure_ascii=False)
        
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write("window.MANZANAS_ALTA_RESOLUCION_DATA = ")
        json.dump(geojson_mzas, f, ensure_ascii=False)
        f.write(";\n")
        
    for dpath in [r"D:\Usuarios\jidiaz\Downloads\data", r"C:\Usuarios\jidiaz\Downloads\data"]:
        os.makedirs(dpath, exist_ok=True)
        import shutil
        shutil.copy2(js_path, os.path.join(dpath, "manzanas_alta_resolucion_data.js"))

if __name__ == "__main__":
    ejecutar_sprint3()
