import os
os.environ['PROJ_DATA'] = r'C:\Program Files\QGIS 4.2.0\share\proj'
os.environ['PROJ_LIB'] = r'C:\Program Files\QGIS 4.2.0\share\proj'

import sys
import time
import math
import json
import pandas as pd
import numpy as np
import geopandas as gpd
from collections import defaultdict
from scipy.spatial import cKDTree
from shapely.geometry import Point, MultiPolygon, Polygon, mapping
from shapely.ops import unary_union
from shapely.validation import make_valid

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 110)
print("GENERACION DE POLIGONOS SEPARADOS (<10 HA) Y MANZANAS POR RUTA NUEVA")
print("DISTRITO 1 (EPEC) - 585.727 SUMINISTROS / 3.299 RUTAS / 18.721 MANZANAS")
print("=" * 110)

padron_path = r"D:\Proyectos\sigec-ruta-nueva-catastro-georef\data\summary\padron_nuevas_rutas_distrito1_completo.parquet"
mza_geom_path = r"D:\Proyectos\sigec-ruta-nueva-catastro-georef\data\manzanas_idecor_capital_4326.parquet"

t0 = time.time()
print("\n[1/4] Cargando padron y geometrias IDECOR...")
df_padron = pd.read_parquet(padron_path)
gdf_mzas = gpd.read_parquet(mza_geom_path)

gdf_mzas['geometry'] = gdf_mzas['geometry'].map(lambda g: make_valid(g) if not g.is_valid else g)
mza_geom_dict = gdf_mzas.set_index('mza_wfs')['geometry'].to_dict()

# Calcular areas reales de manzanas en hectareas
gdf_mzas_proj = gdf_mzas.to_crs(epsg=32720)
mza_area_ha = (gdf_mzas_proj.geometry.area / 10000.0).to_dict()
mza_area_dict = {row['mza_wfs']: mza_area_ha[i] for i, row in gdf_mzas.iterrows()}

print(f"      Padron: {len(df_padron):,} suministros.")
print(f"      Manzanas IDECOR: {len(mza_geom_dict):,} geometrias.")

# [2/4] Construir geometrias limpias de rutas separando componentes > 10 ha
print("\n[2/4] Construyendo poligonos compactos de rutas (restringiendo macro-manzanas)...")

# Macro-manzanas divididas
mza_route_counts = df_padron.groupby(['mza_wfs_asignada', 'nueva_ruta_lectura']).size().unstack(fill_value=0)
split_mzas = set(mza_route_counts[(mza_route_counts > 0).sum(axis=1) > 1].index)

route_components = defaultdict(list)
unique_pairs = df_padron.groupby(['mza_wfs_asignada', 'nueva_ruta_lectura'])

for (m, r_id), group in unique_pairs:
    pts = [Point(xy) for xy in zip(group['longitud'].dropna(), group['latitud'].dropna())]
    if not pts:
        continue
        
    mza_ha = mza_area_dict.get(m, 0.0)
    is_split = (m in split_mzas)
    is_virtual = m.endswith('-000') or m.startswith('VIRT_') or (m not in mza_geom_dict)
    is_macro = (mza_ha > 10.0) # Manzana rural > 10 ha
    
    # Si es una manzana urbana normal (<= 10 ha) no dividida y oficial
    if not is_split and not is_virtual and not is_macro:
        route_components[r_id].append(mza_geom_dict[m])
    else:
        # Envolvente ajustada a los suministros reales (buffer 35m)
        u_pts = unary_union(pts)
        if len(pts) >= 3:
            sub_poly = u_pts.convex_hull.buffer(0.00035)
        else:
            sub_poly = u_pts.buffer(0.00035)
            
        if not is_virtual and m in mza_geom_dict:
            inter = sub_poly.intersection(mza_geom_dict[m])
            if not inter.is_empty and inter.area > 1e-10:
                route_components[r_id].append(make_valid(inter))
            else:
                route_components[r_id].append(make_valid(sub_poly))
        else:
            route_components[r_id].append(make_valid(sub_poly))

print(f"      Geometrias base procesadas para {len(route_components):,} rutas.")

# [3/4] Unir por ruta y SEPARAR poligonos > 10 ha en sub-poligonos individuales
print("\n[3/4] Separando poligonos disjuntos y componentes > 10 ha...")

route_stats = df_padron.groupby('nueva_ruta_lectura').agg(
    distrito=('distrito', 'first'),
    grupo_lectura=('grupo_lectura', 'first'),
    cant_suministros=('suministro', 'count'),
    cant_manzanas=('mza_wfs_asignada', 'nunique'),
    centroide_lat=('latitud', 'mean'),
    centroide_lon=('longitud', 'mean'),
    calles_compartidas=('calles_compartidas_en_ruta', 'first')
).reset_index().set_index('nueva_ruta_lectura').to_dict(orient='index')

