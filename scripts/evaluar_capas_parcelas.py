import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")

capas_a_probar = [
    "EPEC:vt_parcelas_union",
    "EPEC:vm_vt_parcelas_union",
    "EPEC:vm_vt_parcelas_calles",
    "EPEC:vt_parcelas_muni_relevamiento",
    "EPEC:vt_parcelas_idecor_relevamiento",
    "EPEC:vm_v_parcelario_coord_gobcba"
]

print("=== EVALUANDO DISPONIBILIDAD DE CAPAS DE PARCELAS ===")
for capa in capas_a_probar:
    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typeName": capa,
        "outputFormat": "application/json",
        "maxFeatures": 1
    }
    try:
        resp = requests.get(url, auth=auth, params=params, verify=False, timeout=6)
        print(f"Capa {capa} -> Status {resp.status_code}")
        if resp.status_code == 200:
            feat = resp.json().get("features", [])
            if feat:
                print(f"   [+] OK! Properties: {list(feat[0].get('properties', {}).keys())[:6]}")
        else:
            print(f"   [-] Error: {resp.text[:150]}")
    except Exception as e:
        print(f"   [-] Timeout / Fallo: {e}")
