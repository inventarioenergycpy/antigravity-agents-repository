---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 64
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMEORDENATIVOS_2016.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `TRT_NUMERO` | integer | 28243081 · 28250623 · 28250624 · 28250625 · 28250626 |
| `TOR_CODIGO` | text | IC · IN |
| `ORD_NUMERO` | integer | 53048645 · 53056219 · 53056220 · 53056221 · 53056222 |
| `SRV_CODIGO` | integer | 391989 · 2672619 · 2729404 · 2773102 · 2781433 |
| `CNT_NUMERO` | integer | 3 · 1 · 2 |
| `PRS_NUMERO` | integer | 369619 · 1478072 · 5075079 · 4147166 · 1362203 |
| `FECHA_GENERACION` | date | 06/01/2016 |
| `PERIODO_GENERACION` | integer | 201601 |
| `ANIO_GENERACION` | integer | 2016 |
| `MES_GENERACION` | integer | 1 |
| `SCF_CODIGO_ORIGEN` | integer | 1 |
| `SEC_CODIGO_ORIGEN` | text | SUCNOR · COB |
| `SCF_CODIGO_DESTINO` | integer | 49 · 1 |
| `SEC_CODIGO_DESTINO` | text | MED · COB |
| `ORD_FECHA_INICIO` | text | 1/6/2016 12:00:00 AM |
| `ANIO_INICIO` | integer | 2016 |
| `MES_INICIO` | integer | 1 |
| `PERIODO_INICIO` | integer | 201601 |
| `ORD_FECHA_VENCIMIENTO` | text |  · 1/18/2016 12:00:00 AM |
| `ANIO_VENCIMIENTO` | integer |  · 2016 |
| `MES_VENCIMIENTO` | integer |  · 1 |
| `ORD_DATOS_ADICIONALES` | text |  · Aut - Proceso:2137253* Adeuda -F:2015/10 |
| `ORD_PRIORIDAD` | integer | 1 |
| `ORD_RESULTADO` | text | ER · E |
| `ORD_FECHA_FIN` | text | 1/20/2016 12:00:00 AM · 1/21/2016 12:00:00 AM |
| `ANIO_FIN` | integer | 2016 |
| `MES_FIN` | integer | 1 |
| `PERIODO_FIN` | integer | 201601 |
| `ORD_DATOS_RESULTADOS` | text | lectura activa 49285 · -Actualiza Resul. p/Cierre Diario.C.020… · -Actualiza Resul. p/Cierre Diario.C.290… · -Actualiza Resul. p/Cierre Diario · .C.08012016.F.578393734.Ea.S.-Actualiza… |
| `ORD_FECHA_CARGA_RESULTADO` | text | 1/21/2016 12:00:00 AM |
| `ANIO_CARGA_RESULTADO` | integer | 2016 |
| `MES_CARGA_RESULTADO` | integer | 1 |
| `DOC_TIPO` | text |  · RC |
| `DOC_NUMERO` | integer |  · 32736231 · 32736295 · 32736296 · 32736232 |
| `ODT_NUMERO` | unknown |  |
| `USR_NUMERO_ORIGEN` | integer | 10194 · 8710 |
| `USR_NUMERO_DESTINO` | integer | 6626 ·  |
| `ORD_SITUACION` | text | I · V |
| `ORD_ESTADO` | text | D · A |
| `SRV_CODIGO_ORIGEN` | unknown |  |
| `CNT_NUMERO_ORIGEN` | unknown |  |
| `TRT_NUMERO_ORIGEN` | unknown |  |
| `ZOP_CODIGO` | unknown |  |
| `CPR_NUMERO` | integer |  · 2137253 |
| `CNR_NUMERO` | integer | 40687080 ·  |
| `USR_NUMERO_ANULA` | integer |  · 9653 · 10471 |
| `ORD_DATOS_ANULA` | text |  · . Anulado p/Cobranza..C.02022016.F.5783… · . Anulado p/Cobranza..C.29012016.F.5783… · . Anulado p/Cobranza..C.08012016.F.5783… |
| `USR_NUMERO_IMPRIME` | integer | 5785 · 8710 |
| `ORD_FECHA_ANULA` | text |  · 2/2/2016 2:21:31 PM · 1/29/2016 7:59:58 AM · 1/8/2016 2:20:36 PM |
| `RCL_NUMERO` | unknown |  |
| `AGE_CODIGO_ORIGEN` | integer | 2 · 0 |
| `AGE_CODIGO_DESTINO` | integer | 0 |
| `USR_NUMERO_EJEC_ORD` | unknown |  |
| `HABILES_INICIO` | integer | 0 |
| `HABILES_FIN` | integer | 10 · 11 |
| `HABILES_VENCIMIENTO` | integer | 0 · 8 |
| `HABILES_CARGA_RESULTADO` | integer | 11 |
| `EJECUTADO` | flag | SI |
| `TARIFA` | integer | 140 · 240 |
| `ID_CLASE` | integer | 1 · 2 |
| `ID_TENSION` | integer | 1 |
| `ESTADO_ACTUAL_CONTRATO` | text | C · V |
| `GRUPO_CONTRATO` | text | CC |
| `ID_ENTE` | integer | 5000 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/ORDENATIVOS\|ORDENATIVOS]] — match parcial de nombre + 38 columnas en comun
- [[Projects/sigec-explorer/tablas/ORDENATIVOS_HIST\|ORDENATIVOS_HIST]] — 38 columnas en comun
- [[Projects/sigec-explorer/tablas/XXCO_ORD_TMP\|XXCO_ORD_TMP]] — 19 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
