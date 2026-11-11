import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")
params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typeName": "EPEC:vt_parcelas_union",
    "outputFormat": "application/json",
    "cql_filter": "nomenclatura = '11-01-01-04-03-049-018'"
}

try:
    resp = requests.get(url, auth=auth, params=params, verify=False, timeout=12)
    print("Status:", resp.status_code)
    if resp.status_code == 200:
        data = resp.json()
        print("Features encontradas:", len(data.get("features", [])))
        for f in data.get("features", []):
            print("Properties:", f.get("properties"))
            geom = f.get("geometry", {})
            print("Geometry type:", geom.get("type"))
            coords = geom.get("coordinates", [])
            print("Coordinates count / structure:", len(coords))
    else:
        print("Error:", resp.text[:300])
except Exception as e:
    print("Fallo:", e)