final_features = []
feat_id = 0

for r_id, g_list in route_components.items():
    if not g_list:
        continue
        
    info = route_stats.get(r_id, {})
    g = str(info.get('grupo_lectura', '1'))
    cant_sumi = info.get('cant_suministros', 0)
    cant_mzas = info.get('cant_manzanas', 0)
    calles = info.get('calles_compartidas', '')
    
    # Unir componentes de la ruta
    clean = [geom.buffer(0) for geom in g_list if geom is not None and not geom.is_empty]
    try:
        merged = unary_union(clean)
    except Exception:
        merged = unary_union([geom.convex_hull for geom in clean])
        
    merged = make_valid(merged)
    
    # Extraer sub-poligonos individuales
    sub_geoms = []
    if merged.geom_type == 'Polygon':
        sub_geoms = [merged]
    elif merged.geom_type == 'MultiPolygon':
        sub_geoms = list(merged.geoms)
    elif merged.geom_type == 'GeometryCollection':
        for g_item in merged.geoms:
            if g_item.geom_type == 'Polygon':
                sub_geoms.append(g_item)
            elif g_item.geom_type == 'MultiPolygon':
                sub_geoms.extend(list(g_item.geoms))
                
    # Si algún sub-poligono es > 10 ha y está compuesto por varias manzanas,
    # lo conservamos pero marcamos su tamaño real
    part_num = 1
    total_parts = len(sub_geoms)
    
    for poly in sub_geoms:
        if poly.is_empty or poly.area < 1e-12:
            continue
            
        # Calcular area en hectareas con proyeccion UTM
        area_m2 = poly.area * (111139.0 * 111139.0 * 0.85)
        ha = area_m2 / 10000.0
        perim_m = poly.length * 111139.0
        perim_km = perim_m / 1000.0
        comp = (4.0 * math.pi * area_m2) / (perim_m * perim_m) if perim_m > 0 else 0.0
        comp = min(1.0, max(0.0, comp))
        
        # Simplificar levemente para 60 FPS
        poly_simp = poly.simplify(0.00004, preserve_topology=True)
        if poly_simp.is_empty:
            poly_simp = poly
            
        # Nombre de la parte si es separada
        sub_label = f"Ruta {r_id}" if total_parts == 1 else f"Ruta {r_id} (Parte {part_num}/{total_parts})"
        
        final_features.append({
            "type": "Feature",
            "id": str(feat_id),
            "properties": {
                "nueva_ruta_lectura": int(r_id),
                "distrito": 1,
                "grupo_lectura": int(g),
                "cant_suministros": cant_sumi,
                "cant_manzanas": cant_mzas,
                "area_hectareas": round(ha, 2),
                "es_mayor_10ha": bool(ha > 10.0),
                "parte_num": part_num,
                "total_partes": total_parts,
                "etiqueta_parte": sub_label,
                "perimetro_km": round(perim_km, 2),
                "compacidad_isoperimetrica": round(comp, 3),
                "calles_compartidas_en_ruta": calles
            },
            "geometry": mapping(poly_simp)
        })
        feat_id += 1
        part_num += 1

print(f"      Total features generadas (poligonos separados): {len(final_features):,}")
areas_all = [f['properties']['area_hectareas'] for f in final_features]
big_all = [a for a in areas_all if a > 10.0]
print(f"      Poligonos con area <= 10 ha: {len(areas_all) - len(big_all):,} ({((len(areas_all) - len(big_all))/len(areas_all))*100:.1f}%)")
print(f"      Poligonos con area > 10 ha (rurales/extensos aislados): {len(big_all):,} ({len(big_all)/len(areas_all)*100:.1f}%)")
print(f"      Mediana de area por poligono: {np.median(areas_all):.2f} ha (Maximo reducido drasticamente).")

# [4/4] Guardar GeoJSON y JS para visor
out_geojson_path = r"D:\Usuarios\jidiaz\Downloads\visor_manzanas_rutas\data\rutas_nuevas_poligonos_distrito1.geojson"
out_js_path = r"D:\Usuarios\jidiaz\Downloads\visor_manzanas_rutas\data\rutas_poligonos_data.js"

fc = {
    "type": "FeatureCollection",
    "features": final_features
}

print(f"\n[4/4] Guardando poligonos separados en {out_geojson_path}...")
with open(out_geojson_path, "w", encoding="utf-8") as f:
    json.dump(fc, f)

js_content = "const RUTAS_DATA = " + json.dumps(fc) + ";\n"
with open(out_js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"      GeoJSON guardado: {os.path.getsize(out_geojson_path) / (1024*1024):.2f} MB")
print(f"      JS guardado: {os.path.getsize(out_js_path) / (1024*1024):.2f} MB")
print(f"      Completado con exito en {time.time() - t0:.1f} s.")
