import requests

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")

test_manzanas = [
    "11-01-01-17-11-002",
    "11-01-01-01-29-043",
    "11-01-01-34-07-007",
    "11-01-01-21-32-024",
    "11-01-01-28-26-014",
    "11-01-01-02-12-033", # San Vicente
    "11-01-01-04-03-049"  # Centro
]

print("=== CONSULTANDO CALLES PERIMETRALES EN EPEC:vm_manzanas_calles_new ===")
for mza in test_manzanas:
    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typeName": "EPEC:vm_manzanas_calles_new",
        "outputFormat": "application/json",
        "cql_filter": f"nomenclatura = '{mza}'"
    }
    resp = requests.get(url, auth=auth, params=params, verify=False, timeout=10)
    if resp.status_code == 200:
        data = resp.json()
        calles = list(set([f.get("properties", {}).get("nombrecall") for f in data.get("features", []) if f.get("properties", {}).get("nombrecall")]))
        print(f"Manzana {mza} -> Calles perimetrales ({len(calles)}): {', '.join(sorted(calles))}")
    else:
        print(f"Manzana {mza} -> Error {resp.status_code}")
