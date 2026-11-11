import requests, time

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")

t0 = time.time()
params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typeName": "EPEC:vt_parcelas_union",
    "outputFormat": "application/json",
    "cql_filter": "nomenclatura = '11-01-01-04-03-049-001'"
}

try:
    resp = requests.get(url, auth=auth, params=params, verify=False, timeout=25)
    t1 = time.time()
    print(f"Status: {resp.status_code} in {t1-t0:.2f} s")
    if resp.status_code == 200:
        data = resp.json()
        print("Features:", len(data.get("features", [])))
        for f in data.get("features", []):
            print(f.get("properties"))
    else:
        print("Error resp:", resp.text[:400])
except Exception as e:
    print(f"Error: {e}")
