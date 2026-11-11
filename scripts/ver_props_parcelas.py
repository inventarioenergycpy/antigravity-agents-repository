import requests, json

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")
params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typeName": "EPEC:vt_parcelas_union",
    "maxFeatures": 2,
    "outputFormat": "application/json"
}

resp = requests.get(url, auth=auth, params=params, verify=False)
data = resp.json()
print("TOTAL FEATURES IN vt_parcelas_union:", data.get("totalFeatures"))
for f in data.get("features", []):
    print("PROPERTIES OF EPEC:vt_parcelas_union:")
    print(json.dumps(f.get("properties", {}), indent=2))
