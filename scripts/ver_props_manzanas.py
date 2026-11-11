import requests, json

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")
params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typeName": "EPEC:vm_manzanas_calles_new",
    "maxFeatures": 2,
    "outputFormat": "application/json"
}

resp = requests.get(url, auth=auth, params=params, verify=False)
data = resp.json()
for f in data.get("features", []):
    print("PROPERTIES OF EPEC:vm_manzanas_calles_new:")
    print(json.dumps(f.get("properties", {}), indent=2))
