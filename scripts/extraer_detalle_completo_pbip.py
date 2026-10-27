# -*- coding: utf-8 -*-
"""
Script: extraer_detalle_completo_pbip.py
Extrae todas las dimensiones, medidas, títulos, coordenadas y tipos de cada visual.
"""

import os
import json

BASE_PBIP_DIR = r"D:\Usuarios\jidiaz\Downloads\Tablero MI - Zona A.Report\definition\pages"
PAGES_JSON_PATH = os.path.join(BASE_PBIP_DIR, "pages.json")

def parse_projections(query_state):
    dims = []
    measures = []
    
    for section_name, section_data in query_state.items():
        if not isinstance(section_data, dict):
            continue
        projs = section_data.get("projections", [])
        for p in projs:
            field = p.get("field", {})
            if "Column" in field:
                col_name = field["Column"].get("Property", "")
                entity = field["Column"].get("Expression", {}).get("SourceRef", {}).get("Entity", "")
                dims.append(f"{entity}.{col_name}" if entity else col_name)
            elif "Measure" in field:
                m_name = field["Measure"].get("Property", "")
                entity = field["Measure"].get("Expression", {}).get("SourceRef", {}).get("Entity", "")
                measures.append(f"{m_name}")
            elif "Aggregation" in field:
                agg = field["Aggregation"]
                func = agg.get("Function", 0)
                func_names = {0: "Sum", 1: "Avg", 2: "Count", 3: "Min", 4: "Max", 5: "DistinctCount"}
                fn = func_names.get(func, f"Func{func}")
                col_expr = agg.get("Expression", {}).get("Column", {})
                col_name = col_expr.get("Property", "")
                entity = col_expr.get("Expression", {}).get("SourceRef", {}).get("Entity", "")
                measures.append(f"{fn}({entity}.{col_name})")
            elif "HierarchyLevel" in field:
                level = field["HierarchyLevel"].get("Level", "")
                dims.append(level)
                
    return dims, measures

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

def main():
    with open(PAGES_JSON_PATH, "r", encoding="utf-8") as f:
        pages_order = json.load(f).get("pageOrder", [])

    for page_id in pages_order:
        page_dir = os.path.join(BASE_PBIP_DIR, page_id)
        page_json = os.path.join(page_dir, "page.json")
        if not os.path.exists(page_json):
            continue

        with open(page_json, "r", encoding="utf-8") as f:
            pdata = json.load(f)

        display_name = pdata.get("displayName", page_id)
        w = float(pdata.get("width", 1280))
        h = float(pdata.get("height", 720))
        print(f"\n=======================================================")
        print(f"PAGINA: {display_name} ({w}x{h})")
        print(f"=======================================================")

        visuals_dir = os.path.join(page_dir, "visuals")
        if not os.path.exists(visuals_dir):
            continue

        visuals = []
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
            
            # Grilla Qlik 24 col
            col = max(0, min(23, int(round((px / w) * 24))))
            colspan = max(1, min(24 - col, int(round((pw / w) * 24))))
            row = max(0, int(round(py / 60.0)))
            rowspan = max(1, int(round(ph / 60.0)))

            title = extraer_titulo(vdata)
            query_state = vdata.get("visual", {}).get("query", {}).get("queryState", {})
            dims, measures = parse_projections(query_state)

            visuals.append({
                "id": vname,
                "type": v_type,
                "title": title,
                "col": col,
                "row": row,
                "colspan": colspan,
                "rowspan": rowspan,
                "dims": dims,
                "measures": measures
            })

        visuals.sort(key=lambda x: (x["row"], x["col"]))
        for v in visuals:
            dims_str = f"Dims: {v['dims']}" if v['dims'] else ""
            meas_str = f"Meas: {v['measures']}" if v['measures'] else ""
            extra = " | ".join(filter(None, [dims_str, meas_str]))
            print(f"[{v['type']:15s}] Col={v['col']:2d}, Row={v['row']:2d}, W={v['colspan']:2d}, H={v['rowspan']:2d} | Title: '{v['title']}' | {extra}")

if __name__ == "__main__":
    main()
