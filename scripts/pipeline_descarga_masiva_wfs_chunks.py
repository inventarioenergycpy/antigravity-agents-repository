# -*- coding: utf-8 -*-
import urllib.request, ssl, json, time, os, urllib.parse, sys
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data_dir = r"D:\Proyectos\antigravity-agents-repository\data"
cache_dir = os.path.join(data_dir, "cache_parcelas_wfs")
os.makedirs(cache_dir, exist_ok=True)

base_wfs_url = 'https://maaysp-ws.cba.gov.ar/EPEC/wfs?service=WFS&version=1.1.0&request=GetFeature&typeName=EPEC:vm_vt_parcelas_calles&outputFormat=application/json&srsName=EPSG:22174'

def descargar_chunk(chunk_item):
    depto = chunk_item.get('depto', '11')
    circ = chunk_item.get('circ', '')
    sec = chunk_item.get('seccion', '')
    ped = chunk_item.get('pedania', '')
    cql = chunk_item['cql']
    
    if depto == '11':
        filename = f"cap_c{circ}_s{sec}.json"
    else:
        filename = f"int_d{depto}_p{ped}.json"
        
    out_file = os.path.join(cache_dir, filename)
    
    # Check if exists and valid
    if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
        return {"status": "CACHED", "file": filename, "total": chunk_item.get('total', 0)}
        
    url = base_wfs_url + '&cql_filter=' + urllib.parse.quote(cql)
    
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            resp = urllib.request.urlopen(req, context=ctx, timeout=40).read().decode('utf-8')
            # Verify JSON
            data = json.loads(resp)
            cnt = len(data.get('features', []))
            
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(resp)
                
            return {"status": "DOWNLOADED", "file": filename, "total": cnt}
        except Exception as e:
            if attempt == 3:
                return {"status": "ERROR", "file": filename, "error": str(e)}
            time.sleep(1.0 * attempt)

def ejecutar_descarga_masiva():
    print("=" * 80)
    print("🚀 INICIANDO DESCARGA INCREMENTAL WFS DE PARCELAS PROVINCIALES")
    print("=" * 80)
    
    cap_path = os.path.join(data_dir, "catalogo_chunks_capital.json")
    int_path = os.path.join(data_dir, "catalogo_chunks_interior.json")
    
    all_chunks = []
    if os.path.exists(cap_path):
        with open(cap_path, 'r', encoding='utf-8') as f:
            all_chunks.extend(json.load(f))
    if os.path.exists(int_path):
        with open(int_path, 'r', encoding='utf-8') as f:
            all_chunks.extend(json.load(f))
            
    print(f"Total de chunks en catálogo provincial: {len(all_chunks):,}")
    
    t0 = time.time()
    completados = 0
    descargados = 0
    cacheados = 0
    errores = 0
    total_parcelas = 0
    
    # Download with 6 workers (polite to GeoServer, optimal throughput)
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(descargar_chunk, c): c for c in all_chunks}
        for fut in as_completed(futures):
            completados += 1
            res = fut.result()
            st = res.get('status')
            tot = res.get('total', 0)
            total_parcelas += tot
            
            if st == 'CACHED':
                cacheados += 1
            elif st == 'DOWNLOADED':
                descargados += 1
            else:
                errores += 1
                print(f"  [ERROR] {res.get('file')}: {res.get('error')}")
                
            if completados % 25 == 0 or completados == len(all_chunks):
                elapsed = time.time() - t0
                pct = (completados / len(all_chunks)) * 100
                print(f"Progreso: {completados}/{len(all_chunks)} ({pct:.1f}%) | "
                      f"Descargados: {descargados} | Cacheados: {cacheados} | "
                      f"Parcelas acumuladas: {total_parcelas:,} | Tiempo: {elapsed:.1f}s", flush=True)

    print("\n" + "=" * 80)
    print(f"✅ DESCARGA INCREMENTAL FINALIZADA EN {time.time()-t0:.2f}s:")
    print(f"  Chunks cacheados previamente: {cacheados}")
    print(f"  Chunks descargados ahora: {descargados}")
    print(f"  Errores: {errores}")
    print(f"  Total parcelas en cache local: {total_parcelas:,}")
    print("=" * 80)

if __name__ == "__main__":
    ejecutar_descarga_masiva()
