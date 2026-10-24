import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_dir = r"D:\Usuarios\jidiaz\Downloads\visor_manzanas_rutas"
index_path = os.path.join(target_dir, "index.html")
app_js_path = os.path.join(target_dir, "js", "app.js")

print(f"Actualizando visor en: {target_dir}")

# 1. Contenido de index.html
html_code = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SIGEC - Visor Geoespacial de Manzanas y Rutas de Lectura | Distrito 1 EPEC</title>
  <meta name="description" content="Visor geoespacial interactivo de manzanas catastrales y polígonos consolidados de rutas de lectura para el Distrito 1 de EPEC (Córdoba). Inspección de contigüidad, calles perimetrales y suministros.">
  
  <!-- Leaflet CSS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
  
  <!-- Custom Styles -->
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

  <!-- Loading Splash Screen -->
  <div id="loadingOverlay" class="loading-overlay">
    <div class="spinner"></div>
    <div class="loading-text" id="loadingText">Iniciando Visor de Manzanas y Rutas Catastrales...</div>
    <div class="loading-subtext">Cargando 18.721 manzanas y 3.299 rutas disjuntas (Distrito 1)</div>
  </div>

  <!-- Top Glassmorphic Navigation Bar -->
  <header class="top-nav glass-panel">
    <div class="brand-section">
      <div class="brand-badge">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
        </svg>
      </div>
      <div class="brand-text">
        <h1>SIGEC • Manzanas & Rutas</h1>
        <p><span class="status-dot"></span> D1 • Capital y Periurbano</p>
      </div>
    </div>

    <!-- KPIs Compactos -->
    <div class="kpi-group">
      <div class="kpi-pill" title="Manzanas catastrales procesadas">
        <span class="kpi-label">Mzas</span>
        <span class="kpi-value" id="kpiMzas">18.721</span>
      </div>
      <div class="kpi-pill" title="Rutas nuevas de lectura asignadas">
        <span class="kpi-label">Rutas</span>
        <span class="kpi-value" id="kpiRutas">3.299</span>
      </div>
      <div class="kpi-pill" title="Suministros totales auditados">
        <span class="kpi-label">Sumis</span>
        <span class="kpi-value" id="kpiSumis">585.727</span>
      </div>
    </div>

    <!-- Filter Status Badge (visible when a route is isolated) -->
    <div id="filterStatusBadge" class="filter-status-badge hidden">
      <span class="badge-dot"></span>
      <span id="filterStatusText">Filtro activo</span>
      <button id="btnRemoveFilterBadge" class="btn-badge-remove" title="Quitar filtro de ruta y ver todas">✕</button>
    </div>

    <!-- Controls Toolbar -->
    <div class="controls-group">
      <!-- Search Input -->
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input type="text" id="searchInput" class="search-input" placeholder="Buscar Ruta, Mza o Calle..." autocomplete="off">
      </div>

      <!-- Layer View Selector -->
      <select id="layerModeSelect" class="select-control" title="Capa Territorial Visible">
        <option value="both" selected>✨ Rutas + Manzanas</option>
        <option value="routes">🔷 Polígonos de Rutas (3.299)</option>
        <option value="mzas">🏘️ Manzanas Catastrales (18.721)</option>
      </select>

      <!-- Cycle Filter -->
      <select id="cycleSelect" class="select-control" title="Filtrar por Ciclo de Facturación (Grupo 1 al 20)">
        <option value="all">Todos los Ciclos</option>
      </select>

      <!-- Color Mode -->
      <select id="colorModeSelect" class="select-control" title="Modo de Coloración">
        <option value="route">🎨 Color Ruta (Áurea)</option>
        <option value="cycle">📅 Color Ciclo (20)</option>
        <option value="density">📊 Densidad Suministros</option>
        <option value="capacity">⚖️ Capacidad (180±20)</option>
      </select>

      <!-- Action Button: Borrar Filtro / Deseleccionar -->
      <button id="btnCleanFilter" class="btn-action-clear" title="Borrar selección de manzana o aislamiento de ruta (Esc)">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
        <span>Borrar Filtro</span>
      </button>

      <!-- Reset View -->
      <button id="btnResetView" class="btn-icon" title="Restablecer Vista General y Filtros (Esc)">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/>
          <path d="M3 3v5h5"/>
        </svg>
      </button>
    </div>
  </header>

  <!-- Floating Navigation Toolbar: Zoom In, Zoom Out, Full Extent, Clear -->
  <aside class="floating-nav-toolbar glass-panel" title="Navegación del mapa">
    <button id="btnZoomIn" class="btn-nav" title="Acercar mapa (+ o Ctrl+Scroll Arriba)">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <line x1="12" y1="5" x2="12" y2="19"></line>
        <line x1="5" y1="12" x2="19" y2="12"></line>
      </svg>
    </button>
    <button id="btnZoomOut" class="btn-nav" title="Alejar mapa (- o Ctrl+Scroll Abajo)">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <line x1="5" y1="12" x2="19" y2="12"></line>
      </svg>
    </button>
    <div class="nav-divider"></div>
    <button id="btnFitDistrict" class="btn-nav" title="Centrar todo el Distrito 1 de Córdoba">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/>
      </svg>
    </button>
    <button id="btnFloatClear" class="btn-nav btn-nav-clear" title="Borrar selección de manzana o filtro de ruta">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
      </svg>
    </button>
  </aside>

  <!-- Fullscreen Map Canvas -->
  <main id="map"></main>

  <!-- Inspector Floating Sidebar -->
  <aside id="inspectorPanel" class="inspector-panel glass-panel">
    <div class="inspector-header">
      <h2>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2">
          <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
          <line x1="3" y1="9" x2="21" y2="9"></line>
          <line x1="9" y1="21" x2="9" y2="9"></line>
        </svg>
        <span id="inspectorTitle">Detalle de Selección</span>
      </h2>
      <button id="inspectorClose" class="inspector-close" title="Cerrar panel (Esc)">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    </div>

    <div class="inspector-body">
      <!-- Info Card 1: Identificación -->
      <div class="info-card">
        <div class="info-row">
          <span class="info-label" id="inspField1Label">Nomenclatura Catastral</span>
          <span class="info-val" id="inspMza" style="font-family:monospace; color:#38bdf8;">-</span>
        </div>
        <div class="info-row">
          <span class="info-label">Ruta de Lectura Asignada</span>
          <span class="route-badge-large" id="inspRutaBadge">Ruta -</span>
        </div>
        <div class="info-row">
          <span class="info-label">Grupo Cíclico</span>
          <span class="info-val" id="inspGrupo">-</span>
        </div>
        <div class="info-row">
          <span class="info-label">Carga de Suministros</span>
          <span class="info-val" id="inspSumis" style="color:#34d399; font-weight:700;">-</span>
        </div>
        <div class="info-row" id="inspRowCapacidad" style="display:none;">
          <span class="info-label">Estado de Capacidad</span>
          <span class="info-val" id="inspCapacidadBadge">-</span>
        </div>
        <div class="info-row" id="inspRowFuente">
          <span class="info-label">Fuente Geometría</span>
          <span class="info-val" id="inspFuente">IDECOR</span>
        </div>
      </div>

      <!-- Info Card 2: Perímetro, Geometría y Calles -->
      <div class="info-card" id="inspCardGeometry">
        <div class="info-row" id="inspRowArea" style="display:none;">
          <span class="info-label">Área Territorial</span>
          <span class="info-val" id="inspArea">-</span>
        </div>
        <div class="info-row" id="inspRowPerimetro" style="display:none;">
          <span class="info-label">Perímetro</span>
          <span class="info-val" id="inspPerimetro">-</span>
        </div>
        <div class="info-row" id="inspRowCompacidad" style="display:none;">
          <span class="info-label">Compacidad Isoperimétrica</span>
          <span class="info-val" id="inspCompacidad">-</span>
        </div>
        <div class="progress-bar-bg" id="inspCompBar" style="display:none; margin-bottom:8px; width:100%; height:6px; background:#1e293b; border-radius:3px; overflow:hidden;">
          <div class="progress-bar-fill" id="inspCompFill" style="width:0%; height:100%; border-radius:3px; background:#10b981;"></div>
        </div>

        <span class="info-label">Calles Perimetrales / Principales</span>
        <div class="streets-tag-list" id="inspCalles">
          <!-- Chips generados dinámicamente -->
        </div>
        <div style="margin-top: 10px;" id="inspAlturasContainer">
          <span class="info-label">Alturas Observadas por Calle</span>
          <p id="inspAlturas" style="font-size:0.75rem; color:#94a3b8; margin-top:4px; line-height:1.4;">-</p>
        </div>
      </div>

      <!-- Actions -->
      <div class="inspector-actions">
        <button id="btnIsolateRoute" class="btn-primary">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
            <polyline points="2 17 12 22 22 17"></polyline>
            <polyline points="2 12 12 17 22 12"></polyline>
          </svg>
          Aislar y Enfocar esta Ruta Completa
        </button>
        <button id="btnDeselectMza" class="btn-secondary">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
          Deseleccionar / Quitar Filtro
        </button>
      </div>
    </div>
  </aside>

  <!-- Bottom Floating Legend -->
  <footer class="legend-panel glass-panel">
    <div class="legend-item">
      <span class="legend-swatch" style="background:#38bdf8;"></span>
      <span>Manzanas Catastrales</span>
    </div>
    <div class="legend-item">
      <span class="legend-swatch" style="background:linear-gradient(90deg, #ec4899, #3b82f6, #10b981, #f59e0b);"></span>
      <span>Rutas (Paleta Áurea)</span>
    </div>
    <div class="legend-item">
      <span class="legend-swatch" style="background:#10b981;"></span>
      <span>Óptimo (160-200)</span>
    </div>
    <div class="legend-item">
      <span class="legend-swatch" style="background:#f59e0b;"></span>
      <span>Subcarga (&lt;160)</span>
    </div>
    <div class="legend-item">
      <span class="legend-swatch" style="background:#ef4444;"></span>
      <span>Sobrecarga (&gt;200)</span>
    </div>
    <div class="legend-item" style="color:var(--text-muted); font-size:0.74rem;">
      <span>💡 Navegación: <b>Ctrl + Scroll</b> o botones de zoom lateral • <b>Esc</b> para borrar selección</span>
    </div>
  </footer>

  <!-- Leaflet JS -->
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
  
  <!-- Pre-cargadores de Datos Locales (Doble-clic directo sin servidor web local) -->
  <script src="data/manzanas_rutas_data.js"></script>
  <script src="data/rutas_poligonos_data.js"></script>
  
  <!-- Lógica Principal Unificada -->
  <script src="js/app.js"></script>

