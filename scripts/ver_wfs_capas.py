import requests
import xml.etree.ElementTree as ET

url = "https://maaysp-ws.cba.gov.ar/EPEC/wfs"
auth = ("EPEC_comercial", "Bratis-c0m3rc14l")
params = {
    "service": "WFS",
    "version": "1.1.0",
    "request": "GetCapabilities"
}

resp = requests.get(url, auth=auth, params=params, verify=False, timeout=15)
root = ET.fromstring(resp.content)
print("=== CAPAS DISPONIBLES EN EPEC WFS ===")
for elem in root.iter():
    if elem.tag.endswith('FeatureType'):
        name = elem.find('{http://www.opengis.net/wfs}Name')
        title = elem.find('{http://www.opengis.net/wfs}Title')
        srs = elem.find('{http://www.opengis.net/wfs}DefaultSRS')
        if name is not None:
            print(f"- {name.text} | Title: {title.text if title is not None else ''} | SRS: {srs.text if srs is not None else ''}")
