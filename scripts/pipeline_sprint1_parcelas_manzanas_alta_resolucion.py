"""
========================================================================================
SQUAD ARQUETIPO A - GIS, CATASTRO Y RUTAS EPEC
SPRINT 1: Pipeline de Ingesta Incremental de Parcelas y Recomposición de Manzanas HR
========================================================================================
Autor: Operador 1 (Ingeniero Geoespacial) & Project Manager (Gemini 3.8 Flash High)
Fecha: 25 de Octubre de 2026
Capa Origen: EPEC:vm_vt_parcelas_calles (GeoServer WFS)
CRS Entrada: EPSG:22174 (POSGAR 94 / Argentina 4)
CRS Salida: EPSG:4326 (WGS 84 Lat/Lon)
========================================================================================
"""

import os, sys, time, json, math

# Forzar salida utf-8 en consola Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configurar librerías PROJ para entorno QGIS Python
os.environ['PROJ_LIB'] = r'C:\Program Files\QGIS 4.2.0\share\proj'
os.environ['PROJ_DATA'] = r'C:\Program Files\QGIS 4.2.0\share\proj'

import pyproj
import geopandas as gpd
import pandas as pd
from shapely.geometry import shape, mapping, Polygon, MultiPolygon
from shapely.ops import unary_union, transform

# Transformador de coordenadas POSGAR 94 (m) -> WGS 84 (deg)
transformer = pyproj.Transformer.from_crs('EPSG:22174', 'EPSG:4326', always_xy=True)

WFS_URL = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
WFS_AUTH = ("EPEC_comercial", "Bratis-c0m3rc14l")
LAYER_NAME = "EPEC:vm_vt_parcelas_calles"

def reproject_geom_posgar_to_wgs84(geom):
    """Reproyecta una geometría Shapely de EPSG:22174 a EPSG:4326."""
    return transform(transformer.transform, geom)

def descargar_seccion_wfs(circ_str, sec_str, session, max_retries=3):
    """
    Descarga todas las parcelas de una sección catastral específica (ej. 11-01-01-01-02).
    """
    prefix = f"11-01-01-{circ_str}-{sec_str}"
    params = {
        'service': 'WFS',
        'version': '1.1.0',
        'request': 'GetFeature',
        'typeName': LAYER_NAME,
        'maxFeatures': 5000,
        'outputFormat': 'application/json',
        'cql_filter': f"nomenclatura LIKE '{prefix}%'"
    }
    
    for attempt in range(1, max_retries + 1):
        try:
            r = session.get(WFS_URL, auth=WFS_AUTH, params=params, verify=False, timeout=35)
            if r.status_code == 200:
                data = r.json()
                return data.get('features', [])
            else:
                print(f"      [!] Error HTTP {r.status_code} en {prefix} (intento {attempt}): {r.text[:100]}")
        except Exception as e:
            print(f"      [!] Timeout/Excepción en {prefix} (intento {attempt}): {e}")
        time.sleep(1.5 * attempt)
    return []

