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

# 📦 COMEORDENATIVOS_2024.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `TRT_NUMERO` | integer | 42724334 · 42723169 · 42738178 · 42739077 · 42723551 |
| `TOR_CODIGO` | text | NT · IN · ET |
| `ORD_NUMERO` | integer | 72161180 · 72160035 · 72175556 · 72177422 · 72160244 |
| `SRV_CODIGO` | integer | 3025353 · 538563 · 2882531 · 3137972 · 463057 |
| `CNT_NUMERO` | integer | 1 · 4 |
| `PRS_NUMERO` | integer | 5687398 · 456159 · 5090765 · 5268584 · 378658 |
| `FECHA_GENERACION` | date | 08/01/2024 |
| `PERIODO_GENERACION` | integer | 202401 |
| `ANIO_GENERACION` | integer | 2024 |
| `MES_GENERACION` | integer | 1 |
| `SCF_CODIGO_ORIGEN` | integer | 1 · 18 |
| `SEC_CODIGO_ORIGEN` | text | COB · CAT |
| `SCF_CODIGO_DESTINO` | integer | 1 · 18 |
| `SEC_CODIGO_DESTINO` | text | COB · TEC |
| `ORD_FECHA_INICIO` | date | 2024-01-06 00:00:00.000000 · 2024-01-08 00:00:00.000000 · 2024-01-09 00:00:00.000000 · 2024-01-05 00:00:00.000000 |
| `ANIO_INICIO` | integer | 2024 |
| `MES_INICIO` | integer | 1 |
| `PERIODO_INICIO` | integer | 202401 |
| `ORD_FECHA_VENCIMIENTO` | integer |  · 45309 |
| `ANIO_VENCIMIENTO` | integer |  · 2024 |
| `MES_VENCIMIENTO` | integer |  · 1 |
| `ORD_DATOS_ADICIONALES` | text | XXCO_COBRANZA_PKG : PAGO DOBLE FACTURA … · XXCO_COBRANZA_PKG : PAGO DOBLE FACTURA … · Aut - Proceso:3142695* Adeuda -F-673537… · Manual - · XXCO_COBRANZA_PKG : PAGO DOBLE FACTURA … |
| `ORD_PRIORIDAD` | integer | 1 · 4 |
| `ORD_RESULTADO` | text |  · E · SU |
| `ORD_FECHA_FIN` | integer |  · 45312 · 45310 |
| `ANIO_FIN` | integer |  · 2024 |
| `MES_FIN` | integer |  · 1 |
| `PERIODO_FIN` | integer |  · 202401 |
| `ORD_DATOS_RESULTADOS` | text |  · .C.12012024.F.673537435 .Ea.S.-Actualiz… · PARA ACCEDER A LO SOLICITADO EL CLIENTE… |
| `ORD_FECHA_CARGA_RESULTADO` | integer |  · 45312 · 45310 |
| `ANIO_CARGA_RESULTADO` | integer |  · 2024 |
| `MES_CARGA_RESULTADO` | integer |  · 1 |
| `DOC_TIPO` | text |  · RC |
| `DOC_NUMERO` | integer |  · 72298760 |
| `ODT_NUMERO` | unknown |  |
| `USR_NUMERO_ORIGEN` | integer | 8847 · 92379 · 10507 |
| `USR_NUMERO_DESTINO` | integer |  · 10605 |
| `ORD_SITUACION` | text | P · I |
| `ORD_ESTADO` | text | D · A |
| `SRV_CODIGO_ORIGEN` | unknown |  |
| `CNT_NUMERO_ORIGEN` | unknown |  |
| `TRT_NUMERO_ORIGEN` | unknown |  |
| `ZOP_CODIGO` | unknown |  |
| `CPR_NUMERO` | integer | 3142545 · 3141926 · 3142695 ·  · 3141308 |
| `CNR_NUMERO` | unknown |  |
| `USR_NUMERO_ANULA` | integer |  · 8847 |
| `ORD_DATOS_ANULA` | text |  · . Anulado p/Cobranza..C.12012024.F.6735… |
| `USR_NUMERO_IMPRIME` | integer |  · 92379 · 8666 |
| `ORD_FECHA_ANULA` | decimal |  · 45303.549178241 |
| `RCL_NUMERO` | unknown |  |
| `AGE_CODIGO_ORIGEN` | integer | 0 |
| `AGE_CODIGO_DESTINO` | integer | 0 |
| `USR_NUMERO_EJEC_ORD` | unknown |  |
| `HABILES_INICIO` | integer | 0 · 1 · -1 |
| `HABILES_FIN` | integer | 0 · 10 · 9 |
| `HABILES_VENCIMIENTO` | integer | 0 · 8 |
| `HABILES_CARGA_RESULTADO` | integer | 80 · 10 · 9 |
| `EJECUTADO` | flag | NO · SI |
| `TARIFA` | integer | 140 · 240 |
| `ID_CLASE` | integer | 1 |
| `ID_TENSION` | integer | 1 |
| `ESTADO_ACTUAL_CONTRATO` | text | V |
| `GRUPO_CONTRATO` | text | CC |
| `ID_ENTE` | integer | 5000 |
| `ID_TARIFA_FECHA_GENERACION` | integer | 140 · 180 · 240 · 1400 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/ORDENATIVOS\|ORDENATIVOS]] — match parcial de nombre + 38 columnas en comun
- [[Projects/sigec-explorer/tablas/ORDENATIVOS_HIST\|ORDENATIVOS_HIST]] — 38 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
