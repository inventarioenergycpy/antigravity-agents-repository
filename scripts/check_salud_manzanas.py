import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")
params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typeName": "EPEC:vm_manzanas_calles_new",
    "outputFormat": "application/json",
    "cql_filter": "nomenclatura = '11-01-01-04-03-049'"
}

resp = requests.get(url, auth=auth, params=params, verify=False, timeout=10)
print("Status:", resp.status_code)
if resp.status_code == 200:
    data = resp.json()
    calles = set([f['properties']['nombrecall'] for f in data.get('features', [])])
    print("Calles encontradas:", calles)
