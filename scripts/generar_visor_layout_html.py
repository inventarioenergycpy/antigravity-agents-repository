# -*- coding: utf-8 -*-
"""
Script: generar_visor_layout_html.py
Genera una Single Page Application (SPA) en HTML/CSS/JS autocontenida que renderiza
la cuadrícula exacta de 24 columnas de Qlik Sense para cada hoja, mostrando la disposición
equivalente al reporte de Power BI.
"""

import os
import json

JSON_SPEC_PATH = r"D:\Usuarios\jidiaz\Downloads\qlik_sense_sheets_layout_specification.json"
HTML_OUTPUT_SCRIPTS = r"C:\Users\jidiaz\.gemini\antigravity-ide\scratch\antigravity-agents-repository\scripts\viewer_layout_qlik.html"
HTML_OUTPUT_DOWNLOADS = r"D:\Usuarios\jidiaz\Downloads\viewer_layout_qlik.html"

def generar_html():
    with open(JSON_SPEC_PATH, "r", encoding="utf-8") as f:
        pages_data = json.load(f)

    # Embed JSON
    pages_json_str = json.dumps(pages_data, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Visor de Layout Qlik Sense - Tablero MI Zona A (Equivalencia Power BI)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-dark: #0f172a;
      --card-bg: #1e293b;
      --border-color: #334155;
      --primary: #38bdf8;
      --accent: #818cf8;
      --kpi-bg: #064e3b;
      --kpi-border: #10b981;
      --kpi-text: #a7f3d0;
      --pivot-bg: #3b0764;
      --pivot-border: #a855f7;
      --pivot-text: #e9d5ff;
      --table-bg: #1e3a8a;
      --table-border: #3b82f6;
      --table-text: #bfdbfe;
      --map-bg: #7c2d12;
      --map-border: #f97316;
      --map-text: #ffedd5;
      --chart-bg: #1e1b4b;
      --chart-border: #6366f1;
      --chart-text: #c7d2fe;
      --filter-bg: #1f2937;
      --filter-border: #6b7280;
      --filter-text: #e5e7eb;
      --shape-bg: #18181b;
      --shape-border: #52525b;
      --shape-text: #a1a1aa;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: 'Inter', sans-serif;
      background: var(--bg-dark);
      color: #f8fafc;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}
    header {{
      background: #090d16;
      border-bottom: 1px solid var(--border-color);
      padding: 16px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .brand-badge {{
      background: linear-gradient(135deg, #0284c7, #6366f1);
      padding: 6px 12px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 13px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    h1 {{
      font-size: 18px;
      font-weight: 700;
      color: #f1f5f9;
    }}
    .header-actions {{
      display: flex;
      gap: 12px;
    }}
    .btn {{
      background: #1e293b;
      border: 1px solid var(--border-color);
      color: #cbd5e1;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      text-decoration: none;
    }}
    .btn:hover {{
      background: #334155;
      color: #fff;
    }}
    .btn-primary {{
      background: #0284c7;
      border-color: #38bdf8;
      color: #fff;
    }}
    .btn-primary:hover {{
      background: #0369a1;
    }}

    /* Tabs */
    .tabs-bar {{
      background: #111827;
      border-bottom: 1px solid var(--border-color);
      padding: 8px 24px;
      display: flex;
      gap: 8px;
      overflow-x: auto;
    }}
    .tab-btn {{
      background: transparent;
      border: 1px solid transparent;
      color: #94a3b8;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }}
    .tab-btn:hover {{
      color: #f1f5f9;
      background: rgba(255, 255, 255, 0.05);
    }}
    .tab-btn.active {{
      background: #1e293b;
      border-color: #38bdf8;
      color: #38bdf8;
    }}

    /* Canvas / Workspace */
    .workspace {{
      flex: 1;
      padding: 24px;
      display: flex;
      gap: 24px;
      align-items: flex-start;
    }}
    .canvas-container {{
      flex: 1;
      background: #020617;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 10px 25px -5px rgba(0,0,0,0.5);
      overflow-x: auto;
    }}
    .canvas-info {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid #1e293b;
      font-size: 13px;
      color: #94a3b8;
    }}
    .grid-canvas {{
      display: grid;
      grid-template-columns: repeat(24, 1fr);
      gap: 8px;
      background: #0b1120;
      border: 1px dashed #1e293b;
      border-radius: 8px;
      padding: 8px;
      position: relative;
    }}

    /* Tiles / Cards */
    .grid-tile {{
      border-radius: 6px;
      padding: 10px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      cursor: pointer;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
      position: relative;
      overflow: hidden;
      border: 1px solid;
    }}
    .grid-tile:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 16px -2px rgba(0,0,0,0.6);
      z-index: 10;
    }}
    .grid-tile.selected {{
      outline: 2px solid #fff;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.8);
    }}

    /* Tipos */
    .tile-kpi {{ background: var(--kpi-bg); border-color: var(--kpi-border); color: var(--kpi-text); }}
    .tile-pivot-table {{ background: var(--pivot-bg); border-color: var(--pivot-border); color: var(--pivot-text); }}
    .tile-table {{ background: var(--table-bg); border-color: var(--table-border); color: var(--table-text); }}
    .tile-map {{ background: var(--map-bg); border-color: var(--map-border); color: var(--map-text); }}
    .tile-combochart, .tile-barchart, .tile-linechart {{ background: var(--chart-bg); border-color: var(--chart-border); color: var(--chart-text); }}
    .tile-filterpane, .tile-FilterByList507A2DBEC31244C8AAABDE9BA541F723 {{ background: var(--filter-bg); border-color: var(--filter-border); color: var(--filter-text); }}
    .tile-text-image, .tile-action-button {{ background: var(--shape-bg); border-color: var(--shape-border); color: var(--shape-text); }}

    .tile-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 4px;
      margin-bottom: 6px;
    }}
    .tile-type-badge {{
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      padding: 2px 6px;
      border-radius: 4px;
      background: rgba(0,0,0,0.4);
      letter-spacing: 0.3px;
    }}
    .tile-coords {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      opacity: 0.7;
    }}
    .tile-title {{
      font-size: 12px;
      font-weight: 700;
      line-height: 1.3;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .tile-metrics {{
      font-size: 10px;
      opacity: 0.85;
      margin-top: 6px;
      font-family: 'JetBrains Mono', monospace;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* Sidebar Inspector */
    .sidebar-inspector {{
      width: 360px;
      background: #0f172a;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      position: sticky;
      top: 90px;
      max-height: calc(100vh - 120px);
      overflow-y: auto;
    }}
    .inspector-title {{
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 16px;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .prop-group {{
      margin-bottom: 14px;
    }}
    .prop-label {{
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      color: #94a3b8;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }}
    .prop-value {{
      font-size: 13px;
      background: #1e293b;
      padding: 8px 12px;
      border-radius: 6px;
      border: 1px solid #334155;
      font-family: 'JetBrains Mono', monospace;
      color: #f1f5f9;
      word-break: break-all;
    }}
    .badge-code {{
      display: inline-block;
      background: #0284c7;
      color: white;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: bold;
    }}
    .legend-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 16px;
      padding-top: 16px;
      border-top: 1px solid #1e293b;
      font-size: 12px;
    }}
    .legend-item {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .legend-dot {{
      width: 12px;
      height: 12px;
      border-radius: 3px;
      border: 1px solid rgba(255,255,255,0.2);
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-left">
      <div class="brand-badge">Qlik Sense Grid 24 Cols</div>
      <h1>Blueprint de Disposición Visual: Tablero MI - Zona A</h1>
    </div>
    <div class="header-actions">
      <button class="btn" onclick="copiarJSON()">📋 Copiar JSON Bundle</button>
      <a class="btn btn-primary" href="qlik_sense_app_sheets_bundle.json" download="qlik_sense_app_sheets_bundle.json">📥 Descargar Bundle Qlik</a>
    </div>
  </header>

  <div class="tabs-bar" id="tabsBar"></div>

  <div class="workspace">
    <div class="canvas-container">
      <div class="canvas-info">
        <div>
          <strong id="activeSheetTitle" style="color: #f1f5f9; font-size: 15px;"></strong>
          <span id="activeSheetDims" style="margin-left: 12px;"></span>
        </div>
        <div>Grilla Qlik Sense: <strong>24 Columnas</strong> &times; <strong id="activeSheetRows"></strong> Filas</div>
      </div>
      <div class="grid-canvas" id="gridCanvas"></div>
      
      <div class="legend-bar">
        <div class="legend-item"><div class="legend-dot" style="background:var(--kpi-border)"></div> KPI Card</div>
        <div class="legend-item"><div class="legend-dot" style="background:var(--pivot-border)"></div> Pivot Table (Matriz)</div>
        <div class="legend-item"><div class="legend-dot" style="background:var(--table-border)"></div> Tabla Detalle</div>
        <div class="legend-item"><div class="legend-dot" style="background:var(--chart-border)"></div> Gráfico Combo / Barras</div>
        <div class="legend-item"><div class="legend-dot" style="background:var(--map-border)"></div> Mapa Georreferenciado</div>
        <div class="legend-item"><div class="legend-dot" style="background:var(--filter-border)"></div> Panel de Filtro / Slicer</div>
      </div>
    </div>

    <div class="sidebar-inspector" id="inspector">
      <div class="inspector-title">🔍 Inspector de Objeto Qlik</div>
      <div id="inspectorContent">
        <p style="color: #64748b; font-size: 13px;">Haz clic en cualquier gráfico de la grilla para inspeccionar sus coordenadas exactas, dimensiones y medidas de Qlik Sense.</p>
      </div>
    </div>
  </div>

  <script>
    const pagesData = {pages_json_str};
    let activePageIndex = 0;
    let activeVisual = null;

    function renderTabs() {{
      const bar = document.getElementById('tabsBar');
      bar.innerHTML = '';
      pagesData.forEach((p, idx) => {{
        const btn = document.createElement('button');
        btn.className = `tab-btn ${{idx === activePageIndex ? 'active' : ''}}`;
        btn.innerText = p.display_name;
        btn.onclick = () => {{
          activePageIndex = idx;
          activeVisual = null;
          renderTabs();
          renderCanvas();
          renderInspector(null);
        }};
        bar.appendChild(btn);
      }});
    }}

    function renderCanvas() {{
      const page = pagesData[activePageIndex];
      document.getElementById('activeSheetTitle').innerText = page.display_name;
      document.getElementById('activeSheetDims').innerText = `(Original PBI: ${{page.canvas_width}} &times; ${{page.canvas_height}} px)`;
      document.getElementById('activeSheetRows').innerText = page.qlik_grid_rows;

      const canvas = document.getElementById('gridCanvas');
      canvas.innerHTML = '';
      canvas.style.gridTemplateRows = `repeat(${{page.qlik_grid_rows}}, 54px)`;

      page.visuals.forEach((v) => {{
        const q = v.qlik_cell;
        const tile = document.createElement('div');
        tile.className = `grid-tile tile-${{v.qlik_type}} ${{activeVisual === v ? 'selected' : ''}}`;
        tile.style.gridColumn = `${{q.col + 1}} / span ${{q.colspan}}`;
        tile.style.gridRow = `${{q.row + 1}} / span ${{q.rowspan}}`;

        const titleText = v.title || v.pbi_type || 'Sin Título';
        const dimsText = (v.dims && v.dims.length) ? v.dims.map(d => d.split('.').pop()).join(', ') : '';
        const measText = (v.measures && v.measures.length) ? v.measures.join(', ') : '';

        tile.innerHTML = `
          <div>
            <div class="tile-header">
              <span class="tile-type-badge">${{v.qlik_type}}</span>
              <span class="tile-coords">C${{q.col}} R${{q.row}} [${{q.colspan}}x${{q.rowspan}}]</span>
            </div>
            <div class="tile-title" title="${{titleText}}">${{titleText}}</div>
          </div>
          <div class="tile-metrics" title="${{dimsText || measText}}">${{measText || dimsText || ''}}</div>
        `;

        tile.onclick = (e) => {{
          e.stopPropagation();
          activeVisual = v;
          renderCanvas();
          renderInspector(v);
        }};

        canvas.appendChild(tile);
      }});
    }}

    function renderInspector(v) {{
      const c = document.getElementById('inspectorContent');
      if (!v) {{
        c.innerHTML = '<p style="color: #64748b; font-size: 13px;">Haz clic en cualquier gráfico de la grilla para inspeccionar sus coordenadas exactas, dimensiones y medidas de Qlik Sense.</p>';
        return;
      }}
      const q = v.qlik_cell;
      const p = v.pbi_coords;
      c.innerHTML = `
        <div class="prop-group">
          <div class="prop-label">Título del Gráfico</div>
          <div class="prop-value" style="font-weight: 700; color: #38bdf8;">${{v.title || 'Sin Título'}}</div>
        </div>
        <div class="prop-group">
          <div class="prop-label">Tipo de Objeto Qlik Sense</div>
          <div class="prop-value"><span class="badge-code">${{v.qlik_type}}</span> (Origen PBI: ${{v.pbi_type}})</div>
        </div>
        <div class="prop-group">
          <div class="prop-label">Posición en Grilla Qlik (24 Cols)</div>
          <div class="prop-value">
            Columna Inicial: <strong>${{q.col}}</strong><br>
            Fila Inicial: <strong>${{q.row}}</strong><br>
            Ancho (Colspan): <strong>${{q.colspan}} columnas</strong><br>
            Alto (Rowspan): <strong>${{q.rowspan}} filas</strong>
          </div>
        </div>
        <div class="prop-group">
          <div class="prop-label">Coordenadas PBI Píxeles</div>
          <div class="prop-value">X=${{p.x.toFixed(0)}}px, Y=${{p.y.toFixed(0)}}px, W=${{p.width.toFixed(0)}}px, H=${{p.height.toFixed(0)}}px</div>
        </div>
        <div class="prop-group">
          <div class="prop-label">Dimensiones (${{v.dims ? v.dims.length : 0}})</div>
          <div class="prop-value">${{v.dims && v.dims.length ? v.dims.join('<br>') : '<em style="color:#64748b">Ninguna</em>'}}</div>
        </div>
        <div class="prop-group">
          <div class="prop-label">Medidas / Expresiones (${{v.measures ? v.measures.length : 0}})</div>
          <div class="prop-value">${{v.measures && v.measures.length ? v.measures.join('<br>') : '<em style="color:#64748b">Ninguna</em>'}}</div>
        </div>
      `;
    }}

    function copiarJSON() {{
      const jsonStr = JSON.stringify(pagesData, null, 2);
      navigator.clipboard.writeText(jsonStr).then(() => {{
        alert('¡Especificación JSON copiada al portapapeles!');
      }}).catch(err => {{
        console.error(err);
      }});
    }}

    // Iniciar
    renderTabs();
    renderCanvas();
  </script>
</body>
</html>
"""
    with open(HTML_OUTPUT_SCRIPTS, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(HTML_OUTPUT_DOWNLOADS, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Visor HTML generado en:")
    print(f"1. {HTML_OUTPUT_SCRIPTS}")
    print(f"2. {HTML_OUTPUT_DOWNLOADS}")

if __name__ == "__main__":
    generar_html()
