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

# 📦 COMEORDENATIVOS_2020.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `TRT_NUMERO` | integer | 36641141 · 36833770 · 36641151 · 36641153 |
| `TOR_CODIGO` | text | CO · IG · NT |
| `ORD_NUMERO` | integer | 64284759 · 64284760 · 64284761 · 64284762 · 64284763 |
| `SRV_CODIGO` | integer | 867823 · 517026 · 872718 · 873655 |
| `CNT_NUMERO` | integer | 2 · 3 · 6 |
| `PRS_NUMERO` | integer | 680462 · 935419 · 926572 · 5640875 |
| `FECHA_GENERACION` | date | 12/01/2020 |
| `PERIODO_GENERACION` | integer | 202001 |
| `ANIO_GENERACION` | integer | 2020 |
| `MES_GENERACION` | integer | 1 |
| `SCF_CODIGO_ORIGEN` | integer | 1 |
| `SEC_CODIGO_ORIGEN` | text | COB |
| `SCF_CODIGO_DESTINO` | integer | 1 |
| `SEC_CODIGO_DESTINO` | text | MED · COB |
| `ORD_FECHA_INICIO` | date | 2020-01-12 00:00:00.000000 · 2020-01-15 00:00:00.000000 |
| `ANIO_INICIO` | integer | 2020 |
| `MES_INICIO` | integer | 1 |
| `PERIODO_INICIO` | integer | 202001 |
| `ORD_FECHA_VENCIMIENTO` | decimal | 43847.81724537 · 43857 ·  |
| `ANIO_VENCIMIENTO` | integer | 2020 ·  |
| `MES_VENCIMIENTO` | integer | 1 ·  |
| `ORD_DATOS_ADICIONALES` | text | Vencimiento de Ordenativo Anterior IN-6… · Garantizado:867823/2 Por garantia de de… · Vencimiento de Ordenativo Anterior IN-6… · Garante del Suministro 872718 sin Contr… · Vencimiento de Ordenativo Anterior IN-6… |
| `ORD_PRIORIDAD` | integer | 1 |
| `ORD_RESULTADO` | text |  · E |
| `ORD_FECHA_FIN` | integer |  · 43860 |
| `ANIO_FIN` | integer |  · 2020 |
| `MES_FIN` | integer |  · 1 |
| `PERIODO_FIN` | integer |  · 202001 |
| `ORD_DATOS_RESULTADOS` | text | .C.20012020.F.618496815 D.204814 .Ea.D. · .C.20012020.G.F.618496815 D.204814 .Ea.… · .C-Sin RX.15012020.F.618485694 .Ea.D. ·  |
| `ORD_FECHA_CARGA_RESULTADO` | decimal |  · 43860 · 43842.81724537 |
| `ANIO_CARGA_RESULTADO` | integer |  · 2020 |
| `MES_CARGA_RESULTADO` | integer |  · 1 |
| `DOC_TIPO` | unknown |  |
| `DOC_NUMERO` | unknown |  |
| `ODT_NUMERO` | unknown |  |
| `USR_NUMERO_ORIGEN` | integer | 8 |
| `USR_NUMERO_DESTINO` | unknown |  |
| `ORD_SITUACION` | text | P · I |
| `ORD_ESTADO` | text | A |
| `SRV_CODIGO_ORIGEN` | integer |  · 867823 |
| `CNT_NUMERO_ORIGEN` | integer |  · 2 |
| `TRT_NUMERO_ORIGEN` | integer |  · 36641141 |
| `ZOP_CODIGO` | integer | 01 ·  |
| `CPR_NUMERO` | integer |  · 2618951 |
| `CNR_NUMERO` | unknown |  |
| `USR_NUMERO_ANULA` | integer | 1 · 9440 |
| `ORD_DATOS_ANULA` | text | . Anulado Rap.On.Line..C.20012020.F.618… · . Anulado Rap.On.Line..C.20012020.G.F.6… · . Anulado Rap.On.Line..C-Sin RX.1501202… · Anul.Aut.Res.E del ordentivo RP-64597289 |
| `USR_NUMERO_IMPRIME` | integer |  · 8710 · 90069 |
| `ORD_FECHA_ANULA` | decimal | 43850.419849537 · 43845.753194444 · 43882 |
| `RCL_NUMERO` | unknown |  |
| `AGE_CODIGO_ORIGEN` | integer | 2 · 0 |
| `AGE_CODIGO_DESTINO` | integer | 2 · 0 |
| `USR_NUMERO_EJEC_ORD` | unknown |  |
| `HABILES_INICIO` | integer | 0 · 2 · 4 |
| `HABILES_FIN` | integer | 0 · 13 |
| `HABILES_VENCIMIENTO` | integer | 4 · 10 · 0 |
| `HABILES_CARGA_RESULTADO` | integer | 83 · 13 · 80 · 0 · 104 |
| `EJECUTADO` | flag | NO · SI |
| `TARIFA` | integer | 240 · 184 · 140 |
| `ID_CLASE` | integer | 1 |
| `ID_TENSION` | integer | 1 |
| `ESTADO_ACTUAL_CONTRATO` | text | V · C |
| `GRUPO_CONTRATO` | text | CC |
| `ID_ENTE` | integer | 5000 |
| `ID_TARIFA_FECHA_GENERACION` | integer | 240 · 184 · 140 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/ORDENATIVOS\|ORDENATIVOS]] — match parcial de nombre + 38 columnas en comun
- [[Projects/sigec-explorer/tablas/ORDENATIVOS_HIST\|ORDENATIVOS_HIST]] — 38 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
