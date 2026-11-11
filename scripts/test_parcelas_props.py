import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")

params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typeName": "EPEC:vt_parcelas_union",
    "outputFormat": "application/json",
    "propertyName": "id,nomenclatura,parcela,latitud,longitud",
    "maxFeatures": 5
}

try:
    resp = requests.get(url, auth=auth, params=params, verify=False, timeout=12)
    print(f"Status: {resp.status_code}")
    if resp.status_code == 200:
        data = resp.json()
        print("Features encontradas:", len(data.get("features", [])))
        for f in data.get("features", []):
            print(f.get("properties"))
    else:
        print("Respuesta no 200:", resp.text[:500])
except Exception as e:
    print(f"Error: {e}")
