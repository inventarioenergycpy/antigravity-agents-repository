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

# 📦 COMEORDENATIVOS_2017.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `TRT_NUMERO` | integer | 29825744 · 29825852 · 29825858 |
| `TOR_CODIGO` | text | IM · CN · PM |
| `ORD_NUMERO` | integer | 55096288 · 55096324 · 55096430 · 55096440 · 55096466 |
| `SRV_CODIGO` | integer | 2845212 · 358856 · 1072197 |
| `CNT_NUMERO` | integer | 1 · 2 |
| `PRS_NUMERO` | integer | 1094349 · 1150468 · 265105 |
| `FECHA_GENERACION` | date | 06/01/2017 |
| `PERIODO_GENERACION` | integer | 201701 |
| `ANIO_GENERACION` | integer | 2017 |
| `MES_GENERACION` | integer | 1 |
| `SCF_CODIGO_ORIGEN` | integer | 27 |
| `SEC_CODIGO_ORIGEN` | text | LAB |
| `SCF_CODIGO_DESTINO` | integer | 27 |
| `SEC_CODIGO_DESTINO` | text | LAB · MED · MEDESP |
| `ORD_FECHA_INICIO` | text | 1/6/2017 12:00:00 AM · 1/11/2017 12:00:00 AM · 9/12/2017 12:00:00 AM |
| `ANIO_INICIO` | integer | 2017 |
| `MES_INICIO` | integer | 1 · 9 |
| `PERIODO_INICIO` | integer | 201701 · 201709 |
| `ORD_FECHA_VENCIMIENTO` | unknown |  |
| `ANIO_VENCIMIENTO` | unknown |  |
| `MES_VENCIMIENTO` | unknown |  |
| `ORD_DATOS_ADICIONALES` | text | Manual -NO REGISTRA CONSUMO DESDE SU IN… · Generado por el resultado A del ordenat… · Manual -NORMALIZAR PUNTO DE MEDICION CO… · Manual -PUNTO DE MEDICION DAÑADO.- · Generado por el resultado NP del ordena… |
| `ORD_PRIORIDAD` | integer | 4 · 1 |
| `ORD_RESULTADO` | text | A · E · NP |
| `ORD_FECHA_FIN` | text | 1/6/2017 12:00:00 AM · 4/11/2017 12:00:00 AM · 1/17/2017 12:00:00 AM · 11/7/2017 12:00:00 AM |
| `ANIO_FIN` | integer | 2017 |
| `MES_FIN` | integer | 1 · 4 · 11 |
| `PERIODO_FIN` | integer | 201701 · 201704 · 201711 |
| `ORD_DATOS_RESULTADOS` | text | MEDIDOR SIN FUNCIONAR.-EMPLAZAR AL TITU… ·  · EMPLAZAR AL TITULAR PARA QUE REACONDICI… |
| `ORD_FECHA_CARGA_RESULTADO` | text | 1/6/2017 12:00:00 AM · 4/11/2017 12:00:00 AM · 3/15/2017 12:00:00 AM · 6/14/2018 12:00:00 AM |
| `ANIO_CARGA_RESULTADO` | integer | 2017 · 2018 |
| `MES_CARGA_RESULTADO` | integer | 1 · 4 · 3 · 6 |
| `DOC_TIPO` | unknown |  |
| `DOC_NUMERO` | unknown |  |
| `ODT_NUMERO` | unknown |  |
| `USR_NUMERO_ORIGEN` | integer | 8495 |
| `USR_NUMERO_DESTINO` | integer | 8495 · 8425 · 3742 |
| `ORD_SITUACION` | text | I |
| `ORD_ESTADO` | text | D |
| `SRV_CODIGO_ORIGEN` | unknown |  |
| `CNT_NUMERO_ORIGEN` | unknown |  |
| `TRT_NUMERO_ORIGEN` | unknown |  |
| `ZOP_CODIGO` | unknown |  |
| `CPR_NUMERO` | unknown |  |
| `CNR_NUMERO` | integer | 45257828 ·  · 45258791 |
| `USR_NUMERO_ANULA` | unknown |  |
| `ORD_DATOS_ANULA` | unknown |  |
| `USR_NUMERO_IMPRIME` | integer | 8495 · 8425 · 3742 |
| `ORD_FECHA_ANULA` | unknown |  |
| `RCL_NUMERO` | unknown |  |
| `AGE_CODIGO_ORIGEN` | integer | 0 |
| `AGE_CODIGO_DESTINO` | integer | 0 |
| `USR_NUMERO_EJEC_ORD` | integer | 8495 · 6571 · 3742 |
| `HABILES_INICIO` | integer | 0 · 3 · 166 |
| `HABILES_FIN` | integer | 0 · 64 · 7 · 204 |
| `HABILES_VENCIMIENTO` | integer | 0 |
| `HABILES_CARGA_RESULTADO` | integer | 0 · 64 · 46 · 347 |
| `EJECUTADO` | flag | SI |
| `TARIFA` | integer | 140 · 144 · 541 |
| `ID_CLASE` | integer | 1 |
| `ID_TENSION` | integer | 1 |
| `ESTADO_ACTUAL_CONTRATO` | text | V |
| `GRUPO_CONTRATO` | text | CC · GC |
| `ID_ENTE` | integer | 5000 · 3525 |
| `ID_TARIFA_FECHA_GENERACION` | integer | 140 · 144 · 541 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/ORDENATIVOS\|ORDENATIVOS]] — match parcial de nombre + 38 columnas en comun
- [[Projects/sigec-explorer/tablas/ORDENATIVOS_HIST\|ORDENATIVOS_HIST]] — 38 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
