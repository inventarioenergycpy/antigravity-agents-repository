import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")

# 1. Probar cql_filter en vm_manzanas_calles_new
params_mza = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typeName": "EPEC:vm_manzanas_calles_new",
    "outputFormat": "application/json",
    "cql_filter": "nomenclatura = '11-01-01-03-04-003'"
}

resp_mza = requests.get(url, auth=auth, params=params_mza, verify=False, timeout=10)
print(f"Manzanas Status: {resp_mza.status_code}")
data_mza = resp_mza.json()
print(f"Features encontradas para '11-01-01-03-04-003': {len(data_mza.get('features', []))}")
for f in data_mza.get("features", []):
    p = f.get("properties", {})
    print(f"  Calle: {p.get('nombrecall')} (ID: {p.get('idcalle')}) - Tipo: {p.get('tipo')}")

# 2. Probar cql_filter en vt_parcelas_union
params_par = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetFeature",
    "typeName": "EPEC:vt_parcelas_union",
    "outputFormat": "application/json",
    "maxFeatures": 3
}

resp_par = requests.get(url, auth=auth, params=params_par, verify=False, timeout=10)
print(f"\nParcelas Status: {resp_par.status_code}")
data_par = resp_par.json()
print(f"Features de muestra en parcelas: {len(data_par.get('features', []))}")
for f in data_par.get("features", []):
    p = f.get("properties", {})
    print(f"  ID: {p.get('id')} | Nomenclatura: '{p.get('nomenclatura')}' | Parcela: '{p.get('parcela')}' | Lat: {p.get('latitud')} | Lon: {p.get('longitud')}")
