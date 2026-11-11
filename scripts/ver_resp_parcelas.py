import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")

params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typeName": "EPEC:vt_parcelas_union",
    "outputFormat": "application/json",
    "cql_filter": "nomenclatura = '11-01-01-04-03-049-001'"
}

resp = requests.get(url, auth=auth, params=params, verify=False, timeout=30)
print("Content-Type:", resp.headers.get("Content-Type"))
print("Body:")
print(resp.text[:1000])
