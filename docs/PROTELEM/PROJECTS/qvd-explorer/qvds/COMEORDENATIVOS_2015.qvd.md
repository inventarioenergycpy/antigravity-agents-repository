---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 60
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMEORDENATIVOS_2015.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `TRT_NUMERO` | integer | 27148876 · 27149071 · 27149162 · 27149304 · 27149526 |
| `TOR_CODIGO` | text | CX |
| `ORD_NUMERO` | integer | 51742705 · 51742883 · 51743000 · 51743201 · 51743532 |
| `SRV_CODIGO` | integer | 433406 · 2739946 · 226211 · 428861 · 538217 |
| `CNT_NUMERO` | integer | 4 · 3 · 2 · 7 |
| `PRS_NUMERO` | integer | 695798 · 4809949 · 129973 · 4492938 · 455803 |
| `FECHA_GENERACION` | date | 28/05/2015 |
| `PERIODO_GENERACION` | integer | 201505 |
| `ANIO_GENERACION` | integer | 2015 |
| `MES_GENERACION` | integer | 5 |
| `SCF_CODIGO_ORIGEN` | integer | 1 · 30 |
| `SEC_CODIGO_ORIGEN` | text | SUCNOR · CLIESP |
| `SCF_CODIGO_DESTINO` | integer | 1 · 30 |
| `SEC_CODIGO_DESTINO` | text | MED_NORT · MED |
| `ORD_FECHA_INICIO` | text | 5/28/2015 12:00:00 AM |
| `ANIO_INICIO` | integer | 2015 |
| `MES_INICIO` | integer | 5 |
| `PERIODO_INICIO` | integer | 201505 |
| `ORD_FECHA_VENCIMIENTO` | unknown |  |
| `ANIO_VENCIMIENTO` | unknown |  |
| `MES_VENCIMIENTO` | unknown |  |
| `ORD_DATOS_ADICIONALES` | text |  · POR FAVOR CONEXTAR DESPUES DE LAS 14 HO… |
| `ORD_PRIORIDAD` | integer | 1 |
| `ORD_RESULTADO` | text | E · IN |
| `ORD_FECHA_FIN` | text | 5/29/2015 12:00:00 AM · 5/28/2015 12:00:00 AM · 6/2/2015 12:00:00 AM |
| `ANIO_FIN` | integer | 2015 |
| `MES_FIN` | integer | 5 · 6 |
| `PERIODO_FIN` | integer | 201505 · 201506 |
| `ORD_DATOS_RESULTADOS` | text |  · NO SE PUDO VERIFICAR TABLERO DE PROTECC… · IDENTIFICAR DONDE VA COLOCADO EL MEDIDO… |
| `ORD_FECHA_CARGA_RESULTADO` | text | 6/1/2015 12:00:00 AM · 5/29/2015 12:00:00 AM · 6/3/2015 12:00:00 AM |
| `ANIO_CARGA_RESULTADO` | integer | 2015 |
| `MES_CARGA_RESULTADO` | integer | 6 · 5 |
| `DOC_TIPO` | unknown |  |
| `DOC_NUMERO` | unknown |  |
| `ODT_NUMERO` | unknown |  |
| `USR_NUMERO_ORIGEN` | integer | 6698 · 1474 |
| `USR_NUMERO_DESTINO` | integer | 705 · 1474 · 8036 |
| `ORD_SITUACION` | text | I · P |
| `ORD_ESTADO` | text | D |
| `SRV_CODIGO_ORIGEN` | unknown |  |
| `CNT_NUMERO_ORIGEN` | unknown |  |
| `TRT_NUMERO_ORIGEN` | unknown |  |
| `ZOP_CODIGO` | integer | 09 ·  · 02 · 03 |
| `CPR_NUMERO` | unknown |  |
| `CNR_NUMERO` | integer | 38222051 ·  · 38227337 |
| `USR_NUMERO_ANULA` | unknown |  |
| `ORD_DATOS_ANULA` | unknown |  |
| `USR_NUMERO_IMPRIME` | integer | 6567 · 1474 |
| `ORD_FECHA_ANULA` | unknown |  |
| `RCL_NUMERO` | unknown |  |
| `AGE_CODIGO_ORIGEN` | integer | 2 · 0 |
| `AGE_CODIGO_DESTINO` | integer | 0 |
| `USR_NUMERO_EJEC_ORD` | integer | 8351 · 7918 · 7405 |
| `HABILES_INICIO` | integer | 0 |
| `HABILES_FIN` | integer | 1 · 0 · 3 |
| `HABILES_VENCIMIENTO` | integer | 0 |
| `HABILES_CARGA_RESULTADO` | integer | 2 · 1 · 4 |
| `EJECUTADO` | flag | SI |
| `TARIFA` | integer | 140 · 240 |
| `ESTADO_ACTUAL_CONTRATO` | text | C · V |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/ORDENATIVOS\|ORDENATIVOS]] — match parcial de nombre + 38 columnas en comun
- [[Projects/sigec-explorer/tablas/ORDENATIVOS_HIST\|ORDENATIVOS_HIST]] — 38 columnas en comun
- [[Projects/sigec-explorer/tablas/XXCO_ORD_TMP\|XXCO_ORD_TMP]] — 19 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
