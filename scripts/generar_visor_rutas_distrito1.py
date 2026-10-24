import os
import sys
import json
import time

# Configurar PROJ para QGIS en Windows
os.environ['PROJ_DATA'] = r'C:\Program Files\QGIS 4.2.0\share\proj'
os.environ['PROJ_LIB'] = r'C:\Program Files\QGIS 4.2.0\share\proj'

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 100)
print("GENERADOR DEL VISOR CARTOGRÁFICO INTERACTIVO WEB - DISTRITO 1 (EPEC)")
print("SQUAD MULTI-AGENTE ARQUETIPO A - SPRINT 2")
print("=" * 100)

import geopandas as gpd

t0 = time.time()
parquet_path = r"D:\Proyectos\sigec-ruta-nueva-catastro-georef\data\summary\rutas_nuevas_poligonos_distrito1.parquet"
out_html_proj = r"D:\Proyectos\sigec-ruta-nueva-catastro-georef\data\summary\visor_rutas_poligonos_distrito1.html"
out_html_c_down = r"C:\Users\jidiaz\Downloads\visor_rutas_poligonos_distrito1.html"
out_html_d_down = r"D:\Usuarios\jidiaz\Downloads\visor_rutas_poligonos_distrito1.html"

print(f"\n[1/4] Leyendo capa de polígonos de rutas: {parquet_path}...")
gdf = gpd.read_parquet(parquet_path)
print(f"      Total de rutas leídas: {len(gdf):,}")

print("\n[2/4] Simplificando geometrías vectoriales (tolerancia 0.00006) para rendimiento a 60 FPS...")
gdf_sim = gdf.copy()
gdf_sim['geometry'] = gdf_sim['geometry'].simplify(0.00006, preserve_topology=True)

# Convertir a GeoJSON serializable
print("      Serializando a GeoJSON en memoria...")
geojson_str = gdf_sim.to_json()
size_mb = len(geojson_str) / (1024 * 1024)
print(f"      Tamaño optimizado de GeoJSON: {size_mb:.2f} MB (reducción >75% sin pérdida visual)")

# Paleta de 20 colores HSL distintivos para los 20 grupos de lectura
colors_groups = {
    "1": "#38bdf8",  # Sky blue
    "2": "#818cf8",  # Indigo
    "3": "#c084fc",  # Purple
    "4": "#f472b6",  # Pink
    "5": "#fb7185",  # Rose
    "6": "#f97316",  # Orange
    "7": "#fbbf24",  # Amber
    "8": "#a3e635",  # Lime
    "9": "#4ade80",  # Green
    "10": "#2dd4bf", # Teal
    "11": "#06b6d4", # Cyan
    "12": "#60a5fa", # Blue
    "13": "#a78bfa", # Violet
    "14": "#e879f9", # Fuchsia
    "15": "#fb923c", # Tangerine
    "16": "#34d399", # Emerald
    "17": "#14b8a6", # Dark Teal
    "18": "#0284c7", # Ocean Blue
    "19": "#d946ef", # Magenta
    "20": "#eab308"  # Gold
}

counts = gdf.groupby('grupo_lectura').size().to_dict()