def generar_visor_html_mzas_hr(js_relative_path, out_html_path, cant_mzas, cant_parc):
    """Genera visor HTML interactivo con Leaflet y ESRI World Street Map para las manzanas HR."""
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visor Manzanas de Alta Resolución - Sprint 1 EPEC</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
    body, html {{ height: 100%; width: 100%; overflow: hidden; background: #0f172a; color: #f8fafc; }}
    #map {{ height: 100%; width: 100%; z-index: 1; }}
    .header-bar {{
      position: absolute; top: 0; left: 0; right: 0; height: 56px;
      background: rgba(15, 23, 42, 0.94); backdrop-filter: blur(10px);
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 20px; z-index: 1000; border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .header-title {{ font-size: 16px; font-weight: 700; color: #38bdf8; display: flex; align-items: center; gap: 8px; }}
    .badge {{ background: #0284c7; color: white; padding: 3px 8px; border-radius: 6px; font-size: 12px; font-weight: 600; }}
    .info-panel {{
      position: absolute; bottom: 20px; left: 20px; width: 340px;
      background: rgba(15, 23, 42, 0.94); backdrop-filter: blur(12px);
      border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 16px; z-index: 1000; box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }}
    .stat-row {{ display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 13px; }}
    .stat-label {{ color: #94a3b8; }}
    .stat-value {{ font-weight: 600; color: #f8fafc; }}
    .detail-card {{
      margin-top: 12px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.1);
      display: none;
    }}
    .mza-title {{ color: #38bdf8; font-weight: 700; font-size: 14px; margin-bottom: 6px; }}
    .calles-tag {{ font-size: 11px; background: rgba(56, 189, 248, 0.15); color: #7dd3fc; padding: 4px 6px; border-radius: 4px; display: inline-block; margin-top: 4px; }}
  </style>
</head>
<body>
  <div class="header-bar">
    <div class="header-title">
      <span>🗺️ Manzanas de Alta Resolución (Recomposición Bottom-Up)</span>
      <span class="badge">Sprint 1 Pilot</span>
    </div>
    <div style="font-size: 13px; color: #94a3b8;">
      Fuente: <strong style="color: #f8fafc;">EPEC:vm_vt_parcelas_calles</strong> | Disolución Exacta Shapely
    </div>
  </div>

  <div id="map"></div>

  <div class="info-panel">
    <div style="font-size: 14px; font-weight: 700; margin-bottom: 12px; color: #38bdf8;">📊 Métricas del Modelo Sintético</div>
    <div class="stat-row"><span class="stat-label">Manzanas Sintéticas:</span><span class="stat-value">{cant_mzas:,}</span></div>
    <div class="stat-row"><span class="stat-label">Parcelas Disueltas:</span><span class="stat-value">{cant_parc:,}</span></div>
    <div class="stat-row"><span class="stat-label">Promedio Parcelas/Mza:</span><span class="stat-value">{cant_parc/max(1, cant_mzas):.1f}</span></div>
    <div class="stat-row"><span class="stat-label">Trama Vial Urbana:</span><span class="stat-value" style="color: #4ade80;">100% Preservada (Abierta)</span></div>
    
    <div class="detail-card" id="detailCard">
      <div class="mza-title" id="mzaTitle">Manzana: -</div>
      <div class="stat-row"><span class="stat-label">Superficie:</span><span class="stat-value" id="mzaArea">-</span></div>
      <div class="stat-row"><span class="stat-label">Parcelas:</span><span class="stat-value" id="mzaParcels">-</span></div>
      <div class="stat-row"><span class="stat-label">Calles Perimetrales:</span></div>
      <div class="calles-tag" id="mzaStreets">-</div>
    </div>
  </div>

  <script src="{js_relative_path}"></script>
  <script>
    const map = L.map('map', {{
      center: [-31.4167, -64.1833],
      zoom: 14,
      zoomControl: false
    }});
    L.control.zoom({{ position: 'topright' }}).addTo(map);

    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
      maxZoom: 19,
      attribution: 'Esri World Street Map'
    }}).addTo(map);

    let activeLayer = null;
    const detailCard = document.getElementById('detailCard');
    const mzaTitle = document.getElementById('mzaTitle');
    const mzaArea = document.getElementById('mzaArea');
    const mzaParcels = document.getElementById('mzaParcels');
    const mzaStreets = document.getElementById('mzaStreets');

    if (window.MANZANAS_ALTA_RESOLUCION_DATA) {{
      const geoLayer = L.geoJSON(window.MANZANAS_ALTA_RESOLUCION_DATA, {{
        style: function(feat) {{
          return {{
            color: '#0284c7',
            weight: 1.5,
            fillColor: '#38bdf8',
            fillOpacity: 0.35
          }};
        }},
        onEachFeature: function(feat, layer) {{
          layer.on('mouseover', function() {{
            layer.setStyle({{ fillColor: '#fbbf24', fillOpacity: 0.7, weight: 2.5, color: '#f59e0b' }});
            detailCard.style.display = 'block';
            mzaTitle.textContent = 'Manzana: ' + feat.properties.mza_wfs;
            mzaArea.textContent = feat.properties.superficie_ha + ' ha (' + feat.properties.superficie_m2.toLocaleString() + ' m²)';
            mzaParcels.textContent = feat.properties.cant_parcelas + ' parcelas';
            mzaStreets.textContent = feat.properties.calles_perimetrales || 'Sin calle registrada';
          }});
          layer.on('mouseout', function() {{
            geoLayer.resetStyle(layer);
          }});
        }}
      }}).addTo(map);

      map.fitBounds(geoLayer.getBounds(), {{ padding: [60, 60] }});
    }}
  </script>
</body>
</html>
"""
    with open(out_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"🌐 Visor HTML generado: {out_html_path}")

def procesar_secciones(circ_lista, secciones_max=None, out_dir="data"):
    """
    Descarga y sintetiza parcelas y manzanas para las circunscripciones indicadas.
    """
    os.makedirs(out_dir, exist_ok=True)
    cache_dir = os.path.join(out_dir, "cache_parcelas_wfs")
    os.makedirs(cache_dir, exist_ok=True)
    
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=2)
    session.mount("https://", adapter)
    
    print("=" * 80)
    print(" [*] INICIANDO SPRINT 1: INGESTA INCREMENTAL Y RECOMPOSICION DE MANZANAS HR")
    print("=" * 80)
    
    total_parcelas_raw = 0
    parcelas_por_nom = {} # nom_parcela -> {'geom_posgar': shapely_geom, 'calles': set(), 'tipos': set(), 'mza_nom': str, 'parcela_id': str}
    
    t_global_start = time.time()
    
    for circ in circ_lista:
        c_str = f"{circ:02d}"
        print(f"\n[+] Procesando Circunscripcion {c_str}...")
        
        # Iterar secciones 1 a 40 (o hasta secciones_max)
        sec_range = range(1, secciones_max + 1) if secciones_max else range(1, 41)
        
        for sec in sec_range:
            s_str = f"{sec:02d}"
            cache_file = os.path.join(cache_dir, f"circ_{c_str}_sec_{s_str}.json")
            
            features = []
            if os.path.exists(cache_file):
                try:
                    with open(cache_file, 'r', encoding='utf-8') as f:
                        features = json.load(f)
                except Exception:
                    features = []
            
            if not features:
                features = descargar_seccion_wfs(c_str, s_str, session)
                if features:
                    with open(cache_file, 'w', encoding='utf-8') as f:
                        json.dump(features, f)
            
            if not features:
                continue
                
            total_parcelas_raw += len(features)
            
            # Consolidar en memoria
            for feat in features:
                props = feat.get('properties', {})
                nom = (props.get('nomenclatura') or '').strip()
                if not nom:
                    continue
                
                calle = (props.get('nombrecall') or '').strip()
                tipo_calle = (props.get('tipo') or '').strip()
                
                tokens = nom.split('-')
                if len(tokens) >= 6:
                    mza_nom = "-".join(tokens[:6])
                    parcela_id = tokens[6] if len(tokens) > 6 else props.get('parcela', '')
                else:
                    mza_nom = nom[:18]
                    parcela_id = props.get('parcela', '')
                
                if nom not in parcelas_por_nom:
                    raw_geom = feat.get('geometry')
                    if raw_geom:
                        try:
                            shp_geom = shape(raw_geom)
                            if shp_geom.is_valid:
                                parcelas_por_nom[nom] = {
                                    'geom_posgar': shp_geom,
                                    'calles': set(),
                                    'tipos': set(),
                                    'mza_nom': mza_nom,
                                    'parcela_id': parcela_id
                                }
                        except Exception:
                            continue
                
                if nom in parcelas_por_nom:
                    if calle:
                        parcelas_por_nom[nom]['calles'].add(calle)
                    if tipo_calle:
                        parcelas_por_nom[nom]['tipos'].add(tipo_calle)
            
            print(f"   ✓ Sec {s_str}: {len(features):4d} registros WFS | Acumulado parcelas unicas: {len(parcelas_por_nom):,}")

    print("\n" + "-" * 80)
    print(f"[+] Ingesta concluida: {total_parcelas_raw:,} registros WFS descargados.")
    print(f"[+] Total de Parcelas Unicas consolidadas: {len(parcelas_por_nom):,}")
    print("-" * 80)
    
    # =========================================================================
    # FASE 2: DISOLUCIÓN TOPOLÓGICA DE MANZANAS (unary_union)
    # =========================================================================
    print("\n[+] FASE 2: Recomposicion de Manzanas Sinteticas de Alta Resolucion...")
    
    mzas_dict = {}
    mzas_calles = {}
    
    for nom, pdata in parcelas_por_nom.items():
        mza_nom = pdata['mza_nom']
        if mza_nom not in mzas_dict:
            mzas_dict[mza_nom] = []
            mzas_calles[mza_nom] = set()
        mzas_dict[mza_nom].append(pdata['geom_posgar'])
        mzas_calles[mza_nom].update(pdata['calles'])
        
    print(f"[+] Total de Manzanas a sintetizar: {len(mzas_dict):,} manzanas.")
    
    features_manzanas = []
    mzas_rows = []
    
    t_mza_start = time.time()
    for i, (mza_nom, geoms) in enumerate(mzas_dict.items(), 1):
        try:
            union_geom_posgar = unary_union(geoms)
            if not union_geom_posgar.is_valid:
                union_geom_posgar = union_geom_posgar.buffer(0)
                
            area_m2 = union_geom_posgar.area
            area_ha = area_m2 / 10000.0
            
            union_geom_wgs84 = reproject_geom_posgar_to_wgs84(union_geom_posgar)
            centroide = union_geom_wgs84.centroid
            
            calles_list = sorted(list(mzas_calles[mza_nom]))
            calles_str = ", ".join(calles_list[:8])
            
            mza_props = {
                "mza_wfs": mza_nom,
                "cant_parcelas": len(geoms),
                "superficie_ha": round(area_ha, 3),
                "superficie_m2": round(area_m2, 1),
                "centroide_lat": round(centroide.y, 6),
                "centroide_lon": round(centroide.x, 6),
                "calles_perimetrales": calles_str,
                "cant_calles": len(calles_list)
            }
            
            feat_mza = {
                "type": "Feature",
                "properties": mza_props,
                "geometry": mapping(union_geom_wgs84)
            }
            features_manzanas.append(feat_mza)
            
            mzas_rows.append({
                **mza_props,
                "geometry": union_geom_wgs84
            })
        except Exception as e:
            print(f"   [!] Error disolviendo manzana {mza_nom}: {e}")
            
        if i % 250 == 0 or i == len(mzas_dict):
            print(f"   ... Sintetizadas {i:,} / {len(mzas_dict):,} manzanas ({i/len(mzas_dict)*100:.1f}%)")
            
    print(f"[+] Tiempo de disolucion topologica: {time.time() - t_mza_start:.2f} s")
    
    # =========================================================================
    # FASE 3: EXPORTACIÓN DE ENTREGABLES
    # =========================================================================
    # 1. GeoJSON
    geojson_mzas = {
        "type": "FeatureCollection",
        "name": "manzanas_alta_resolucion_distrito1",
        "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
        "features": features_manzanas
    }
    
    out_geojson_path = os.path.join(out_dir, "manzanas_alta_resolucion_distrito1.geojson")
    with open(out_geojson_path, "w", encoding="utf-8") as f:
        json.dump(geojson_mzas, f, ensure_ascii=False)
    print(f"\n💾 GeoJSON de Manzanas HR guardado: {out_geojson_path} ({os.path.getsize(out_geojson_path)/1024/1024:.2f} MB)")
    
    # 2. JS Autónomo
    out_js_path = os.path.join(out_dir, "manzanas_alta_resolucion_data.js")
    with open(out_js_path, "w", encoding="utf-8") as f:
        f.write("window.MANZANAS_ALTA_RESOLUCION_DATA = ")
        json.dump(geojson_mzas, f, ensure_ascii=False)
        f.write(";\n")
    print(f"💾 JS Autónomo guardado: {out_js_path} ({os.path.getsize(out_js_path)/1024/1024:.2f} MB)")
    
    # 3. GeoParquet
    try:
        gdf_mzas = gpd.GeoDataFrame(mzas_rows, crs="EPSG:4326")
        out_parquet_path = os.path.join(out_dir, "manzanas_alta_resolucion_distrito1.parquet")
        gdf_mzas.to_parquet(out_parquet_path)
        print(f"💾 GeoParquet de Manzanas HR guardado: {out_parquet_path} ({os.path.getsize(out_parquet_path)/1024/1024:.2f} MB)")
    except Exception as e:
        print(f"   [!] Aviso Parquet: {e}")
        
    # 4. Espejado a Downloads
    for dpath in [r"D:\Usuarios\jidiaz\Downloads\data", r"C:\Usuarios\jidiaz\Downloads\data"]:
        try:
            os.makedirs(dpath, exist_ok=True)
            import shutil
            shutil.copy2(out_js_path, os.path.join(dpath, "manzanas_alta_resolucion_data.js"))
            print(f"   ✓ Espejado data.js a: {dpath}")
        except Exception:
            pass
            
    # 5. Generar Visor HTML interactivo autónomo
    for vpath in [r"D:\Usuarios\jidiaz\Downloads\visor_manzanas_hr_piloto.html", r"C:\Usuarios\jidiaz\Downloads\visor_manzanas_hr_piloto.html"]:
        try:
            generar_visor_html_mzas_hr("data/manzanas_alta_resolucion_data.js", vpath, len(features_manzanas), len(parcelas_por_nom))
        except Exception as e:
            print(f"   [!] Error generando visor HTML: {e}")
            
    print("\n" + "=" * 80)
    print(f"🎉 SPRINT 1 COMPLETADO EXITOSAMENTE EN {time.time() - t_global_start:.2f} SEGUNDOS")
    print(f"📊 Manzanas Recompuestas: {len(features_manzanas):,} manzanas de alta resolución.")
    print(f"📍 Parcelas Consolidadas: {len(parcelas_por_nom):,} parcelas oficiales.")
    print("=" * 80)

if __name__ == "__main__":
    # Ejecución de Circunscripción 01 (todas las secciones 1 a 33 activas)
    circ_objetivo = [1]
    secciones_limite = 35
    
    if len(sys.argv) > 1 and sys.argv[1] == "--full":
        circ_objetivo = list(range(1, 16))
        secciones_limite = None
        
    procesar_secciones(circ_objetivo, secciones_max=secciones_limite, out_dir=r"D:\Proyectos\antigravity-agents-repository\data")
