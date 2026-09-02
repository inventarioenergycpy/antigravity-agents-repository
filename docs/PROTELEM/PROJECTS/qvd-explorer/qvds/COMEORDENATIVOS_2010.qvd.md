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

# 📦 COMEORDENATIVOS_2010.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `TRT_NUMERO` | integer | 16912874 · 16912886 · 16912891 · 16875293 · 16877565 |
| `TOR_CODIGO` | text | II · VC · CX |
| `ORD_NUMERO` | integer | 40001298 · 40001314 · 40001321 · 39940794 · 39944801 |
| `SRV_CODIGO` | integer | 740928 · 740929 · 826087 · 518131 · 2349283 |
| `CNT_NUMERO` | integer | 1 · 5 |
| `PRS_NUMERO` | integer | 666724 · 666725 · 1534877 · 435718 · 1483045 |
| `ORD_FECHA_GENERACION` | text | 1/26/2010 12:00:00 AM · 1/12/2010 12:00:00 AM · 1/13/2010 12:00:00 AM |
| `ANIO_GENERACION` | integer | 2010 |
| `PERIODO_GENERACION` | text | 01/2010 |
| `MES_GENERACION` | integer | 1 |
| `SCF_CODIGO_ORIGEN` | integer | 1 |
| `SEC_CODIGO_ORIGEN` | text | ATSUM · SUCEST · OCSE |
| `SCF_CODIGO_DESTINO` | integer | 1 |
| `SEC_CODIGO_DESTINO` | text | FRAU · ATSUM · MED_SUR |
| `ORD_FECHA_INICIO` | text | 3/23/2010 12:00:00 AM · 1/26/2010 12:00:00 AM · 1/14/2010 12:00:00 AM |
| `ANIO_INICIO` | integer | 2010 |
| `MES_INICIO` | integer | 3 · 1 |
| `ORD_FECHA_VENCIMIENTO` | unknown |  |
| `ANIO_VENCIMIENTO` | unknown |  |
| `MES_VENCIMIENTO` | unknown |  |
| `ORD_DATOS_ADICIONALES` | text | Generado por Carga de Lecturas ON-LINE · SE ENTREGA ET 21 · Manual - |
| `ORD_PRIORIDAD` | integer | 1 · 4 |
| `ORD_RESULTADO` | text |  · R · E |
| `ORD_FECHA_FIN` | text |  · 4/16/2010 12:00:00 AM · 1/14/2010 12:00:00 AM · 1/15/2010 12:00:00 AM |
| `ANIO_FIN` | integer |  · 2010 |
| `MES_FIN` | integer |  · 4 · 1 |
| `ORD_DATOS_RESULTADOS` | text |  · A261926 · -Proc.x carga Rapida 22/01/2010 · -Proc.x carga Rapida 23/01/2010 |
| `ORD_FECHA_CARGA_RESULTADO` | text |  · 4/19/2010 12:00:00 AM · 1/22/2010 12:00:00 AM · 1/23/2010 12:00:00 AM |
| `ANIO_CARGA_RESULTADO` | integer |  · 2010 |
| `MES_CARGA_RESULTADO` | integer |  · 4 · 1 |
| `DOC_TIPO` | unknown |  |
| `DOC_NUMERO` | unknown |  |
| `ODT_NUMERO` | unknown |  |
| `USR_NUMERO_ORIGEN` | integer | 7950 · 8364 · 8838 |
| `USR_NUMERO_DESTINO` | integer |  · 5998 · 4573 · 8854 |
| `ORD_SITUACION` | text | I |
| `ORD_ESTADO` | text | A · D |
| `SRV_CODIGO_ORIGEN` | unknown |  |
| `CNT_NUMERO_ORIGEN` | unknown |  |
| `TRT_NUMERO_ORIGEN` | unknown |  |
| `ZOP_CODIGO` | integer | 08 ·  · 05 · 06 |
| `CPR_NUMERO` | unknown |  |
| `CNR_NUMERO` | integer |  · 14109244 · 13990528 · 13989513 |
| `USR_NUMERO_ANULA` | integer | 5998 ·  |
| `ORD_DATOS_ANULA` | text | SE ANULA Y SE ASOCIA CON A261927.- ·  |
| `USR_NUMERO_IMPRIME` | integer | 238 · 7950 · 6745 · 599 |
| `ORD_FECHA_ANULA` | text | 4/19/2010 12:00:00 AM ·  |
| `RCL_NUMERO` | integer | 644803 · 644805 ·  |
| `AGE_CODIGO_ORIGEN` | integer | 0 · 1 |
| `AGE_CODIGO_DESTINO` | integer | 0 · 2 |
| `USR_NUMERO_EJEC_ORD` | integer |  · 90005 |
| `HABILES_INICIO` | integer | 40 · 0 · 2 · 1 |
| `HABILES_FIN` | integer | 0 · 55 · 2 |
| `HABILES_VENCIMIENTO` | integer | 0 |
| `HABILES_CARGA_RESULTADO` | integer | 99 · 56 · 24 · 8 |
| `EJECUTADO` | flag | NO · SI |
| `TCL_CODIGO` | integer | 140 · 240 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/ORDENATIVOS\|ORDENATIVOS]] — match parcial de nombre + 39 columnas en comun
- [[Projects/sigec-explorer/tablas/ORDENATIVOS_HIST\|ORDENATIVOS_HIST]] — 39 columnas en comun
- [[Projects/sigec-explorer/tablas/XXCO_ORD_TMP\|XXCO_ORD_TMP]] — 20 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
