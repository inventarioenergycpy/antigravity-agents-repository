# -*- coding: utf-8 -*-
import os, sys, json, time, glob, re

proj_dir = r"C:\Program Files\QGIS 4.2.0\share\proj"
os.environ['PROJ_DATA'] = proj_dir
os.environ['PROJ_LIB'] = proj_dir

import pyproj
try:
    pyproj.datadir.set_data_dir(proj_dir)
except Exception:
    pass

from shapely.geometry import shape, mapping
from shapely.ops import unary_union, transform
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

transformer_to_wgs84 = pyproj.Transformer.from_crs("EPSG:22174", "EPSG:4326", always_xy=True).transform

data_dir = r"D:\Proyectos\antigravity-agents-repository\data"
cache_dir = os.path.join(data_dir, "cache_parcelas_wfs")
out_mzas_dir = os.path.join(data_dir, "manzanas_por_circ")
os.makedirs(out_mzas_dir, exist_ok=True)

DEPTO_NOMBRES = {
    "11": "Capital",
    "13": "Colón",
    "16": "Cruz del Eje",
    "23": "Punilla",
    "24": "Río Cuarto",
    "25": "Río Primero",
    "27": "San Justo",
    "30": "Santa María",
    "31": "Tercero Arriba"
}

def procesar_sintesis_provincial():
    print("=" * 80)
    print("🚀 RECOMPOSICIÓN DE MANZANAS DE ALTA RESOLUCIÓN A ESCALA PROVINCIAL")
    print("=" * 80)
    
    t0 = time.time()
    chunk_files = glob.glob(os.path.join(cache_dir, "*.json"))
    print(f"Total archivos de chunks en cache local: {len(chunk_files):,}")
    
    # 1. Agrupar parcelas por clave de Manzana y por Jurisdicción
    print("\n📦 Cargando y agrupando parcelas desde chunks locales...")
    partitions = {} # key: "11_C01", "13_P01", etc.
    total_parc_features = 0
    unique_parcels_set = set()
    
    for fpath in chunk_files:
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                cdata = json.load(f)
        except Exception:
            continue
            
        if isinstance(cdata, dict):
            feats = cdata.get('features', [])
        elif isinstance(cdata, list):
            feats = cdata
        else:
            feats = []
            
        for feat in feats:
            total_parc_features += 1
            props = feat.get('properties', {})
            geom_raw = feat.get('geometry')
            if not geom_raw:
                continue
                
            nom = (props.get('nomenclatura') or '').strip()
            if not nom:
                continue
                
            tokens = nom.split('-')
            if len(tokens) < 6:
                continue
                
            depto = tokens[0]
            mza_key = "-".join(tokens[:6])
            
            # Determinar partición operativa
            if depto == '11':
                circ = tokens[3] if len(tokens) > 3 else "00"
                part_id = f"11_C{circ}"
            else:
                ped = tokens[1] if len(tokens) > 1 else "00"
                part_id = f"{depto}_P{ped}"
                
            if part_id not in partitions:
                partitions[part_id] = {}
                
            if mza_key not in partitions[part_id]:
                partitions[part_id][mza_key] = {}
                
            calle = (props.get('nombrecall') or '').strip()
            nrocasa = (props.get('nrocasa') or '').strip()
            
            if nom not in partitions[part_id][mza_key]:
                unique_parcels_set.add(nom)
                try:
                    poly = shape(geom_raw)
                    if poly.is_valid and not poly.is_empty:
                        partitions[part_id][mza_key][nom] = {
                            "geom": poly,
                            "calles": set([calle] if calle else []),
                            "nros": [int(nrocasa)] if nrocasa.isdigit() else []
                        }
                except Exception:
                    pass
            else:
                if calle:
                    partitions[part_id][mza_key][nom]["calles"].add(calle)
                if nrocasa.isdigit():
                    partitions[part_id][mza_key][nom]["nros"].append(int(nrocasa))

    print(f"✅ Total registros de parcelas evaluados: {total_parc_features:,}")
    print(f"✅ Total parcelas físicas únicas consolidadas: {len(unique_parcels_set):,}")
    print(f"✅ Total particiones operativas identificadas: {len(partitions):,}")

    # 2. Sintetizar Manzanas por cada Partición y exportar
    print("\n⚙️ Disolviendo topológicamente y sintetizando Manzanas Sintéticas...")
    cat_jerarquico = {} # Depto -> Circ/Ped -> stats
    resumen_particiones = []
    total_mzas_prov = 0
    mzas_master_rows = []
    
    for part_id in sorted(partitions.keys()):
        mzas_dict = partitions[part_id]
        if not mzas_dict:
            continue
            
        depto_id = part_id.split('_')[0]
        sub_id = part_id.split('_')[1] # C01 o P01
        depto_nombre = DEPTO_NOMBRES.get(depto_id, f"Depto {depto_id}")
        
        if depto_id not in cat_jerarquico:
            cat_jerarquico[depto_id] = {
                "nombre": depto_nombre,
                "subdivisiones": {}
            }
            
        part_features = []
        part_parc_cnt = 0
        
        for mza_key, parc_dict in mzas_dict.items():
            if not parc_dict:
                continue
                
            polys = [p["geom"] for p in parc_dict.values()]
            if not polys:
                continue
                
            try:
                mza_poly = unary_union(polys)
                if mza_poly.is_empty:
                    continue
                    
                area_m2 = mza_poly.area
                area_ha = area_m2 / 10000.0
                perim_m = mza_poly.length
                
                # Consolidar calles perimetrales
                all_calles = set()
                all_nros = []
                for p in parc_dict.values():
                    all_calles.update(p["calles"])
                    all_nros.extend(p["nros"])
                    
                calles_str = ", ".join(sorted(all_calles)) if all_calles else "S/D"
                rango_alt = f"{min(all_nros)}-{max(all_nros)}" if all_nros else "S/D"
                
                # Reproyectar a WGS84 para visualización
                mza_wgs84 = transform(transformer_to_wgs84, mza_poly)
                center_pt = mza_wgs84.centroid
                
                feat = {
                    "type": "Feature",
                    "properties": {
                        "mza_wfs": mza_key,
                        "depto": depto_id,
                        "particion": part_id,
                        "cant_parcelas": len(parc_dict),
                        "area_ha": round(area_ha, 4),
                        "perimetro_m": round(perim_m, 2),
                        "calles_perimetrales": calles_str,
                        "rango_alturas": rango_alt
                    },
                    "geometry": mapping(mza_wgs84)
                }
                part_features.append(feat)
                part_parc_cnt += len(parc_dict)
                total_mzas_prov += 1
                
                mzas_master_rows.append({
                    "mza_wfs": mza_key,
                    "depto": depto_id,
                    "particion": part_id,
                    "cant_parcelas": len(parc_dict),
                    "area_ha": round(area_ha, 4),
                    "perimetro_m": round(perim_m, 2),
                    "calles_perimetrales": calles_str,
                    "centro_lat": round(center_pt.y, 6),
                    "centro_lon": round(center_pt.x, 6)
                })
            except Exception:
                continue

        # Exportar GeoJSON de la partición para carga diferida en el visor
        part_geojson_path = os.path.join(out_mzas_dir, f"mzas_{part_id}.geojson")
        with open(part_geojson_path, 'w', encoding='utf-8') as f:
            json.dump({"type": "FeatureCollection", "features": part_features}, f)
            
        cat_jerarquico[depto_id]["subdivisiones"][sub_id] = {
            "part_id": part_id,
            "cant_manzanas": len(part_features),
            "cant_parcelas": part_parc_cnt,
            "geojson_file": f"mzas_{part_id}.geojson"
        }
        
        resumen_particiones.append({
            "particion": part_id,
            "depto": depto_nombre,
            "manzanas": len(part_features),
            "parcelas": part_parc_cnt
        })

    print(f"\n✅ RECOMPOSICIÓN COMPLETADA:")
    print(f"  Total Manzanas Sintéticas sintetizadas: {total_mzas_prov:,}")
    print(f"  Total Particiones guardadas: {len(resumen_particiones)}")
    
    # 3. Guardar catálogo jerárquico y tabla master Parquet
    cat_path = os.path.join(data_dir, "catalogo_jerarquico_provincial.json")
    with open(cat_path, 'w', encoding='utf-8') as f:
        json.dump(cat_jerarquico, f, indent=2)
    print(f"Catálogo jerárquico guardado en: {cat_path}")
    
    df_master = pd.DataFrame(mzas_master_rows)
    master_parquet = os.path.join(data_dir, "manzanas_alta_resolucion_provincial.parquet")
    df_master.to_parquet(master_parquet, index=False, engine='pyarrow')
    print(f"Tabla Master Parquet guardada en: {master_parquet} ({len(df_master):,} filas)")
    print(f"Tiempo total de síntesis: {time.time()-t0:.2f} segundos.")

if __name__ == "__main__":
    procesar_sintesis_provincial()
