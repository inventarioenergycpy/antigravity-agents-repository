import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")
params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typeName": "EPEC:vt_parcelas_union",
    "outputFormat": "application/json",
    "srsName": "EPSG:22174",
    "bbox": "4387000,6528000,4388000,6529000,EPSG:22174",
    "maxFeatures": 3
}

try:
    resp = requests.get(url, auth=auth, params=params, verify=False, timeout=10)
    print("BBOX query status:", resp.status_code)
    if resp.status_code == 200:
        data = resp.json()
        print("Features:", len(data.get("features", [])))
        for f in data.get("features", []):
            print(f.get("properties"))
    else:
        print("Error:", resp.text[:300])
except Exception as e:
    print("Fallo:", e)
