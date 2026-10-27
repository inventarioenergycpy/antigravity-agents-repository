import os
import json

base_dir = r"D:\Usuarios\jidiaz\Downloads\Tablero MI - Zona A.Report\definition\pages\ReportSectioncf0c0c9985bb2d9803d9\visuals"

for vname in os.listdir(base_dir):
    vpath = os.path.join(base_dir, vname, "visual.json")
    if not os.path.exists(vpath):
        continue
    with open(vpath, "r", encoding="utf-8") as f:
        d = json.load(f)
    v = d.get("visual", {})
    v_type = v.get("visualType")
    proj = v.get("visualContainerObjects", {})
    query = v.get("query", {})
    prototype_query = query.get("prototypeQuery", {})
    from_list = prototype_query.get("From", [])
    select_list = prototype_query.get("Select", [])
    
    print(f"Visual {vname} ({v_type}):")
    for s in select_list:
        if "Measure" in s:
            print(f"   - Measure: {s['Measure'].get('Property')} (from {s['Measure'].get('Expression', {}).get('SourceRef', {}).get('Entity')})")
        elif "Column" in s:
            print(f"   - Column: {s['Column'].get('Property')} (from {s['Column'].get('Expression', {}).get('SourceRef', {}).get('Entity')})")
        elif "HierarchyLevel" in s:
            print(f"   - Hierarchy: {s['HierarchyLevel'].get('Level')} of {s['HierarchyLevel'].get('Expression', {}).get('Hierarchy', {}).get('Hierarchy')}")
