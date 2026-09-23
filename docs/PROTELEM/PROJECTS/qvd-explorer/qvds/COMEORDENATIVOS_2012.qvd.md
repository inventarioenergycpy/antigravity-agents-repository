---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 57
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMEORDENATIVOS_2012.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `TRT_NUMERO` | integer | 22443845 · 21295839 · 21295853 · 21295873 · 21295880 |
| `TOR_CODIGO` | text | NT · CX |
| `ORD_NUMERO` | integer | 46398809 · 44926902 · 44926927 · 44926954 · 44926963 |
| `SRV_CODIGO` | integer | 226832 · 1034054 · 338536 · 478014 · 1268884 |
| `CNT_NUMERO` | integer | 1 · 3 · 12 · 6 · 2 |
| `PRS_NUMERO` | integer | 130594 · 4619383 · 3571965 · 3509490 · 1203426 |
| `ORD_FECHA_GENERACION` | text | 10/5/2012 12:00:00 AM · 1/6/2012 12:00:00 AM |
| `ANIO_GENERACION` | integer | 2012 |
| `PERIODO_GENERACION` | text | 10/2012 · 01/2012 |
| `MES_GENERACION` | integer | 10 · 1 |
| `SCF_CODIGO_ORIGEN` | integer | 31 · 1 · 22 |
| `SEC_CODIGO_ORIGEN` | text | COB · FINANCIA · OCSE |
| `SCF_CODIGO_DESTINO` | integer | 31 · 1 · 22 |
| `SEC_CODIGO_DESTINO` | text | COB · MED_SUR · MED |
| `ORD_FECHA_INICIO` | text | 10/5/2012 12:00:00 AM · 1/6/2012 12:00:00 AM |
| `ANIO_INICIO` | integer | 2012 |
| `MES_INICIO` | integer | 10 · 1 |
| `ORD_FECHA_VENCIMIENTO` | unknown |  |
| `ANIO_VENCIMIENTO` | unknown |  |
| `MES_VENCIMIENTO` | unknown |  |
| `ORD_DATOS_ADICIONALES` | text | Garante del Suministro 226832 sin Contr… · Manual -Documenta deuda con rc. 2408079… · SE ADJUNTA CROQUIS.- ·  · Manual -con rc. 24081089. |
| `ORD_PRIORIDAD` | integer | 1 · 4 |
| `ORD_RESULTADO` | text | E · IN |
| `ORD_FECHA_FIN` | text |  · 1/7/2012 12:00:00 AM · 1/6/2012 12:00:00 AM · 1/9/2012 12:00:00 AM |
| `ANIO_FIN` | integer |  · 2012 |
| `MES_FIN` | integer |  · 1 |
| `ORD_DATOS_RESULTADOS` | text | .C.10102012.F.558993289.Ea.D. · DEBE REEMPLAZAR LA PUESTA A TIERRA COMP… · -Proc.x carga Rapida 09/01/2012 ·  · -Proc.x carga Rapida 11/01/2012 |
| `ORD_FECHA_CARGA_RESULTADO` | text | 10/5/2012 7:11:30 PM · 1/9/2012 12:00:00 AM · 1/11/2012 12:00:00 AM |
| `ANIO_CARGA_RESULTADO` | integer | 2012 |
| `MES_CARGA_RESULTADO` | integer | 10 · 1 |
| `DOC_TIPO` | unknown |  |
| `DOC_NUMERO` | unknown |  |
| `ODT_NUMERO` | unknown |  |
| `USR_NUMERO_ORIGEN` | integer | 6365 · 5651 · 8830 · 7468 |
| `USR_NUMERO_DESTINO` | integer |  · 10176 · 2010 · 8854 |
| `ORD_SITUACION` | text | P · I |
| `ORD_ESTADO` | text | A · D |
| `SRV_CODIGO_ORIGEN` | unknown |  |
| `CNT_NUMERO_ORIGEN` | unknown |  |
| `TRT_NUMERO_ORIGEN` | unknown |  |
| `ZOP_CODIGO` | integer |  · 04 · 05 |
| `CPR_NUMERO` | unknown |  |
| `CNR_NUMERO` | integer |  · 22281500 · 22281792 · 22284726 · 22283406 |
| `USR_NUMERO_ANULA` | integer | 5727 ·  |
| `ORD_DATOS_ANULA` | text | . Anulado p/Cobranza..C.10102012.F.5589… ·  |
| `USR_NUMERO_IMPRIME` | integer |  · 788 · 2010 · 3681 |
| `ORD_FECHA_ANULA` | text | 10/10/2012 7:52:22 AM ·  |
| `RCL_NUMERO` | unknown |  |
| `AGE_CODIGO_ORIGEN` | integer | 0 · 1 |
| `AGE_CODIGO_DESTINO` | integer | 0 |
| `USR_NUMERO_EJEC_ORD` | integer |  · 8544 · 8141 |
| `HABILES_INICIO` | integer | 0 |
| `HABILES_FIN` | integer | 0 · 1 |
| `HABILES_VENCIMIENTO` | integer | 0 |
| `HABILES_CARGA_RESULTADO` | integer | 0 · 1 · 3 |
| `EJECUTADO` | flag | SI |
| `TCL_CODIGO` | integer | 240 · 140 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/ORDENATIVOS\|ORDENATIVOS]] — match parcial de nombre + 39 columnas en comun
- [[Projects/sigec-explorer/tablas/ORDENATIVOS_HIST\|ORDENATIVOS_HIST]] — 39 columnas en comun
- [[Projects/sigec-explorer/tablas/XXCO_ORD_TMP\|XXCO_ORD_TMP]] — 20 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
