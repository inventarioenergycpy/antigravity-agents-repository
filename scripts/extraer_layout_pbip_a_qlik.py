# -*- coding: utf-8 -*-
"""
Script: extraer_layout_pbip_a_qlik.py
Objetivo: Analizar la estructura nativa PBIP de 'Tablero MI - Zona A' y extraer
las coordenadas, dimensiones, tipos de gráficos y títulos de cada página,
traduciéndolos automáticamente a una cuadrícula estándar de Qlik Sense (24 columnas x N filas).
"""

import os
import json

BASE_PBIP_DIR = r"D:\Usuarios\jidiaz\Downloads\Tablero MI - Zona A.Report\definition\pages"
PAGES_JSON_PATH = os.path.join(BASE_PBIP_DIR, "pages.json")

def extraer_titulo(vdata):
    try:
        title_objs = vdata.get("visual", {}).get("visualContainerObjects", {}).get("title", [])
        if title_objs:
            expr = title_objs[0].get("properties", {}).get("text", {}).get("expr", {})
            if "Literal" in expr:
                val = expr["Literal"].get("Value", "")
                return val.strip("'\"")
            elif "Measure" in expr:
                return "Medida: " + expr["Measure"].get("Property", "")
    except Exception:
        pass
    
    # Text box fallback
    try:
        text_props = vdata.get("visual", {}).get("objects", {}).get("text", [])
        for p in text_props:
            expr = p.get("properties", {}).get("text", {}).get("expr", {})
            if "Literal" in expr:
                val = expr["Literal"].get("Value", "")
                if val:
                    return val.strip("'\"")
    except Exception:
        pass
        
    return ""

def mapear_tipo_qlik(pbi_type):
    mapping = {
        "card": "kpi",
        "multiRowCard": "kpi",
        "matrix": "pivot-table",
        "pivotTable": "pivot-table",
        "tableEx": "table",
        "map": "map",
        "azureMap": "map",
        "shapeMap": "map",
        "barChart": "barchart",
        "columnChart": "barchart",
        "clusteredBarChart": "barchart",
        "clusteredColumnChart": "barchart",
        "hundredPercentStackedBarChart": "barchart",
        "hundredPercentStackedColumnChart": "barchart",
        "lineChart": "linechart",
        "lineClusteredColumnComboChart": "combochart",
        "lineStackedColumnComboChart": "combochart",
        "pieChart": "piechart",
        "donutChart": "piechart",
        "slicer": "filterpane",
        "textbox": "text-image",
        "shape": "text-image",
        "image": "text-image",
        "actionButton": "action-button"
    }
    return mapping.get(pbi_type, pbi_type)

def main():
    if not os.path.exists(PAGES_JSON_PATH):
        print(f"Error: no existe {PAGES_JSON_PATH}")
        return

    with open(PAGES_JSON_PATH, "r", encoding="utf-8") as f:
        pages_order = json.load(f).get("pageOrder", [])

    catalogo_completo = []

    for page_id in pages_order:
        page_dir = os.path.join(BASE_PBIP_DIR, page_id)
        page_json = os.path.join(page_dir, "page.json")
        if not os.path.exists(page_json):
            continue

        with open(page_json, "r", encoding="utf-8") as f:
            pdata = json.load(f)

        display_name = pdata.get("displayName", page_id)
        canvas_w = float(pdata.get("width", 1280))
        canvas_h = float(pdata.get("height", 720))

        page_record = {
            "page_id": page_id,
            "display_name": display_name,
            "canvas_width": canvas_w,
            "canvas_height": canvas_h,
            "qlik_grid_cols": 24,
            "visuals": []
        }

        # Grid unit calculation:
        # Standard Qlik Sense desktop is 24 columns wide.
        # Height: assume standard 12 rows for 720px (60px per row), or proportional.
        row_height_px = 60.0
        qlik_grid_rows = max(12, int(round(canvas_h / row_height_px)))
        page_record["qlik_grid_rows"] = qlik_grid_rows

        visuals_dir = os.path.join(page_dir, "visuals")
        if os.path.exists(visuals_dir):
            for vname in os.listdir(visuals_dir):
                vpath = os.path.join(visuals_dir, vname, "visual.json")
                if not os.path.exists(vpath):
                    continue

                with open(vpath, "r", encoding="utf-8") as vf:
                    vdata = json.load(vf)

                v_type = vdata.get("visual", {}).get("visualType", "unknown")
                pos = vdata.get("position", {})
                px = float(pos.get("x", 0))
                py = float(pos.get("y", 0))
                pw = float(pos.get("width", 100))
                ph = float(pos.get("height", 50))
                pz = int(pos.get("z", 0))

                title = extraer_titulo(vdata)
                qlik_type = mapear_tipo_qlik(v_type)

                # Mapeo a celdas Qlik Sense (Grilla de 24 columnas)
                col = max(0, min(23, int(round((px / canvas_w) * 24))))
                colspan = max(1, min(24 - col, int(round((pw / canvas_w) * 24))))

                row = max(0, int(round(py / row_height_px)))
                rowspan = max(1, int(round(ph / row_height_px)))

                visual_item = {
                    "id": vname,
                    "pbi_type": v_type,
                    "qlik_type": qlik_type,
                    "title": title,
                    "pbi_coords": {
                        "x": px,
                        "y": py,
                        "width": pw,
                        "height": ph,
                        "z": pz
                    },
                    "qlik_cell": {
                        "col": col,
                        "row": row,
                        "colspan": colspan,
                        "rowspan": rowspan
                    }
                }
                page_record["visuals"].append(visual_item)

        # Ordenar visuales por fila y luego columna
        page_record["visuals"].sort(key=lambda v: (v["qlik_cell"]["row"], v["qlik_cell"]["col"]))
        catalogo_completo.append(page_record)

    output_json = r"D:\Usuarios\jidiaz\Downloads\qlik_sense_sheets_layout_specification.json"
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(catalogo_completo, f, indent=2, ensure_ascii=False)
    print(f"Catalogo JSON generado con éxito: {output_json}")

    # Imprimir resumen de cada página
    for p in catalogo_completo:
        print(f"\n=======================================================")
        print(f"HOJA: {p['display_name']} ({p['canvas_width']}x{p['canvas_height']} px -> Grilla Qlik: 24x{p['qlik_grid_rows']})")
        print(f"=======================================================")
        for v in p["visuals"]:
            q = v["qlik_cell"]
            print(f"  [{v['qlik_type']:12s}] Grilla: Col={q['col']:2d}, Row={q['row']:2d}, Ancho={q['colspan']:2d}, Alto={q['rowspan']:2d} | PBI: {v['pbi_type']:15s} | Titulo: {v['title']}")

if __name__ == "__main__":
    main()