</body>
</html>
"""

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html_code)
print("✔ index.html escrito con éxito.")

# 2. Contenido de js/app.js
js_code = """// SIGEC - EPEC: Visor Geoespacial Unificado de Manzanas Catastrales y Polígonos de Rutas
// Distrito 1 - Optimizado con Canvas Renderer para 18.721 Manzanas y 3.299 Rutas

document.addEventListener('DOMContentLoaded', () => {
  const loadingOverlay = document.getElementById('loadingOverlay');
  const loadingText = document.getElementById('loadingText');
  const searchInput = document.getElementById('searchInput');
  const cycleSelect = document.getElementById('cycleSelect');
  const colorModeSelect = document.getElementById('colorModeSelect');
  const layerModeSelect = document.getElementById('layerModeSelect');
  
  // Elementos de Inspección y Filtros
  const inspectorPanel = document.getElementById('inspectorPanel');
  const inspectorTitle = document.getElementById('inspectorTitle');
  const inspectorClose = document.getElementById('inspectorClose');
  const btnIsolateRoute = document.getElementById('btnIsolateRoute');
  const btnDeselectMza = document.getElementById('btnDeselectMza');
  const btnCleanFilter = document.getElementById('btnCleanFilter');
  const btnResetView = document.getElementById('btnResetView');
  const filterStatusBadge = document.getElementById('filterStatusBadge');
  const filterStatusText = document.getElementById('filterStatusText');
  const btnRemoveFilterBadge = document.getElementById('btnRemoveFilterBadge');
  
  // Botones de Navegación y Zoom
  const btnZoomIn = document.getElementById('btnZoomIn');
  const btnZoomOut = document.getElementById('btnZoomOut');
  const btnFitDistrict = document.getElementById('btnFitDistrict');
  const btnFloatClear = document.getElementById('btnFloatClear');
  
  // Ficha de Inspección
  const inspField1Label = document.getElementById('inspField1Label');
  const inspMza = document.getElementById('inspMza');
  const inspRutaBadge = document.getElementById('inspRutaBadge');
  const inspGrupo = document.getElementById('inspGrupo');
  const inspSumis = document.getElementById('inspSumis');
  const inspRowCapacidad = document.getElementById('inspRowCapacidad');
  const inspCapacidadBadge = document.getElementById('inspCapacidadBadge');
  const inspRowFuente = document.getElementById('inspRowFuente');
  const inspFuente = document.getElementById('inspFuente');
  
  const inspRowArea = document.getElementById('inspRowArea');
  const inspArea = document.getElementById('inspArea');
  const inspRowPerimetro = document.getElementById('inspRowPerimetro');
  const inspPerimetro = document.getElementById('inspPerimetro');
  const inspRowCompacidad = document.getElementById('inspRowCompacidad');
  const inspCompacidad = document.getElementById('inspCompacidad');
  const inspCompBar = document.getElementById('inspCompBar');
  const inspCompFill = document.getElementById('inspCompFill');
  const inspCalles = document.getElementById('inspCalles');
  const inspAlturasContainer = document.getElementById('inspAlturasContainer');
  const inspAlturas = document.getElementById('inspAlturas');
  
  // Contadores KPI
  const kpiMzas = document.getElementById('kpiMzas');
  const kpiRutas = document.getElementById('kpiRutas');
  const kpiSumis = document.getElementById('kpiSumis');
  
  let currentSelectedFeature = null;
  let activeIsolatedRoute = null;
  let activeCycleFilter = 'all';
  let currentColorMode = 'route'; // 'route', 'cycle', 'density', 'capacity'
  let currentLayerMode = 'both';  // 'both', 'routes', 'mzas'
  let lastFeatureClickTime = 0;

  // 1. Inicializar Mapa Leaflet con soporte de zoom
  const map = L.map('map', {
    center: [-31.4201, -64.1888], // Córdoba Capital Centro
    zoom: 13,
    minZoom: 10,
    maxZoom: 19,
    preferCanvas: true,
    scrollWheelZoom: true,
    zoomControl: false // Usamos nuestra barra personalizada integrada
  });
  
  // Renderers Canvas ultra-rápidos
  const canvasRendererMzas = L.canvas({ padding: 0.5, tolerance: 4 });
  const canvasRendererRoutes = L.canvas({ padding: 0.5, tolerance: 4 });
  
  // Capas Base
  const baseLayers = {
    "OpenStreetMap (Voyager - Predeterminado)": L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
      maxZoom: 19,
      attribution: '&copy; OpenStreetMap contributors &copy; CARTO'
    }),
    "ESRI Calles del Mundo": L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19,
      attribution: 'Tiles &copy; Esri &mdash; World Street Map'
    }),
    "CartoDB Claro": L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
      maxZoom: 19,
      attribution: '&copy; OpenStreetMap &copy; CARTO'
    }),
    "CartoDB Oscuro": L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
      maxZoom: 19,
      attribution: '&copy; OpenStreetMap &copy; CARTO'
    }),
    "Satélite (ESRI)": L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19,
      attribution: 'Tiles &copy; Esri &mdash; World Imagery'
    })
  };
  
  baseLayers["OpenStreetMap (Voyager - Predeterminado)"].addTo(map);
  L.control.layers(baseLayers, null, { position: 'bottomright' }).addTo(map);
  
  // Capa para destacar la selección
  const highlightLayer = L.geoJSON(null, {
    interactive: false,
    style: {
      color: '#0284c7',
      weight: 3.5,
      fillColor: '#38bdf8',
      fillOpacity: 0.85,
      dashArray: '4, 4'
    }
  }).addTo(map);

  // Paleta Áurea Determinística para Rutas (3.300 colores distintos)
  function getRouteColor(routeId) {
    if (!routeId || routeId === 0) return '#64748b';
    const num = parseInt(routeId, 10);
    const hue = (!isNaN(num) ? (num * 137.507764) : 200) % 360;
    return `hsl(${hue.toFixed(1)}, 84%, 55%)`;
  }
  
  // Paleta de 20 Ciclos de Facturación
  const cyclePalette = [
    '#f43f5e', '#ec4899', '#d946ef', '#a855f7', '#8b5cf6',
    '#6366f1', '#3b82f6', '#0ea5e9', '#06b6d4', '#14b8a6',
    '#10b981', '#22c55e', '#84cc16', '#eab308', '#f59e0b',
    '#f97316', '#ef4444', '#78716c', '#0284c7', '#4f46e5'
  ];
  
  function getCycleColor(cycleStr) {
    const num = parseInt(cycleStr, 10);
    if (isNaN(num)) return '#94a3b8';
    return cyclePalette[(num - 1) % cyclePalette.length];
  }
  
  function getDensityColor(sumis) {
    if (sumis <= 10) return '#38bdf8';
    if (sumis <= 30) return '#34d399';
    if (sumis <= 70) return '#fbbf24';
    if (sumis <= 150) return '#f97316';
    return '#ef4444'; // Macro-manzana
  }

  function getCapacityColor(sumis) {
    if (sumis >= 160 && sumis <= 200) return '#10b981'; // Óptimo
    if (sumis < 160) return '#f59e0b'; // Subcarga
    return '#ef4444'; // Sobrecarga
  }
  
  function getFeatureColor(props, isRoutePoly = false) {
    const sumis = isRoutePoly ? (props.cant_suministros || 0) : (props.s || 0);
    const rId = isRoutePoly ? props.nueva_ruta_lectura : props.r;
    const gVal = isRoutePoly ? props.grupo_lectura : props.g;

    if (currentColorMode === 'cycle') return getCycleColor(gVal);
    if (currentColorMode === 'density') return getDensityColor(sumis);
    if (currentColorMode === 'capacity') return getCapacityColor(sumis);
    return getRouteColor(rId);
  }
  
  // Estructuras de datos
  let geojsonMzasLayer = null;
  let geojsonRoutesLayer = null;
  
  let allMzasFeatures = [];
  let allRoutesFeatures = [];
  let featuresByMza = new Map();
  let featuresByRouteMzas = new Map();
  let routesById = new Map();

  // Estilo para Manzanas
  function styleMzaFeature(feature) {
    if (currentLayerMode === 'routes') {
      return { renderer: canvasRendererMzas, fillColor: 'transparent', fillOpacity: 0, color: 'transparent', weight: 0, interactive: false };
    }

    const props = feature.properties;
    const isIsolated = (activeIsolatedRoute !== null);
    const matchesIsolated = (props.r === activeIsolatedRoute);
    
    if (isIsolated && !matchesIsolated) {
      return {
        renderer: canvasRendererMzas,
        fillColor: '#94a3b8',
        fillOpacity: 0.05,
        color: '#cbd5e1',
        weight: 0.2,
        interactive: true
      };
    }
    
    if (activeCycleFilter !== 'all' && String(props.g) !== String(activeCycleFilter)) {
      return {
        renderer: canvasRendererMzas,
        fillColor: 'transparent',
        fillOpacity: 0,
        color: 'transparent',
        weight: 0,
        interactive: false
      };
    }
    
    const color = getFeatureColor(props, false);
    return {
      renderer: canvasRendererMzas,
      fillColor: color,
      fillOpacity: isIsolated ? 0.88 : (currentLayerMode === 'both' ? 0.65 : 0.75),
      color: isIsolated ? '#0f172a' : '#334155',
      weight: isIsolated ? 2.0 : 0.8,
      interactive: true
    };
  }

  // Estilo para Polígonos Consolidados de Rutas
  function styleRouteFeature(feature) {
    if (currentLayerMode === 'mzas') {
      return { renderer: canvasRendererRoutes, fillColor: 'transparent', fillOpacity: 0, color: 'transparent', weight: 0, interactive: false };
    }

    const props = feature.properties;
    const rId = props.nueva_ruta_lectura;
    const isIsolated = (activeIsolatedRoute !== null);
    const matchesIsolated = (rId === activeIsolatedRoute);

    if (isIsolated && !matchesIsolated) {
      return {
        renderer: canvasRendererRoutes,
        fillColor: 'transparent',
        fillOpacity: 0,
        color: '#64748b',
        weight: 0.3,
        interactive: false
      };
    }

    if (activeCycleFilter !== 'all' && String(props.grupo_lectura) !== String(activeCycleFilter)) {
      return {
        renderer: canvasRendererRoutes,
        fillColor: 'transparent',
        fillOpacity: 0,
        color: 'transparent',
        weight: 0,
        interactive: false
      };
    }

    const color = getFeatureColor(props, true);
    const isBothMode = (currentLayerMode === 'both');

    return {
      renderer: canvasRendererRoutes,
      fillColor: isBothMode ? 'transparent' : color,
      fillOpacity: isBothMode ? 0 : (isIsolated ? 0.75 : 0.45),
      color: isBothMode ? (isIsolated ? '#38bdf8' : color) : '#ffffff',
      weight: isBothMode ? (isIsolated ? 3.0 : 1.8) : 1.2,
      dashArray: isBothMode ? '4, 4' : null,
      interactive: true
    };
  }

  function selectFeature(feature, isRoutePoly = false) {
    currentSelectedFeature = feature;
    const p = feature.properties;
    
    highlightLayer.clearLayers();
    highlightLayer.addData(feature);
    
    if (isRoutePoly) {
      // Selección de Ruta Consolidada
      const rId = p.nueva_ruta_lectura;
      const cant = p.cant_suministros || 0;
      
      if (inspectorTitle) inspectorTitle.textContent = "Detalle de Ruta";
      if (inspField1Label) inspField1Label.textContent = "ID Nueva Ruta";
      if (inspMza) inspMza.textContent = `Ruta #${rId}`;
      if (inspRutaBadge) {
        inspRutaBadge.textContent = `Ruta ${rId}`;
        inspRutaBadge.style.background = getRouteColor(rId);
      }
      if (inspGrupo) inspGrupo.textContent = `Grupo ${p.grupo_lectura}`;
      if (inspSumis) inspSumis.textContent = `${cant.toLocaleString('es-AR')} suministros`;
      
      // Estado de capacidad
      if (inspRowCapacidad && inspCapacidadBadge) {
        inspRowCapacidad.style.display = 'flex';
        if (cant >= 160 && cant <= 200) {
          inspCapacidadBadge.innerHTML = '<span class="badge-capacity badge-capacity-green">🟢 Óptimo (160-200)</span>';
        } else if (cant < 160) {
          inspCapacidadBadge.innerHTML = `<span class="badge-capacity badge-capacity-orange">🟡 Subcarga (${cant} u.)</span>`;
        } else {
          inspCapacidadBadge.innerHTML = `<span class="badge-capacity badge-capacity-red">🔴 Sobrecarga (${cant} u.)</span>`;
        }
      }
      if (inspRowFuente && inspFuente) inspFuente.textContent = 'Polígono Disuelto IDECOR';
      
      // Área, Perímetro y Compacidad
      if (inspRowArea && inspArea) {
        inspRowArea.style.display = 'flex';
        inspArea.textContent = `${(p.area_hectareas || 0).toFixed(2)} ha`;
      }
      if (inspRowPerimetro && inspPerimetro) {
        inspRowPerimetro.style.display = 'flex';
        inspPerimetro.textContent = `${(p.perimetro_km || 0).toFixed(2)} km`;
      }
      if (inspRowCompacidad && inspCompacidad) {
        inspRowCompacidad.style.display = 'flex';
        const comp = (p.compacidad_isoperimetrica || 0);
        inspCompacidad.textContent = `${comp.toFixed(3)} (${(comp*100).toFixed(1)}%)`;
      }
      if (inspCompBar && inspCompFill) {
        inspCompBar.style.display = 'block';
        const pct = Math.min(100, Math.round((p.compacidad_isoperimetrica || 0) * 100));
        inspCompFill.style.width = `${pct}%`;
        inspCompFill.style.background = (pct >= 25) ? '#10b981' : '#f59e0b';
      }
      
      // Calles
      if (inspCalles) {
        inspCalles.innerHTML = '';
        if (p.calles_compartidas_en_ruta && p.calles_compartidas_en_ruta.trim() !== '') {
          const streets = p.calles_compartidas_en_ruta.split(',').map(s => s.trim()).filter(s => s.length > 0);
          streets.slice(0, 10).forEach(street => {
            const tag = document.createElement('span');
            tag.className = 'street-tag';
            tag.textContent = street;
            inspCalles.appendChild(tag);
          });
        } else {
          inspCalles.innerHTML = '<span style="color:var(--text-muted); font-size:0.75rem;">Calles residenciales urbanas</span>';
        }
      }
      if (inspAlturasContainer) inspAlturasContainer.style.display = 'none';

    } else {
      // Selección de Manzana Catastral
      if (inspectorTitle) inspectorTitle.textContent = "Detalle de Manzana";
      if (inspField1Label) inspField1Label.textContent = "Nomenclatura Catastral";
      if (inspMza) inspMza.textContent = p.m;
      if (inspRutaBadge) {
        inspRutaBadge.textContent = `Ruta ${p.r}`;
        inspRutaBadge.style.background = getRouteColor(p.r);
      }
      if (inspGrupo) inspGrupo.textContent = `Ciclo ${p.g}`;
      if (inspSumis) inspSumis.textContent = `${(p.s || 0).toLocaleString('es-AR')} suministros`;
      if (inspRowCapacidad) inspRowCapacidad.style.display = 'none';
      if (inspRowFuente && inspFuente) inspFuente.textContent = p.f || 'IDECOR';
      
      if (inspRowArea) inspRowArea.style.display = 'none';
      if (inspRowPerimetro) inspRowPerimetro.style.display = 'none';
      if (inspRowCompacidad) inspRowCompacidad.style.display = 'none';
      if (inspCompBar) inspCompBar.style.display = 'none';
      
      if (inspCalles) {
        inspCalles.innerHTML = '';
        if (p.c && p.c.trim() !== '') {
          const streets = p.c.split('|').map(s => s.trim()).filter(s => s.length > 0);
          streets.forEach(street => {
            const tag = document.createElement('span');
            tag.className = 'street-tag';
            tag.textContent = street;
            inspCalles.appendChild(tag);
          });
        } else {
          inspCalles.innerHTML = '<span style="color:var(--text-muted); font-size:0.75rem;">Sin calles catalogadas</span>';
        }
      }
      
      if (inspAlturasContainer) inspAlturasContainer.style.display = 'block';
      if (inspAlturas) {
        if (p.a && p.a.trim() !== '') {
          inspAlturas.textContent = p.a.split(';').slice(0, 4).join('; ');
        } else {
          inspAlturas.textContent = 'N/D';
        }
      }
    }
    
    if (inspectorPanel) {
      inspectorPanel.classList.add('open');
    }
  }

  function clearAllSelectionsAndFilters() {
    currentSelectedFeature = null;
    activeIsolatedRoute = null;
    activeCycleFilter = 'all';
    
    if (cycleSelect) cycleSelect.value = 'all';
    if (searchInput) searchInput.value = '';
    
    highlightLayer.clearLayers();
    
    if (inspectorPanel) {
      inspectorPanel.classList.remove('open');
    }
    
    if (filterStatusBadge) {
      filterStatusBadge.classList.add('hidden');
    }
    
    map.getContainer().style.cursor = '';
    
    if (geojsonMzasLayer) geojsonMzasLayer.setStyle(styleMzaFeature);
    if (geojsonRoutesLayer) geojsonRoutesLayer.setStyle(styleRouteFeature);
  }

  // Aislar Ruta Completa
  if (btnIsolateRoute) {
    btnIsolateRoute.addEventListener('click', () => {
      if (!currentSelectedFeature) return;
      const targetRoute = currentSelectedFeature.properties.r || currentSelectedFeature.properties.nueva_ruta_lectura;
      activeIsolatedRoute = targetRoute;
      
      const routeFeats = featuresByRouteMzas.get(targetRoute) || [];
      
      if (filterStatusBadge && filterStatusText) {
        filterStatusText.textContent = `Ruta ${targetRoute} (${routeFeats.length} mzas)`;
        filterStatusBadge.classList.remove('hidden');
      }
      
      if (geojsonMzasLayer) geojsonMzasLayer.setStyle(styleMzaFeature);
      if (geojsonRoutesLayer) geojsonRoutesLayer.setStyle(styleRouteFeature);
      
      // Enfocar polígono consolidado de la ruta si existe, o sus manzanas
      if (routesById.has(targetRoute)) {
        const rFeat = routesById.get(targetRoute);
        const bounds = L.geoJSON(rFeat).getBounds();
        map.fitBounds(bounds, { padding: [60, 60], maxZoom: 17 });
      } else if (routeFeats.length > 0) {
        const bounds = L.geoJSON({ type: 'FeatureCollection', features: routeFeats }).getBounds();
        map.fitBounds(bounds, { padding: [60, 60], maxZoom: 17 });
      }
    });
  }

  if (btnDeselectMza) btnDeselectMza.addEventListener('click', clearAllSelectionsAndFilters);
  if (btnCleanFilter) btnCleanFilter.addEventListener('click', clearAllSelectionsAndFilters);
  if (btnRemoveFilterBadge) btnRemoveFilterBadge.addEventListener('click', clearAllSelectionsAndFilters);
  if (btnFloatClear) btnFloatClear.addEventListener('click', clearAllSelectionsAndFilters);

  if (inspectorClose) {
    inspectorClose.addEventListener('click', () => {
      inspectorPanel.classList.remove('open');
      highlightLayer.clearLayers();
    });
  }

  if (btnResetView) {
    btnResetView.addEventListener('click', () => {
      clearAllSelectionsAndFilters();
      map.setView([-31.4201, -64.1888], 13);
    });
  }

  if (btnZoomIn) btnZoomIn.addEventListener('click', () => map.zoomIn());
  if (btnZoomOut) btnZoomOut.addEventListener('click', () => map.zoomOut());

  if (btnFitDistrict) {
    btnFitDistrict.addEventListener('click', () => {
      if (geojsonRoutesLayer) {
        map.fitBounds(geojsonRoutesLayer.getBounds(), { padding: [25, 25] });
      } else if (geojsonMzasLayer) {
        map.fitBounds(geojsonMzasLayer.getBounds(), { padding: [25, 25] });
      } else {
        map.setView([-31.4201, -64.1888], 13);
      }
    });
  }

  // Soporte nativo para Ctrl + Scroll del mouse
  const mapContainer = document.getElementById('map');
  if (mapContainer) {
    mapContainer.addEventListener('wheel', (e) => {
      if (e.ctrlKey) {
        e.preventDefault();
        if (e.deltaY < 0) map.zoomIn(1);
        else if (e.deltaY > 0) map.zoomOut(1);
      }
    }, { passive: false });
  }

  // Atajos de Teclado (+, -, Esc)
  window.addEventListener('keydown', (e) => {
    if (document.activeElement === searchInput) return;
    if (e.key === 'Escape') clearAllSelectionsAndFilters();
    else if (e.key === '+' || e.key === '=') map.zoomIn();
    else if (e.key === '-' || e.key === '_') map.zoomOut();
  });

  // Clic en área vacía del mapa deselecciona
  map.on('click', () => {
    if (Date.now() - lastFeatureClickTime < 250) return;
    if (currentSelectedFeature && activeIsolatedRoute === null) {
      currentSelectedFeature = null;
      highlightLayer.clearLayers();
      if (inspectorPanel) inspectorPanel.classList.remove('open');
      map.getContainer().style.cursor = '';
    }
  });

  // Selector de Ciclo
  if (cycleSelect) {
    cycleSelect.addEventListener('change', (e) => {
      activeCycleFilter = e.target.value;
      activeIsolatedRoute = null;
      
      if (filterStatusBadge && filterStatusText) {
        if (activeCycleFilter !== 'all') {
          filterStatusText.textContent = `Ciclo ${activeCycleFilter}`;
          filterStatusBadge.classList.remove('hidden');
        } else {
          filterStatusBadge.classList.add('hidden');
        }
      }
      
      if (geojsonMzasLayer) geojsonMzasLayer.setStyle(styleMzaFeature);
      if (geojsonRoutesLayer) geojsonRoutesLayer.setStyle(styleRouteFeature);
      
      if (activeCycleFilter !== 'all') {
        const cycleFeats = allRoutesFeatures.filter(f => String(f.properties.grupo_lectura) === String(activeCycleFilter));
        if (cycleFeats.length > 0) {
          const bounds = L.geoJSON({ type: 'FeatureCollection', features: cycleFeats }).getBounds();
          map.fitBounds(bounds, { padding: [40, 40] });
        }
      }
    });
  }

  // Selector de Modo de Color
  if (colorModeSelect) {
    colorModeSelect.addEventListener('change', (e) => {
      currentColorMode = e.target.value;
      if (geojsonMzasLayer) geojsonMzasLayer.setStyle(styleMzaFeature);
      if (geojsonRoutesLayer) geojsonRoutesLayer.setStyle(styleRouteFeature);
    });
  }

  // Selector de Capa Activa (Ambas, Solo Rutas, Solo Manzanas)
  if (layerModeSelect) {
    layerModeSelect.addEventListener('change', (e) => {
      currentLayerMode = e.target.value;
      if (geojsonMzasLayer) geojsonMzasLayer.setStyle(styleMzaFeature);
      if (geojsonRoutesLayer) geojsonRoutesLayer.setStyle(styleRouteFeature);
    });
  }

  // Buscador Instantáneo
  if (searchInput) {
    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const query = searchInput.value.trim().toUpperCase();
        if (!query) return;
        
        // 1. Buscar por Ruta (ej. "1042" o "RUTA 1042")
        const routeMatch = query.replace('RUTA', '').trim();
        const routeNum = parseInt(routeMatch, 10);
        if (!isNaN(routeNum)) {
          if (routesById.has(routeNum)) {
            const rFeat = routesById.get(routeNum);
            activeIsolatedRoute = routeNum;
            if (filterStatusBadge && filterStatusText) {
              filterStatusText.textContent = `Ruta ${routeNum}`;
              filterStatusBadge.classList.remove('hidden');
            }
            if (geojsonMzasLayer) geojsonMzasLayer.setStyle(styleMzaFeature);
            if (geojsonRoutesLayer) geojsonRoutesLayer.setStyle(styleRouteFeature);
            selectFeature(rFeat, true);
            const bounds = L.geoJSON(rFeat).getBounds();
            map.fitBounds(bounds, { padding: [60, 60], maxZoom: 17 });
            return;
          } else if (featuresByRouteMzas.has(routeNum)) {
            const routeFeats = featuresByRouteMzas.get(routeNum);
            activeIsolatedRoute = routeNum;
            if (filterStatusBadge && filterStatusText) {
              filterStatusText.textContent = `Ruta ${routeNum} (${routeFeats.length} mzas)`;
              filterStatusBadge.classList.remove('hidden');
            }
            if (geojsonMzasLayer) geojsonMzasLayer.setStyle(styleMzaFeature);
            if (geojsonRoutesLayer) geojsonRoutesLayer.setStyle(styleRouteFeature);
            selectFeature(routeFeats[0], false);
            const bounds = L.geoJSON({ type: 'FeatureCollection', features: routeFeats }).getBounds();
            map.fitBounds(bounds, { padding: [60, 60], maxZoom: 17 });
            return;
          }
        }
        
        // 2. Buscar por ID de Manzana
        if (featuresByMza.has(query)) {
          const feat = featuresByMza.get(query);
          selectFeature(feat, false);
          const bounds = L.geoJSON(feat).getBounds();
          map.fitBounds(bounds, { padding: [80, 80], maxZoom: 18 });
          return;
        }
        
        // 3. Buscar parcial por Calle
        const partial = allMzasFeatures.find(f => f.properties.c && f.properties.c.toUpperCase().includes(query));
        if (partial) {
          selectFeature(partial, false);
          const bounds = L.geoJSON(partial).getBounds();
          map.fitBounds(bounds, { padding: [80, 80], maxZoom: 18 });
          return;
        }
        
        alert(`No se encontró ninguna manzana o ruta para "${query}". Intente con un número de ruta (ej. 1042) o código catastral.`);
      }
    });
  }

  // Cargar datos
  function initializeLayers(mzasData, routesData) {
    allMzasFeatures = mzasData ? mzasData.features : [];
    allRoutesFeatures = routesData ? routesData.features : [];
    
    // Indexar manzanas
    allMzasFeatures.forEach(feat => {
      const p = feat.properties;
      featuresByMza.set(p.m.toUpperCase(), feat);
      if (!featuresByRouteMzas.has(p.r)) {
        featuresByRouteMzas.set(p.r, []);
      }
      featuresByRouteMzas.get(p.r).push(feat);
    });

    // Indexar rutas consolidadas
    const uniqueCycles = new Set();
    allRoutesFeatures.forEach(feat => {
      const p = feat.properties;
      routesById.set(parseInt(p.nueva_ruta_lectura, 10), feat);
      uniqueCycles.add(String(p.grupo_lectura));
    });

    if (cycleSelect) {
      cycleSelect.innerHTML = '<option value="all">Todos los Ciclos (1 al 20)</option>';
      const sortedCycles = Array.from(uniqueCycles).sort((a, b) => parseInt(a) - parseInt(b));
      sortedCycles.forEach(c => {
        const opt = document.createElement('option');
        opt.value = c;
        opt.textContent = `Ciclo / Grupo ${c}`;
        cycleSelect.appendChild(opt);
      });
    }

    // 1. Capa de Polígonos Consolidados de Rutas
    if (routesData) {
      geojsonRoutesLayer = L.geoJSON(routesData, {
        renderer: canvasRendererRoutes,
        style: styleRouteFeature,
        onEachFeature: (feature, layer) => {
          const p = feature.properties;
          layer.bindTooltip(`
            <div style="font-weight:700; color:#38bdf8; margin-bottom:2px;">Ruta ${p.nueva_ruta_lectura} (Grupo ${p.grupo_lectura})</div>
            <div style="font-size:0.75rem; color:#e2e8f0;">${p.cant_suministros} suministros • ${p.cant_manzanas} mzas</div>
            <div style="font-size:0.75rem; color:#94a3b8;">Compacidad: ${(p.compacidad_isoperimetrica || 0).toFixed(3)} • ${(p.area_hectareas || 0).toFixed(1)} ha</div>
          `, { className: 'custom-tooltip', sticky: true, direction: 'top' });

          layer.on({
            click: (e) => {
              L.DomEvent.stopPropagation(e);
              lastFeatureClickTime = Date.now();
              selectFeature(feature, true);
            },
            mouseover: () => { map.getContainer().style.cursor = 'pointer'; },
            mouseout: () => { map.getContainer().style.cursor = ''; }
          });
        }
      }).addTo(map);
    }

    // 2. Capa de Manzanas Catastrales
    if (mzasData) {
      geojsonMzasLayer = L.geoJSON(mzasData, {
        renderer: canvasRendererMzas,
        style: styleMzaFeature,
        onEachFeature: (feature, layer) => {
          const p = feature.properties;
          layer.bindTooltip(`
            <div style="font-weight:700; color:#38bdf8; margin-bottom:2px;">Ruta ${p.r} (Ciclo ${p.g})</div>
            <div style="font-size:0.75rem; color:#e2e8f0;">Mza: ${p.m}</div>
            <div style="font-size:0.75rem; color:#94a3b8;">${p.s} suministros</div>
          `, { className: 'custom-tooltip', sticky: true, direction: 'top' });

          layer.on({
            click: (e) => {
              L.DomEvent.stopPropagation(e);
              lastFeatureClickTime = Date.now();
              selectFeature(feature, false);
            },
            mouseover: () => { map.getContainer().style.cursor = 'pointer'; },
            mouseout: () => { map.getContainer().style.cursor = ''; }
          });
        }
      }).addTo(map);
    }

    if (loadingOverlay) {
      loadingOverlay.classList.add('hidden');
    }
  }

  // Comprobar variables de datos locales
  const mzasLoaded = (typeof MANZANAS_DATA !== 'undefined') ? MANZANAS_DATA : null;
  const routesLoaded = (typeof RUTAS_DATA !== 'undefined') ? RUTAS_DATA : null;

  if (mzasLoaded || routesLoaded) {
    if (loadingText) loadingText.textContent = 'Renderizando capas vectoriales en Canvas...';
    setTimeout(() => {
      initializeLayers(mzasLoaded, routesLoaded);
    }, 150);
  } else {
    if (loadingText) loadingText.textContent = 'Cargando datos desde disco...';
    Promise.all([
      fetch('data/manzanas_rutas_distrito1.geojson').then(r => r.json()).catch(() => null),
      fetch('data/rutas_nuevas_poligonos_distrito1.geojson').then(r => r.json()).catch(() => null)
    ]).then(([mzas, routes]) => {
      initializeLayers(mzas, routes);
    }).catch(err => {
      console.error('Error cargando GeoJSON:', err);
      if (loadingText) loadingText.innerHTML = `Error cargando datos.<br><span style="font-size:0.75rem; color:#ef4444;">${err.message}</span>`;
    });
  }
});
"""

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js_code)
print("✔ js/app.js escrito con éxito.")

print("✔ Actualización completada sin errores!")
