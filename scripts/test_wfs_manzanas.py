import requests

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

try:
    resp = requests.get(url, auth=auth, params=params, timeout=15, verify=False)
    print(f"Status: {resp.status_code}")
    print("Content preview (first 500 chars):")
    print(resp.text[:500])
except Exception as e:
    print(f"Error: {e}")
