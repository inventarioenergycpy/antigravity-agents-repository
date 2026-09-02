---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 65
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMEORDENATIVOS_2025.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `TRT_NUMERO` | integer | 45501797 · 45499188 · 45519299 · 45522113 · 45495493 |
| `TOR_CODIGO` | text | IN · RP · RO |
| `ORD_NUMERO` | integer | 75848810 · 75846188 · 75866386 · 75873187 · 75841988 |
| `SRV_CODIGO` | integer | 749316 · 2762059 · 3012135 · 341633 · 3139205 |
| `CNT_NUMERO` | integer | 8 · 1 · 2 |
| `PRS_NUMERO` | integer | 5916818 · 3964124 · 5658784 · 1086713 · 5119393 |
| `FECHA_GENERACION` | date | 20/01/2025 · 19/01/2025 |
| `PERIODO_GENERACION` | integer | 202501 |
| `ANIO_GENERACION` | integer | 2025 |
| `MES_GENERACION` | integer | 1 |
| `SCF_CODIGO_ORIGEN` | integer | 1 · 47 |
| `SEC_CODIGO_ORIGEN` | text | COB · WEB |
| `SCF_CODIGO_DESTINO` | integer | 1 · 47 · 24 · 49 |
| `SEC_CODIGO_DESTINO` | text | COB · MED · OCSE |
| `ORD_FECHA_INICIO` | date | 2025-01-20 00:00:00.000000 · 2025-01-21 00:00:00.000000 · 2025-01-19 17:18:37.000000 |
| `ANIO_INICIO` | integer | 2025 |
| `MES_INICIO` | integer | 1 |
| `PERIODO_INICIO` | integer | 202501 |
| `ORD_FECHA_VENCIMIENTO` | integer | 45687 ·  |
| `ANIO_VENCIMIENTO` | integer | 2025 ·  |
| `MES_VENCIMIENTO` | integer | 1 ·  |
| `ORD_DATOS_ADICIONALES` | text | Aut - Proceso:3444982* Adeuda -F-687726… · Aut - Proceso:3444976* Adeuda -F-687890… · Aut - Proceso:3445019* Adeuda -F-686711… · Baja a Pedido Solcitada, Te Contato 351… · Verificar la conexion/reconexion del co… |
| `ORD_PRIORIDAD` | integer | 1 · 4 |
| `ORD_RESULTADO` | text | E |
| `ORD_FECHA_FIN` | integer | 45690 · 45678 · 45677 |
| `ANIO_FIN` | integer | 2025 |
| `MES_FIN` | integer | 2 · 1 |
| `PERIODO_FIN` | integer | 202502 · 202501 |
| `ORD_DATOS_RESULTADOS` | text | -Actualiza Resul. p/Cierre Diario · Gabinete (Tipos de Linea/Sitio)-Proc.x … · Estimado cliente analizado su reclamo l… |
| `ORD_FECHA_CARGA_RESULTADO` | integer | 45690 · 45678 · 45677 |
| `ANIO_CARGA_RESULTADO` | integer | 2025 |
| `MES_CARGA_RESULTADO` | integer | 2 · 1 |
| `DOC_TIPO` | text | RC ·  |
| `DOC_NUMERO` | integer | 79336090 · 79334593 · 79352131 ·  |
| `ODT_NUMERO` | unknown |  |
| `USR_NUMERO_ORIGEN` | integer | 92605 · 6727 · 2 |
| `USR_NUMERO_DESTINO` | integer |  · 8702 · 6704 |
| `ORD_SITUACION` | text | I |
| `ORD_ESTADO` | text | A · D |
| `SRV_CODIGO_ORIGEN` | unknown |  |
| `CNT_NUMERO_ORIGEN` | unknown |  |
| `TRT_NUMERO_ORIGEN` | unknown |  |
| `ZOP_CODIGO` | unknown |  |
| `CPR_NUMERO` | integer | 3444982 · 3444976 · 3445019 ·  |
| `CNR_NUMERO` | unknown |  |
| `USR_NUMERO_ANULA` | integer | 2 ·  |
| `ORD_DATOS_ANULA` | text | Anulacion Suspendidos Proc:ON LINE Por … · Anulacion Suspendidos Proc:ON LINE Por … · Anulacion Suspendidos Proc:ON LINE Por … ·  |
| `USR_NUMERO_IMPRIME` | integer | 92605 · 8702 ·  |
| `ORD_FECHA_ANULA` | decimal | 45679.398298611 · 45690.9396875 · 45688.497465278 ·  |
| `RCL_NUMERO` | unknown |  |
| `AGE_CODIGO_ORIGEN` | integer | 0 |
| `AGE_CODIGO_DESTINO` | integer | 0 |
| `USR_NUMERO_EJEC_ORD` | integer |  · 8702 · 6704 |
| `HABILES_INICIO` | integer | 0 · 1 |
| `HABILES_FIN` | integer | 10 · 1 · 0 |
| `HABILES_VENCIMIENTO` | integer | 8 · 0 |
| `HABILES_CARGA_RESULTADO` | integer | 10 · 1 · 0 |
| `EJECUTADO` | flag | SI |
| `TARIFA` | integer | 140 |
| `ID_CLASE` | integer | 1 |
| `ID_TENSION` | integer | 1 |
| `ESTADO_ACTUAL_CONTRATO` | text | C · V |
| `GRUPO_CONTRATO` | text | CC |
| `ID_ENTE` | integer | 5000 |
| `ID_TARIFA_FECHA_GENERACION` | integer | 140 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/ORDENATIVOS\|ORDENATIVOS]] — match parcial de nombre + 38 columnas en comun
- [[Projects/sigec-explorer/tablas/ORDENATIVOS_HIST\|ORDENATIVOS_HIST]] — 38 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
