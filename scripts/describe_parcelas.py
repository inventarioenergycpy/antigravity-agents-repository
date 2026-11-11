import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")
params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "DescribeFeatureType",
    "typeName": "EPEC:vt_parcelas_union"
}

resp = requests.get(url, auth=auth, params=params, verify=False, timeout=10)
print(resp.text[:2000])
