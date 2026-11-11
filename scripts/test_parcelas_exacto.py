import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")

test_cases = [
    "nomenclatura = '11-01-01-02-12-033-047'",
    "nomenclatura = '1101010212033047'",
    "nomenclatura = '11-01-01-04-03-049-001'",
    "nomenclatura = '1101010403049001'"
]

for flt in test_cases:
    print(f"[*] Probando filtro exacto en vt_parcelas_union: {flt}")
    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typeName": "EPEC:vt_parcelas_union",
        "outputFormat": "application/json",
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
                print(f"    ID: {p.get('id')} | Nomenclatura: '{p.get('nomenclatura')}' | Parcela: '{p.get('parcela')}' | Lat: {p.get('latitud')} | Lon: {p.get('longitud')}")
                geom = f.get("geometry", {})
                print(f"    Geometria: Tipo {geom.get('type')}, vertices: {len(geom.get('coordinates', [[]])[0]) if geom else 0}")
    except Exception as e:
        print(f"  Error: {e}")
