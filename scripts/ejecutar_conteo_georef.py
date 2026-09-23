import os
import sys
import time
import oracledb
import pandas as pd
from dotenv import load_dotenv

# Configurar salida UTF-8 para consola Windows
sys.stdout.reconfigure(encoding='utf-8')

# Cargar variables de entorno desde .env
load_dotenv(r'D:\Proyectos\antigravity-agents-repository\.env')

OR_USER = os.getenv("OR_USER", "jidiaz")
OR_PASS = os.getenv("OR_PASS")
OR_HOST = os.getenv("OR_HOST", "epec2-scan2.epec.net")
OR_PORT = int(os.getenv("OR_PORT", "1521"))
OR_SERVICE_NAME = os.getenv("OR_SERVICE_NAME", "PRODEBS_SEE")
OR_INSTANT_CLIENT = os.getenv("OR_INSTANT_CLIENT", r"C:\app\client\product\19.0.0\client_2\bin")

def ejecutar_consulta():
    if not OR_PASS:
        print("ERROR: La variable de entorno OR_PASS no está definida.")
        print("Por favor, proporciona o configura la contraseña en el archivo .env.")
        return

    print(f"[*] Inicializando Oracle Client (Modo Thick 64-bit)...")
    print(f"    Ruta: {OR_INSTANT_CLIENT}")
    oracledb.init_oracle_client(lib_dir=OR_INSTANT_CLIENT)

    print(f"[*] Conectando a {OR_USER}@{OR_HOST}:{OR_PORT}/{OR_SERVICE_NAME}...")
    dsn = oracledb.makedsn(host=OR_HOST, port=OR_PORT, service_name=OR_SERVICE_NAME)
    
    intentos = 3
    conn = None
    for intento in range(1, intentos + 1):
        try:
            conn = oracledb.connect(user=OR_USER, password=OR_PASS, dsn=dsn)
            print(f"[+] Conexión establecida exitosamente (Intento {intento}).")
            break
        except Exception as e:
            print(f"[-] Intento {intento} falló: {e}")
            if intento < intentos:
                time.sleep(2)
            else:
                print("[-] No se pudo conectar a la base de datos Oracle.")
                return

    try:
        with conn.cursor() as cur:
            print("[*] Aplicando protección: SET TRANSACTION READ ONLY...")
            cur.execute("SET TRANSACTION READ ONLY")

        sql_query = """
        SELECT
            FLOOR((TO_NUMBER(suministro) - 1) / 500000) AS tramo_id,
            TO_CHAR(FLOOR((TO_NUMBER(suministro) - 1) / 500000) * 500000 + 1, 'FM999G999G999') || ' - ' ||
            TO_CHAR((FLOOR((TO_NUMBER(suministro) - 1) / 500000) + 1) * 500000, 'FM999G999G999') AS rango_teorico,
            COUNT(*) AS total_filas,
            COUNT(DISTINCT suministro) AS suministros_unicos,
            MIN(TO_NUMBER(suministro)) AS suministro_min_real,
            MAX(TO_NUMBER(suministro)) AS suministro_max_real,
            (MAX(TO_NUMBER(suministro)) - MIN(TO_NUMBER(suministro)) + 1) - COUNT(DISTINCT suministro) AS huecos_en_secuencia,
            ROUND((COUNT(DISTINCT suministro) / 500000.0) * 100, 2) AS pct_densidad_tramo
        FROM
            georef.vw_suministros
        WHERE
            suministro IS NOT NULL
            AND REGEXP_LIKE(TRIM(suministro), '^[0-9]+$')
            AND TO_NUMBER(suministro) > 0
        GROUP BY
            FLOOR((TO_NUMBER(suministro) - 1) / 500000)
        ORDER BY
            tramo_id ASC
        """

        print("[*] Ejecutando consulta analítica sobre georef.vw_suministros...")
        t_inicio = time.time()
        
        df = pd.read_sql(sql_query, conn)
        t_total = time.time() - t_inicio
        
        print(f"[+] Consulta finalizada en {t_total:.2f} segundos.")
        print(f"[+] Total de tramos encontrados: {len(df)}")
        print("\n" + "="*80)
        print("RESULTADO DEL CONTEO ESCALONADO DE A 500.000:")
        print("="*80)
        print(df.to_string(index=False))
        print("="*80)

        # Exportar resultado localmente en Descargas
        descargas = os.path.expanduser(r"~\Downloads")
        out_csv = os.path.join(descargas, "conteo_suministros_georef_500k.csv")
        df.to_csv(out_csv, index=False, encoding="utf-8-sig")
        print(f"\n[+] Resultado exportado a: {out_csv}")

    except Exception as e:
        print(f"[-] Error durante la ejecución de la consulta: {e}")
    finally:
        if conn:
            conn.close()
            print("[*] Conexión cerrada de forma segura.")

if __name__ == "__main__":
    ejecutar_consulta()
