import os

html_code = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EPEC - Visor Geoespacial de Manzanas y Rutas de Lectura (Distrito 1)</title>
    <!-- Leaflet CSS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
    <!-- Google Fonts: Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        body, html {
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-color: #0b0f19;
            color: #f1f5f9;
        }
        #map {
            width: 100%;
            height: 100%;
            z-index: 1;
            background: #090d16;
        }
        /* Cursor pointer for interactive canvas features */
        .leaflet-interactive {
            cursor: pointer !important;
        }
        /* Floating Glassmorphic Header */
        .header-bar {
            position: absolute;
            top: 14px;
            left: 16px;
            right: 16px;
            z-index: 1000;
            background: rgba(15, 23, 42, 0.90);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 12px;
            padding: 10px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.6);
            pointer-events: auto;
        }
        .header-title {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .header-title h1 {
            font-size: 15px;
            font-weight: 700;
            letter-spacing: -0.02em;
            color: #f8fafc;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .header-title span.badge {
            font-size: 11px;
            background: #1e293b;
            color: #38bdf8;
            padding: 2px 7px;
            border-radius: 6px;
            border: 1px solid rgba(56, 189, 248, 0.3);
            font-weight: 600;
        }
        .header-right {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .stats-pills {
            display: flex;
            gap: 8px;
            align-items: center;
        }
        .pill {
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 8px;
            padding: 3px 10px;
            font-size: 11px;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .pill strong {
            color: #38bdf8;
            font-weight: 700;
        }
        /* Selection Status Banner in Header */
        .header-selection-badge {
            display: flex;
            align-items: center;
            gap: 8px;
            background: rgba(2, 132, 199, 0.25);
            border: 1px solid #38bdf8;
            border-radius: 8px;
            padding: 4px 12px;
            font-size: 12px;
            color: #e0f2fe;
            animation: pulse-border 2s infinite ease-in-out;
        }
        @keyframes pulse-border {
            0%, 100% { border-color: #38bdf8; box-shadow: 0 0 8px rgba(56, 189, 248, 0.2); }
            50% { border-color: #7dd3fc; box-shadow: 0 0 16px rgba(56, 189, 248, 0.5); }
        }
        .btn-header-clear {
            background: #ef4444;
            border: none;
            color: #ffffff;
            border-radius: 5px;
            padding: 2px 8px;
            font-size: 11px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        .btn-header-clear:hover {
            background: #dc2626;
            transform: scale(1.03);
        }
        .hidden {
            display: none !important;
        }
        /* Floating Sidebar Controls */
        .sidebar {
            position: absolute;
            top: 72px;
            left: 16px;
            width: 330px;
            max-height: calc(100% - 90px);
            z-index: 1000;
            background: rgba(15, 23, 42, 0.92);
            backdrop-filter: blur(18px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 14px;
            padding: 14px;
            overflow-y: auto;
            box-shadow: 0 20px 30px -10px rgba(0, 0, 0, 0.7);
            display: flex;
            flex-direction: column;
            gap: 11px;
        }
        .sidebar h2 {
            font-size: 13px;
            font-weight: 700;
            letter-spacing: -0.01em;
            color: #e2e8f0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        /* Selection Box in Sidebar */
        .sidebar-selection-box {
            background: rgba(30, 41, 59, 0.95);
            border: 1px solid #38bdf8;
            border-radius: 8px;
            padding: 8px 10px;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .sidebar-selection-title {
            font-size: 11px;
            font-weight: 700;
            color: #38bdf8;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .btn-sidebar-clear {
            width: 100%;
            background: linear-gradient(135deg, #ef4444, #dc2626);
            border: 1px solid #f87171;
            color: #ffffff;
            padding: 6px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            box-shadow: 0 4px 10px rgba(239, 68, 68, 0.3);
        }
        .btn-sidebar-clear:hover {
            background: #b91c1c;
            transform: translateY(-1px);
        }
        .control-group {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        .control-group label {
            font-size: 11px;
            font-weight: 600;
            color: #94a3b8;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .search-box {
            width: 100%;
            background: #0f172a;
            border: 1px solid #334155;
            color: #f8fafc;
            padding: 7px 10px;
            border-radius: 7px;
            font-size: 12px;
            outline: none;
            transition: all 0.2s;
        }
        .search-box:focus {
            border-color: #38bdf8;
            box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
        }
        .select-custom {
            width: 100%;
            background: #0f172a;
            border: 1px solid #334155;
            color: #f8fafc;
            padding: 6px 9px;
            border-radius: 7px;
            font-size: 12px;
            outline: none;
            cursor: pointer;
        }
        .select-custom:focus {
            border-color: #38bdf8;
        }
        .filter-buttons {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 6px;
        }
        .btn-filter, .btn-filter-area {
            background: #1e293b;
            border: 1px solid #334155;
            color: #cbd5e1;
            padding: 5px 8px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-filter:hover, .btn-filter-area:hover {
            background: #334155;
        }
        .btn-filter.active, .btn-filter-area.active {
            background: #0284c7;
            color: #ffffff;
            border-color: #38bdf8;
        }
        .opacity-slider {
            width: 100%;
            accent-color: #38bdf8;
            cursor: pointer;
        }
        /* Custom Leaflet Popup */
        .leaflet-popup-content-wrapper {
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(12px);
            color: #f8fafc;
            border: 1px solid rgba(56, 189, 248, 0.3);
            border-radius: 12px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.7);
        }
        .leaflet-popup-tip {
            background: rgba(15, 23, 42, 0.95);
        }
        .popup-card {
            padding: 4px;
            font-size: 12px;
            min-width: 220px;
        }
        .popup-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #334155;
            padding-bottom: 5px;
            margin-bottom: 6px;
        }
        .popup-title {
            font-size: 13px;
            font-weight: 700;
            color: #38bdf8;
        }
        .popup-badge {
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 700;
        }
        .badge-optimo { background: rgba(16, 185, 129, 0.2); color: #10b981; border: 1px solid #10b981; }
        .badge-sub { background: rgba(245, 158, 11, 0.2); color: #f59e0b; border: 1px solid #f59e0b; }
        .badge-sobre { background: rgba(239, 68, 68, 0.2); color: #ef4444; border: 1px solid #ef4444; }
        .popup-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 3px;
        }
        .popup-row span.label { color: #94a3b8; }
        .popup-row span.val { font-weight: 600; color: #f1f5f9; }
        
        /* Floating Nav Toolbar: Positioned cleanly to the right of sidebar */
        .nav-toolbar {
            position: absolute;
            top: 72px;
            left: 356px;
            z-index: 1000;
            display: flex;
            flex-direction: column;
            gap: 6px;
            background: rgba(15, 23, 42, 0.90);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 8px;
            padding: 4px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
        }
        .btn-nav {
            width: 32px;
            height: 32px;
            border: none;
            background: transparent;
            color: #f1f5f9;
            border-radius: 6px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 15px;
            font-weight: 700;
            transition: all 0.2s;
        }
        .btn-nav:hover {
            background: #334155;
            color: #38bdf8;
        }
        .btn-nav-clear {
            color: #f87171 !important;
        }
        .btn-nav-clear:hover {
            background: rgba(239, 68, 68, 0.25) !important;
            color: #ffffff !important;
        }
        /* Custom Tooltip */
        .custom-tooltip {
            background: rgba(15, 23, 42, 0.92) !important;
            border: 1px solid #38bdf8 !important;
            border-radius: 6px !important;
            color: #f8fafc !important;
            font-size: 11px !important;
            padding: 4px 8px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4) !important;
            pointer-events: none !important;
        }
    </style>
</head>
<body>
    <div id="map"></div>

    <!-- Floating Navigation Toolbar -->
    <div class="nav-toolbar">
        <button id="btn-zoom-in" class="btn-nav" title="Acercar mapa (+)">+</button>
        <button id="btn-zoom-out" class="btn-nav" title="Alejar mapa (−)">−</button>
        <button id="btn-fit-district" class="btn-nav" title="Centrar todo el Distrito 1">⛶</button>
        <button id="btn-clear-selection-nav" class="btn-nav btn-nav-clear" title="Borrar selección de ruta (Esc)">✕</button>
    </div>

    <!-- Header Glassmorphic Bar -->
    <div class="header-bar">
        <div class="header-title">
            <h1>⚡ EPEC | SIGEC <span style="font-weight:400; color:#94a3b8;">• Manzanas & Rutas</span></h1>
            <span class="badge">Distrito 1 • Córdoba</span>
        </div>

        <div class="header-right">
            <!-- Active Selection Banner in Header -->
            <div id="header-selection-badge" class="header-selection-badge hidden">
                <span>📍 <strong id="header-selected-route">Ruta -</strong></span>
                <button id="btn-header-clear" class="btn-header-clear" title="Quitar selección y ver todas las rutas (Esc)">✕ Borrar Selección</button>
            </div>

            <div class="stats-pills">
                <div class="pill">Mzas: <strong id="kpi-mzas">18.721</strong></div>
                <div class="pill">Rutas: <strong id="kpi-rutas">3.299</strong></div>
                <div class="pill">Suministros: <strong id="kpi-sumis">585.727</strong></div>
                <div class="pill">Mediana: <strong id="kpi-mediana">185 u.</strong></div>
                <div class="pill">Óptimas: <strong id="kpi-optimas" style="color: #10b981;">62.5%</strong></div>
            </div>
        </div>
    </div>

    <!-- Sidebar Floating Controls -->
    <div class="sidebar">
        <h2>Panel de Filtros & Control <span id="visible-count" style="color:#38bdf8; font-weight:700;">(3.299)</span></h2>

        <!-- Selection Banner in Sidebar -->
        <div id="sidebar-selection-box" class="sidebar-selection-box hidden">
            <div class="sidebar-selection-title">
                <span>📍 Filtro Activo: <strong id="sidebar-selected-text">Ruta -</strong></span>
            </div>
            <button id="btn-sidebar-clear" class="btn-sidebar-clear" title="Borrar selección y restaurar todas las rutas (Esc)">
                ✕ Borrar Selección de Ruta
            </button>
        </div>

        <!-- Layer Mode Selector -->
        <div class="control-group">
            <label>🗺️ Capa Territorial Visible</label>
            <select id="layer-mode" class="select-custom">
                <option value="mzas" selected>🎨 Manzanas por Ruta Nueva (18.721 mzas)</option>
                <option value="both">🔲 Ambas (Manzanas + Rutas Separadas)</option>
                <option value="routes">🔷 Polígonos de Rutas Separados (17.954 partes)</option>
            </select>
        </div>

        <!-- Surface Area Filter: <= 10 ha vs > 10 ha -->
        <div class="control-group">
            <label>📐 Superficie de Polígono (Separar > 10 ha)</label>
            <div class="filter-buttons">
                <button class="btn-filter-area active" data-area="ALL">Todos</button>
                <button class="btn-filter-area" data-area="COMPACT" title="Mostrar sólo polígonos compactos <= 10 ha">Compactos (≤ 10 ha)</button>
                <button class="btn-filter-area" data-area="MACRO" title="Mostrar polígonos extensos > 10 ha">Extensos (> 10 ha)</button>
            </div>
        </div>

        <!-- Search Input -->
        <div class="control-group">
            <label for="route-search">🔍 Buscar Ruta, Mza o Calle</label>
            <input type="text" id="route-search" class="search-box" placeholder="Ej: 1042, 01-01-001, COLON...">
        </div>

        <!-- Cycle / Group Selector -->
        <div class="control-group">
            <label for="group-select">📅 Grupo de Lectura (Ciclo 1 al 20)</label>
            <select id="group-select" class="select-custom">
                <option value="ALL">Todos los Grupos (1 al 20)</option>
                <option value="1">Grupo 1 (159 rutas)</option>
                <option value="2">Grupo 2 (102 rutas)</option>
                <option value="3">Grupo 3 (207 rutas)</option>
                <option value="4">Grupo 4 (131 rutas)</option>
                <option value="5">Grupo 5 (152 rutas)</option>
                <option value="6">Grupo 6 (67 rutas)</option>
                <option value="7">Grupo 7 (140 rutas)</option>
                <option value="8">Grupo 8 (162 rutas)</option>
                <option value="9">Grupo 9 (96 rutas)</option>
                <option value="10">Grupo 10 (94 rutas)</option>
                <option value="11">Grupo 11 (135 rutas)</option>
                <option value="12">Grupo 12 (123 rutas)</option>
                <option value="13">Grupo 13 (183 rutas)</option>
                <option value="14">Grupo 14 (300 rutas)</option>
                <option value="15">Grupo 15 (193 rutas)</option>
                <option value="16">Grupo 16 (273 rutas)</option>
                <option value="17">Grupo 17 (206 rutas)</option>
                <option value="18">Grupo 18 (180 rutas)</option>
                <option value="19">Grupo 19 (171 rutas)</option>
                <option value="20">Grupo 20 (225 rutas)</option>
            </select>
        </div>

        <!-- Capacity Filter -->
        <div class="control-group">
            <label>⚖️ Capacidad Operativa (Suministros)</label>
            <div class="filter-buttons">
                <button class="btn-filter active" data-cap="ALL">Todas</button>
                <button class="btn-filter" data-cap="SI" style="color:#10b981;">Óptimas (160-200)</button>
                <button class="btn-filter" data-cap="SUB" style="color:#f59e0b;">Subcarga (&lt;160)</button>
                <button class="btn-filter" data-cap="SOBRE" style="color:#ef4444;">Sobrecarga (&gt;200)</button>
            </div>
        </div>

        <!-- Base Map Selector (Sin Bloqueos 403) -->
        <div class="control-group">
            <label>🗺️ Mapa Base</label>
            <select id="basemap-select" class="select-custom">
                <option value="esri_calles" selected>ESRI Calles del Mundo (Recomendado - Sin Marcas)</option>
                <option value="voyager">OpenStreetMap (Voyager)</option>
                <option value="dark">CartoDB Dark Matter (Nocturno)</option>
                <option value="light">CartoDB Positron (Claro)</option>
                <option value="esri_sat">Esri Satelital (Alta Resolución)</option>
            </select>
        </div>

        <!-- Opacity Slider -->
        <div class="control-group">
            <label for="opacity-range">Opacidad de Relleno: <span id="opacity-val">0.70</span></label>
            <input type="range" id="opacity-range" class="opacity-slider" min="0.1" max="1.0" step="0.05" value="0.70">
        </div>
    </div>

    <!-- Leaflet JS -->
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
    
    <!-- Local JS Data Sources (CORS-free) -->
    <script src="data/manzanas_rutas_data.js"></script>
    <script src="data/rutas_poligonos_data.js"></script>

    <script>
    document.addEventListener('DOMContentLoaded', () => {
        const mzasData = (typeof MANZANAS_DATA !== 'undefined') ? MANZANAS_DATA : null;
        const rutasData = (typeof RUTAS_DATA !== 'undefined') ? RUTAS_DATA : null;

        // Paleta Áurea Determinística para Rutas (3.300 colores armónicos)
        function getRouteColor(routeId) {
            if (!routeId || routeId === 0) return '#64748b';
            const num = parseInt(routeId, 10);
            const hue = (!isNaN(num) ? (num * 137.507764) : 200) % 360;
            return `hsl(${hue.toFixed(1)}, 84%, 55%)`;
        }

        // 1. Inicializar Mapa con preferCanvas
        const map = L.map('map', {
            center: [-31.4201, -64.1888],
            zoom: 13,
            minZoom: 10,
            maxZoom: 19,
            zoomControl: false,
            preferCanvas: true
        });

        // UNICO Canvas Renderer Compartido (Evita conflicto de múltiples canvas overlays en DOM)
        const sharedCanvasRenderer = L.canvas({ padding: 0.5, tolerance: 6 });

        // Deshabilitar propagación de clics y arrastres sobre UI flotante
        [
            document.querySelector('.nav-toolbar'),
            document.querySelector('.sidebar'),
            document.querySelector('.header-bar')
        ].forEach(el => {
            if (el) {
                L.DomEvent.disableClickPropagation(el);
                L.DomEvent.disableScrollPropagation(el);
            }
        });

        // Mapas Base
        const basemaps = {
            esri_calles: L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
                maxZoom: 19,
                attribution: 'Tiles &copy; Esri &mdash; World Street Map'
            }),
            voyager: L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
                maxZoom: 19,
                attribution: '&copy; OpenStreetMap contributors &copy; CARTO'
            }),
            dark: L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
                maxZoom: 19,
                attribution: '&copy; OpenStreetMap &copy; CARTO'
            }),
            light: L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
                maxZoom: 19,
                attribution: '&copy; OpenStreetMap &copy; CARTO'
            }),
            esri_sat: L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
                maxZoom: 19,
                attribution: 'Tiles &copy; Esri &mdash; World Imagery'
            })
        };

        basemaps.esri_calles.addTo(map);
        let currentBasemap = basemaps.esri_calles;

        document.getElementById('basemap-select').addEventListener('change', (e) => {
            const key = e.target.value;
            if (basemaps[key]) {
                map.removeLayer(currentBasemap);
                basemaps[key].addTo(map);
                currentBasemap = basemaps[key];
            }
        });

        // Capa de Resalte (utiliza sharedCanvasRenderer con interactive: false)
        const highlightLayer = L.geoJSON(null, {
            renderer: sharedCanvasRenderer,
            interactive: false,
            style: { color: '#38bdf8', weight: 4.0, fillColor: '#0284c7', fillOpacity: 0.85, dashArray: '4, 4' }
        }).addTo(map);

        // Estados de Filtros
        let currentLayerMode = 'mzas'; // 'mzas', 'both', 'routes'
        let currentAreaFilter = 'ALL'; // 'ALL', 'COMPACT' (<=10ha), 'MACRO' (>10ha)
        let currentGroupFilter = 'ALL';
        let currentCapFilter = 'ALL';
        let currentOpacity = 0.70;
        let activeIsolatedRoute = null;

        // Elementos de Selección
        const headerSelectionBadge = document.getElementById('header-selection-badge');
        const headerSelectedRoute = document.getElementById('header-selected-route');
        const btnHeaderClear = document.getElementById('btn-header-clear');

        const sidebarSelectionBox = document.getElementById('sidebar-selection-box');
        const sidebarSelectedText = document.getElementById('sidebar-selected-text');
        const btnSidebarClear = document.getElementById('btn-sidebar-clear');

        const btnNavClear = document.getElementById('btn-clear-selection-nav');

        function setSelection(routeId) {
            activeIsolatedRoute = routeId;
            if (routeId !== null) {
                const txt = `Ruta ${routeId}`;
                if (headerSelectedRoute) headerSelectedRoute.textContent = txt;
                if (headerSelectionBadge) headerSelectionBadge.classList.remove('hidden');

                if (sidebarSelectedText) sidebarSelectedText.textContent = txt;
                if (sidebarSelectionBox) sidebarSelectionBox.classList.remove('hidden');
            } else {
                clearSelection();
            }
            updateStyles();
        }

        function clearSelection() {
            activeIsolatedRoute = null;
            highlightLayer.clearLayers();
            if (headerSelectionBadge) headerSelectionBadge.classList.add('hidden');
            if (sidebarSelectionBox) sidebarSelectionBox.classList.add('hidden');
            map.getContainer().style.cursor = '';
            updateStyles();
        }

        // Conectar botones de Borrar Selección
        [btnHeaderClear, btnSidebarClear, btnNavClear].forEach(btn => {
            if (btn) {
                btn.addEventListener('click', (e) => {
                    L.DomEvent.stopPropagation(e);
                    L.DomEvent.preventDefault(e);
                    clearSelection();
                });
            }
        });

        // Clic en área vacía del mapa deselecciona
        map.on('click', () => {
            clearSelection();
        });

        // Verificadores de visibilidad
        function isMzaVisible(p) {
            if (currentLayerMode === 'routes') return false;
            if (currentGroupFilter !== 'ALL' && String(p.g) !== currentGroupFilter) return false;
            return true;
        }

        function isRouteVisible(p) {
            if (currentLayerMode === 'mzas') return false;
            if (currentGroupFilter !== 'ALL' && String(p.grupo_lectura) !== currentGroupFilter) return false;
            
            const cant = p.cant_suministros || 0;
            if (currentCapFilter === 'SI' && (cant < 160 || cant > 200)) return false;
            if (currentCapFilter === 'SUB' && cant >= 160) return false;
            if (currentCapFilter === 'SOBRE' && cant <= 200) return false;

            const ha = p.area_hectareas || 0;
            const esMacro = (ha > 10.0);
            if (currentAreaFilter === 'COMPACT' && esMacro) return false;
            if (currentAreaFilter === 'MACRO' && !esMacro) return false;

            return true;
        }

        // Estilos para Manzanas Catastrales
        // IMPORTANTE: Cuando hay una ruta aislada, las demás manzanas conservan fillOpacity: 0.08
        // para que Leaflet Canvas SIEMPRE las mantenga clickeables y con cursor pointer.
        function styleMza(feature) {
            const p = feature.properties;
            const visible = isMzaVisible(p);

            if (!visible) {
                return { renderer: sharedCanvasRenderer, fillColor: 'transparent', fillOpacity: 0, color: 'transparent', weight: 0 };
            }

            const rId = p.r;
            const isIsolated = (activeIsolatedRoute !== null);
            const matchesIsolated = (rId === activeIsolatedRoute);

            if (isIsolated && !matchesIsolated) {
                return {
                    renderer: sharedCanvasRenderer,
                    fillColor: '#64748b',
                    fillOpacity: 0.08, // Mantiene la interactividad en Canvas
                    color: '#94a3b8',
                    weight: 0.3
                };
            }

            const color = getRouteColor(rId);
            return {
                renderer: sharedCanvasRenderer,
                fillColor: color,
                fillOpacity: isIsolated ? 0.90 : currentOpacity,
                color: isIsolated ? '#0f172a' : '#334155',
                weight: isIsolated ? 2.5 : 0.8
            };
        }

        // Estilos para Polígonos Separados de Rutas
        function styleRoute(feature) {
            const p = feature.properties;
            const visible = isRouteVisible(p);

            if (!visible) {
                return { renderer: sharedCanvasRenderer, fillColor: 'transparent', fillOpacity: 0, color: 'transparent', weight: 0 };
            }

            const rId = p.nueva_ruta_lectura;
            const ha = p.area_hectareas || 0;
            const esMacro = (ha > 10.0);
            const isIsolated = (activeIsolatedRoute !== null);
            const matchesIsolated = (rId === activeIsolatedRoute);

            if (isIsolated && !matchesIsolated) {
                return {
                    renderer: sharedCanvasRenderer,
                    fillColor: '#475569',
                    fillOpacity: 0.08, // Mantiene la interactividad en Canvas
                    color: '#64748b',
                    weight: 0.4
                };
            }

            const color = getRouteColor(rId);
            const isBoth = (currentLayerMode === 'both');

            return {
                renderer: sharedCanvasRenderer,
                fillColor: isBoth ? 'transparent' : color,
                fillOpacity: isBoth ? 0 : (esMacro ? 0.20 : currentOpacity),
                color: esMacro ? '#f59e0b' : (isBoth ? '#38bdf8' : '#ffffff'),
                weight: esMacro ? 2.5 : (isBoth ? 2.0 : 1.2),
                dashArray: esMacro ? '6, 6' : (isBoth ? '4, 4' : null)
            };
        }

        let geojsonMzasLayer = null;
        let geojsonRoutesLayer = null;

        // Construir capas sobre el mismo renderer compartido
        if (rutasData) {
            geojsonRoutesLayer = L.geoJSON(rutasData, {
                renderer: sharedCanvasRenderer,
                style: styleRoute,
                onEachFeature: (feature, layer) => {
                    const p = feature.properties;
                    const ha = p.area_hectareas || 0;
                    const esMacro = (ha > 10.0);
                    const tagMacro = esMacro ? '<span style="color:#f59e0b; font-weight:700;">⚠️ Extenso (>10 ha)</span>' : '<span style="color:#10b981;">Compacto</span>';
                    
                    layer.bindTooltip(`
                        <div style="font-weight:700; color:#38bdf8;">${p.etiqueta_parte || ('Ruta ' + p.nueva_ruta_lectura)}</div>
                        <div style="color:#f1f5f9;">Grupo ${p.grupo_lectura} • ${p.cant_suministros} sumis</div>
                        <div style="font-size:10px; color:#cbd5e1;">Sup: ${ha.toFixed(2)} ha • ${tagMacro}</div>
                    `, { className: 'custom-tooltip', sticky: true });

                    layer.on({
                        click: (e) => {
                            if (!isRouteVisible(p)) return;
                            L.DomEvent.stopPropagation(e);
                            highlightLayer.clearLayers();
                            highlightLayer.addData(feature);
                            setSelection(p.nueva_ruta_lectura);
                        },
                        mouseover: () => {
                            if (isRouteVisible(p)) {
                                map.getContainer().style.cursor = 'pointer';
                            }
                        },
                        mouseout: () => {
                            map.getContainer().style.cursor = '';
                        }
                    });
                }
            });
        }

        if (mzasData) {
            geojsonMzasLayer = L.geoJSON(mzasData, {
                renderer: sharedCanvasRenderer,
                style: styleMza,
                onEachFeature: (feature, layer) => {
                    const p = feature.properties;
                    layer.bindTooltip(`
                        <div style="font-weight:700; color:#38bdf8;">Ruta ${p.r} (Ciclo ${p.g})</div>
                        <div style="color:#f1f5f9;">Mza: ${p.m} • ${p.s} suministros</div>
                        <div style="font-size:10px; color:#94a3b8;">${(p.c || '').split('|').slice(0, 2).join(' - ')}</div>
                    `, { className: 'custom-tooltip', sticky: true });

                    layer.on({
                        click: (e) => {
                            if (!isMzaVisible(p)) return;
                            L.DomEvent.stopPropagation(e);
                            highlightLayer.clearLayers();
                            highlightLayer.addData(feature);
                            setSelection(p.r);
                        },
                        mouseover: () => {
                            if (isMzaVisible(p)) {
                                map.getContainer().style.cursor = 'pointer';
                            }
                        },
                        mouseout: () => {
                            map.getContainer().style.cursor = '';
                        }
                    });
                }
            });
        }

        // Función para sincronizar capas en el mapa según el modo
        function updateLayerVisibility() {
            if (currentLayerMode === 'mzas') {
                if (geojsonRoutesLayer && map.hasLayer(geojsonRoutesLayer)) map.removeLayer(geojsonRoutesLayer);
                if (geojsonMzasLayer && !map.hasLayer(geojsonMzasLayer)) map.addLayer(geojsonMzasLayer);
            } else if (currentLayerMode === 'routes') {
                if (geojsonMzasLayer && map.hasLayer(geojsonMzasLayer)) map.removeLayer(geojsonMzasLayer);
                if (geojsonRoutesLayer && !map.hasLayer(geojsonRoutesLayer)) map.addLayer(geojsonRoutesLayer);
            } else if (currentLayerMode === 'both') {
                if (geojsonRoutesLayer && !map.hasLayer(geojsonRoutesLayer)) map.addLayer(geojsonRoutesLayer);
                if (geojsonMzasLayer && !map.hasLayer(geojsonMzasLayer)) map.addLayer(geojsonMzasLayer);
            }
            updateStyles();
        }

        function updateStyles() {
            if (geojsonMzasLayer && map.hasLayer(geojsonMzasLayer)) geojsonMzasLayer.setStyle(styleMza);
            if (geojsonRoutesLayer && map.hasLayer(geojsonRoutesLayer)) geojsonRoutesLayer.setStyle(styleRoute);
        }

        // Inicializar capas
        updateLayerVisibility();

        // Eventos de Controles
        document.getElementById('layer-mode').addEventListener('change', (e) => {
            currentLayerMode = e.target.value;
            updateLayerVisibility();
        });

        // Filtro de Superficie (Separar > 10 ha)
        document.querySelectorAll('.btn-filter-area').forEach(btn => {
            btn.addEventListener('click', (e) => {
                L.DomEvent.stopPropagation(e);
                document.querySelectorAll('.btn-filter-area').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentAreaFilter = btn.getAttribute('data-area');
                updateStyles();
            });
        });

        // Filtro de Grupo de Lectura
        document.getElementById('group-select').addEventListener('change', (e) => {
            currentGroupFilter = e.target.value;
            clearSelection();
            
            // Auto-encuadrar en el grupo seleccionado
            if (currentGroupFilter !== 'ALL') {
                if (currentLayerMode === 'mzas' && mzasData) {
                    const gFeats = mzasData.features.filter(f => String(f.properties.g) === currentGroupFilter);
                    if (gFeats.length > 0) {
                        const bounds = L.geoJSON({ type: 'FeatureCollection', features: gFeats }).getBounds();
                        map.fitBounds(bounds, { padding: [50, 50], maxZoom: 15 });
                    }
                } else if (rutasData) {
                    const gFeats = rutasData.features.filter(f => String(f.properties.grupo_lectura) === currentGroupFilter);
                    if (gFeats.length > 0) {
                        const bounds = L.geoJSON({ type: 'FeatureCollection', features: gFeats }).getBounds();
                        map.fitBounds(bounds, { padding: [50, 50], maxZoom: 15 });
                    }
                }
            }
        });

        // Filtro de Capacidad
        document.querySelectorAll('.btn-filter').forEach(btn => {
            btn.addEventListener('click', (e) => {
                L.DomEvent.stopPropagation(e);
                document.querySelectorAll('.btn-filter').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentCapFilter = btn.getAttribute('data-cap');
                updateStyles();
            });
        });

        // Slider de Opacidad
        const opacityRange = document.getElementById('opacity-range');
        const opacityVal = document.getElementById('opacity-val');
        opacityRange.addEventListener('input', (e) => {
            currentOpacity = parseFloat(e.target.value);
            opacityVal.textContent = currentOpacity.toFixed(2);
            updateStyles();
        });

        // Buscador
        const routeSearch = document.getElementById('route-search');
        routeSearch.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                const query = routeSearch.value.trim().toUpperCase();
                if (!query) return;

                const rNum = parseInt(query.replace('RUTA', '').trim(), 10);
                if (!isNaN(rNum)) {
                    if (rutasData) {
                        const matchFeats = rutasData.features.filter(f => f.properties.nueva_ruta_lectura === rNum);
                        if (matchFeats.length > 0) {
                            setSelection(rNum);
                            const bounds = L.geoJSON({ type: 'FeatureCollection', features: matchFeats }).getBounds();
                            map.fitBounds(bounds, { padding: [60, 60], maxZoom: 17 });
                            highlightLayer.clearLayers();
                            matchFeats.forEach(f => highlightLayer.addData(f));
                            return;
                        }
                    }
                    if (mzasData) {
                        const matchMzas = mzasData.features.filter(f => f.properties.r === rNum);
                        if (matchMzas.length > 0) {
                            setSelection(rNum);
                            const bounds = L.geoJSON({ type: 'FeatureCollection', features: matchMzas }).getBounds();
                            map.fitBounds(bounds, { padding: [60, 60], maxZoom: 17 });
                            highlightLayer.clearLayers();
                            matchMzas.forEach(f => highlightLayer.addData(f));
                            return;
                        }
                    }
                }
            }
        });

        // Botones de Navegación Toolbar
        document.getElementById('btn-zoom-in').addEventListener('click', (e) => {
            L.DomEvent.stopPropagation(e);
            map.zoomIn();
        });
        document.getElementById('btn-zoom-out').addEventListener('click', (e) => {
            L.DomEvent.stopPropagation(e);
            map.zoomOut();
        });
        document.getElementById('btn-fit-district').addEventListener('click', (e) => {
            L.DomEvent.stopPropagation(e);
            if (geojsonMzasLayer && map.hasLayer(geojsonMzasLayer)) map.fitBounds(geojsonMzasLayer.getBounds(), { padding: [20, 20] });
            else if (geojsonRoutesLayer && map.hasLayer(geojsonRoutesLayer)) map.fitBounds(geojsonRoutesLayer.getBounds(), { padding: [20, 20] });
            else map.setView([-31.4201, -64.1888], 13);
        });

        // Teclado Esc
        window.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                clearSelection();
            }
        });
    });
    </script>
</body>
</html>
"""

# Guardar en D: y C:
dst_d = r"D:\Usuarios\jidiaz\Downloads\visor_rutas_poligonos_distrito1.html"
dst_c = r"C:\Users\jidiaz\Downloads\visor_rutas_poligonos_distrito1.html"

for path in [dst_d, dst_c]:
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_code)
    print(f"Visor guardado con single canvas y conmutación limpia: {path}")

print("Solución definitiva aplicada.")