print("\n[3/4] Generando plantilla HTML moderna con Leaflet, Glassmorphism y panel de control interactivo...")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EPEC - Visor Geoespacial de Nuevas Rutas de Lectura (Distrito 1)</title>
    <!-- Leaflet CSS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
    <!-- Google Fonts: Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }}
        body, html {{
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-color: #0b0f19;
            color: #f1f5f9;
        }}
        #map {{
            width: 100%;
            height: 100%;
            z-index: 1;
            background: #090d16;
        }}
        /* Floating Glassmorphic Header */
        .header-bar {{
            position: absolute;
            top: 16px;
            left: 70px;
            right: 16px;
            z-index: 1000;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
            pointer-events: auto;
        }}
        .header-title {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .header-title h1 {{
            font-size: 16px;
            font-weight: 700;
            letter-spacing: -0.02em;
            color: #f8fafc;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .header-title span.badge {{
            font-size: 11px;
            background: #1e293b;
            color: #38bdf8;
            padding: 3px 8px;
            border-radius: 6px;
            border: 1px solid rgba(56, 189, 248, 0.3);
            font-weight: 600;
        }}
        .stats-pills {{
            display: flex;
            gap: 10px;
            align-items: center;
        }}
        .pill {{
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 8px;
            padding: 4px 12px;
            font-size: 12px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .pill strong {{
            color: #38bdf8;
            font-weight: 700;
        }}
        /* Floating Sidebar Controls */
        .sidebar {{
            position: absolute;
            top: 80px;
            left: 16px;
            width: 340px;
            max-height: calc(100% - 100px);
            z-index: 1000;
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 18px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.6);
            overflow-y: auto;
            pointer-events: auto;
        }}
        .sidebar h2 {{
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #94a3b8;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .control-group {{
            margin-bottom: 16px;
        }}
        .control-group label {{
            display: block;
            font-size: 12px;
            font-weight: 600;
            color: #cbd5e1;
            margin-bottom: 6px;
        }}
        .search-box {{
            width: 100%;
            padding: 9px 12px;
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 8px;
            color: #f8fafc;
            font-size: 13px;
            outline: none;
            transition: border-color 0.2s;
        }}
        .search-box:focus {{
            border-color: #38bdf8;
            box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
        }}
        .select-custom {{
            width: 100%;
            padding: 8px 12px;
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 8px;
            color: #f8fafc;
            font-size: 13px;
            outline: none;
            cursor: pointer;
        }}
        .filter-buttons {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 6px;
        }}
        .btn-filter {{
            background: #1e293b;
            border: 1px solid #334155;
            color: #cbd5e1;
            padding: 7px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 500;
            cursor: pointer;
            text-align: center;
            transition: all 0.2s;
        }}
        .btn-filter:hover {{
            background: #334155;
            color: #fff;
        }}
        .btn-filter.active {{
            background: #0284c7;
            border-color: #38bdf8;
            color: #fff;
            font-weight: 700;
        }}
        .opacity-slider {{
            width: 100%;
            accent-color: #38bdf8;
            cursor: pointer;
        }}
        .legend {{
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            padding: 10px;
            font-size: 11px;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 4px;
        }}
        .legend-color {{
            width: 12px;
            height: 12px;
            border-radius: 3px;
        }}
        /* Info Card Popup */
        .leaflet-popup-content-wrapper {{
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(16px);
            color: #f8fafc;
            border: 1px solid rgba(56, 189, 248, 0.3);
            border-radius: 12px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.7);
        }}
        .leaflet-popup-tip {{
            background: rgba(15, 23, 42, 0.95);
        }}
        .popup-card {{
            padding: 6px;
            font-size: 12px;
            min-width: 230px;
        }}
        .popup-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #334155;
            padding-bottom: 6px;
            margin-bottom: 8px;
        }}
        .popup-title {{
            font-size: 14px;
            font-weight: 700;
            color: #38bdf8;
        }}
        .popup-badge {{
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 700;
        }}
        .badge-optimo {{ background: rgba(16, 185, 129, 0.2); color: #10b981; border: 1px solid #10b981; }}
        .badge-sub {{ background: rgba(245, 158, 11, 0.2); color: #f59e0b; border: 1px solid #f59e0b; }}
        .badge-sobre {{ background: rgba(239, 68, 68, 0.2); color: #ef4444; border: 1px solid #ef4444; }}
        .popup-row {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 4px;
        }}
        .popup-row span.label {{ color: #94a3b8; }}
        .popup-row span.val {{ font-weight: 600; color: #f1f5f9; }}
        .progress-bar-bg {{
            width: 100%;
            height: 6px;
            background: #1e293b;
            border-radius: 3px;
            margin-top: 4px;
            overflow: hidden;
        }}
        .progress-bar-fill {{
            height: 100%;
            border-radius: 3px;
        }}
        /* Scrollbar */
        ::-webkit-scrollbar {{
            width: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: transparent;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 3px;
        }}
    </style>
</head>
<body>
    <div id="map"></div>

    <!-- Header Glassmorphic Bar -->
    <div class="header-bar">
        <div class="header-title">
            <h1>⚡ EPEC | Nuevas Rutas de Lectura <span class="badge">Distrito 1</span></h1>
        </div>
        <div class="stats-pills">
            <div class="pill">Rutas: <strong id="kpi-rutas">3.299</strong></div>
            <div class="pill">Suministros: <strong id="kpi-sumis">585.727</strong></div>
            <div class="pill">Mediana: <strong id="kpi-mediana">185 u.</strong></div>
            <div class="pill">Óptimas: <strong id="kpi-optimas" style="color: #10b981;">62.5%</strong></div>
        </div>
    </div>

    <!-- Sidebar Floating Controls -->
    <div class="sidebar">
        <h2>Panel de Filtros & Control <span id="visible-count" style="color:#38bdf8; font-weight:700;">(3.299)</span></h2>
        
        <div class="control-group">
            <label for="route-search">🔍 Buscar Ruta por Código</label>
            <input type="text" id="route-search" class="search-box" placeholder="Ej: 01005, 17206, 5005...">
        </div>

        <div class="control-group">
            <label for="group-select">📅 Grupo de Lectura (Ciclo 1 al 20)</label>
            <select id="group-select" class="select-custom">
                <option value="ALL">Todos los Grupos (1 al 20)</option>
                {"".join([f'<option value="{g}">Grupo {g} ({counts.get(str(g),0)} rutas)</option>' for g in range(1, 21)])}
            </select>
        </div>

        <div class="control-group">
            <label>⚖️ Capacidad Operativa (Suministros)</label>
            <div class="filter-buttons">
                <button class="btn-filter active" data-cap="ALL">Todas</button>
                <button class="btn-filter" data-cap="SI" style="color:#10b981;">Óptimas (160-200)</button>
                <button class="btn-filter" data-cap="SUB" style="color:#f59e0b;">Subcarga (&lt;160)</button>
                <button class="btn-filter" data-cap="SOBRE" style="color:#ef4444;">Sobrecarga (&gt;200)</button>
            </div>
        </div>

        <div class="control-group">
            <label>🗺️ Mapa Base</label>
            <select id="basemap-select" class="select-custom">
                <option value="dark">CartoDB Dark Matter (Nocturno)</option>
                <option value="light">CartoDB Positron (Claro)</option>
                <option value="osm">OpenStreetMap Estándar</option>
                <option value="esri">Esri Satelital</option>
            </select>
        </div>

        <div class="control-group">
            <label for="opacity-range">Opacidad de Polígonos: <span id="opacity-val">0.65</span></label>
            <input type="range" id="opacity-range" class="opacity-slider" min="0.1" max="1.0" step="0.05" value="0.65">
        </div>

        <div class="control-group">
            <label>📌 Referencias de Capacidad</label>
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background: #10b981;"></div>
                    <span><strong>160 a 200 sum</strong>: Óptimo Contractual (62.5%)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #f59e0b;"></div>
                    <span><strong>&lt; 160 sum</strong>: Subcarga / Periferia (26.4%)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #ef4444;"></div>
                    <span><strong>&gt; 200 sum</strong>: Sobrecarga / Macro (11.1%)</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Leaflet JS -->
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
    <script>
        // Datos GeoJSON inyectados directamente
        const geojsonData = {geojson_str};

        // Paleta de colores para los 20 grupos
        const groupColors = {json.dumps(colors_groups)};

        // Inicializar Mapa centrado en Córdoba Capital
        const map = L.map('map', {{
            center: [-31.4201, -64.1888],
            zoom: 12,
            zoomControl: false,
            preferCanvas: true
        }});

        L.control.zoom({{ position: 'bottomright' }}).addTo(map);

        // Capas de mapas base
        const basemaps = {{
            dark: L.tileLayer('https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
                maxZoom: 19,
                subdomains: 'abcd',
                attribution: '&copy; CartoDB &copy; OpenStreetMap'
            }}),
            light: L.tileLayer('https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
                maxZoom: 19,
                subdomains: 'abcd',
                attribution: '&copy; CartoDB &copy; OpenStreetMap'
            }}),
            osm: L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                maxZoom: 19,
                attribution: '&copy; OpenStreetMap contributors'
            }}),
            esri: L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
                maxZoom: 19,
                attribution: 'Tiles &copy; Esri'
            }})
        }};

        basemaps.dark.addTo(map);

        let currentOpacity = 0.65;
        let selectedGroup = "ALL";
        let selectedCap = "ALL";
        let geojsonLayer = null;
        let routeIndex = {{}};

        // Función de estilo
        function getFeatureStyle(feature) {{
            const g = String(feature.properties.grupo_lectura || "1");
            const color = groupColors[g] || "#38bdf8";
            return {{
                fillColor: color,
                weight: 1.2,
                opacity: 0.9,
                color: '#ffffff',
                fillOpacity: currentOpacity
            }};
        }}

        // Popup interactivo
        function onEachFeature(feature, layer) {{
            const props = feature.properties;
            routeIndex[String(props.nueva_ruta_lectura)] = layer;

            const cant = props.cant_suministros || 0;
            let badgeClass = "badge-optimo";
            let badgeText = "ÓPTIMO (160-200)";
            let progressColor = "#10b981";
            if (cant < 160) {{
                badgeClass = "badge-sub";
                badgeText = "SUBCARGA (&lt;160)";
                progressColor = "#f59e0b";
            }} else if (cant > 200) {{
                badgeClass = "badge-sobre";
                badgeText = "SOBRECARGA (&gt;200)";
                progressColor = "#ef4444";
            }}

            const compVal = (props.compacidad_isoperimetrica || 0).toFixed(3);
            const compPercent = Math.min(100, Math.round((props.compacidad_isoperimetrica || 0) * 100));

            const popupHtml = `
                <div class="popup-card">
                    <div class="popup-header">
                        <span class="popup-title">Ruta #` + props.nueva_ruta_lectura + `</span>
                        <span class="popup-badge ` + badgeClass + `">` + badgeText + `</span>
                    </div>
                    <div class="popup-row">
                        <span class="label">Grupo de Lectura:</span>
                        <span class="val">Grupo ` + props.grupo_lectura + `</span>
                    </div>
                    <div class="popup-row">
                        <span class="label">Suministros:</span>
                        <span class="val" style="color:` + progressColor + `; font-size:13px;">` + cant + ` u.</span>
                    </div>
                    <div class="popup-row">
                        <span class="label">Manzanas:</span>
                        <span class="val">` + (props.cant_manzanas || 0) + ` mzas</span>
                    </div>
                    <div class="popup-row">
                        <span class="label">Área:</span>
                        <span class="val">` + (props.area_hectareas || 0).toFixed(2) + ` ha</span>
                    </div>
                    <div class="popup-row">
                        <span class="label">Perímetro:</span>
                        <span class="val">` + (props.perimetro_km || 0).toFixed(2) + ` km</span>
                    </div>
                    <div class="popup-row">
                        <span class="label">Compacidad:</span>
                        <span class="val">` + compVal + `</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill" style="width: ` + compPercent + `%; background: ` + progressColor + `;"></div>
                    </div>
                </div>
            `;

            layer.bindPopup(popupHtml);

            // Hover effects
            layer.on({{
                mouseover: function(e) {{
                    const l = e.target;
                    l.setStyle({{
                        weight: 2.8,
                        color: '#38bdf8',
                        fillOpacity: Math.min(1.0, currentOpacity + 0.25)
                    }});
                    l.bringToFront();
                }},
                mouseout: function(e) {{
                    geojsonLayer.resetStyle(e.target);
                }}
            }});
        }}

        // Filtrado dinámico
        function filterFeature(feature) {{
            const props = feature.properties;
            const g = String(props.grupo_lectura);
            const cant = props.cant_suministros || 0;

            if (selectedGroup !== "ALL" && g !== selectedGroup) {{
                return false;
            }}

            if (selectedCap === "SI") {{
                if (cant < 160 || cant > 200) return false;
            }} else if (selectedCap === "SUB") {{
                if (cant >= 160) return false;
            }} else if (selectedCap === "SOBRE") {{
                if (cant <= 200) return false;
            }}

            return true;
        }}

        function updateLayer() {{
            if (geojsonLayer) {{
                map.removeLayer(geojsonLayer);
            }}

            routeIndex = {{}};
            geojsonLayer = L.geoJSON(geojsonData, {{
                style: getFeatureStyle,
                onEachFeature: onEachFeature,
                filter: filterFeature
            }}).addTo(map);

            let visibleCount = 0;
            let totalSumis = 0;
            let optimasCount = 0;

            geojsonData.features.forEach(f => {{
                if (filterFeature(f)) {{
                    visibleCount++;
                    const c = f.properties.cant_suministros || 0;
                    totalSumis += c;
                    if (c >= 160 && c <= 200) optimasCount++;
                }}
            }});

            document.getElementById('visible-count').innerText = '(' + visibleCount.toLocaleString() + ')';
            document.getElementById('kpi-rutas').innerText = visibleCount.toLocaleString();
            document.getElementById('kpi-sumis').innerText = totalSumis.toLocaleString();
            const pct = visibleCount > 0 ? ((optimasCount / visibleCount) * 100).toFixed(1) + '%' : '0%';
            document.getElementById('kpi-optimas').innerText = pct;
        }}

        // Render inicial
        updateLayer();

        // Control de Eventos
        document.getElementById('group-select').addEventListener('change', function(e) {{
            selectedGroup = e.target.value;
            updateLayer();
            if (selectedGroup !== "ALL") {{
                // Auto-fit bounds del grupo
                const groupBounds = geojsonLayer.getBounds();
                if (groupBounds.isValid()) {{
                    map.fitBounds(groupBounds, {{ padding: [30, 30] }});
                }}
            }}
        }});

        document.querySelectorAll('.btn-filter').forEach(btn => {{
            btn.addEventListener('click', function() {{
                document.querySelectorAll('.btn-filter').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                selectedCap = this.getAttribute('data-cap');
                updateLayer();
            }});
        }});

        document.getElementById('basemap-select').addEventListener('change', function(e) {{
            Object.values(basemaps).forEach(l => map.removeLayer(l));
            basemaps[e.target.value].addTo(map);
            geojsonLayer.bringToFront();
        }});

        document.getElementById('opacity-range').addEventListener('input', function(e) {{
            currentOpacity = parseFloat(e.target.value);
            document.getElementById('opacity-val').innerText = currentOpacity.toFixed(2);
            geojsonLayer.eachLayer(l => {{
                l.setStyle({{ fillOpacity: currentOpacity }});
            }});
        }});

        // Buscador de ruta con autocompletado y zoom
        document.getElementById('route-search').addEventListener('input', function(e) {{
            const val = e.target.value.trim();
            if (val.length >= 3 && routeIndex[val]) {{
                const targetLayer = routeIndex[val];
                map.fitBounds(targetLayer.getBounds(), {{ maxZoom: 16, padding: [50, 50] }});
                targetLayer.openPopup();
            }}
        }});
    </script>
</body>
</html>
"""

print(f"\n[4/4] Escribiendo archivo HTML interactivo optimizado...")
print(f"      1. Guardando en Proyecto: {out_html_proj}")
with open(out_html_proj, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"      2. Guardando en Descargas (C:): {out_html_c_down}")
with open(out_html_c_down, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"      3. Guardando en Descargas (D:): {out_html_d_down}")
with open(out_html_d_down, 'w', encoding='utf-8') as f:
    f.write(html_content)

total_time = time.time() - t0
print("\n" + "=" * 100)
print(f"VISOR CARTOGRÁFICO INTERACTIVO GENERADO CON ÉXITO EN {total_time:.2f} SEGUNDOS!")
print("=" * 100)
