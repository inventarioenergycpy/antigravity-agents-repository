import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")

# Probar cql_filter con prefijo de nomenclatura con guiones o sin guiones
test_filters = [
    "nomenclatura LIKE '11-01-01%'",
    "nomenclatura LIKE '110101%'",
    "id < 100"
]

for flt in test_filters:
    print(f"[*] Probando filtro en vt_parcelas_union: {flt}")
    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typeName": "EPEC:vt_parcelas_union",
        "outputFormat": "application/json",
        "maxFeatures": 2,
        "cql_filter": flt
    }
    try:
        resp = requests.get(url, auth=auth, params=params, verify=False, timeout=8)
        print(f"  Status: {resp.status_code}")
        if resp.status_code == 200:
            features = resp.json().get("features", [])
            print(f"  Encontradas: {len(features)}")
            for f in features:
                p = f.get("properties", {})
                print(f"    Nomenclatura: '{p.get('nomenclatura')}' | Parcela: '{p.get('parcela')}' | Lat: {p.get('latitud')} | Lon: {p.get('longitud')}")
            if features:
                break
    except Exception as e:
        print(f"  Error: {e}")
