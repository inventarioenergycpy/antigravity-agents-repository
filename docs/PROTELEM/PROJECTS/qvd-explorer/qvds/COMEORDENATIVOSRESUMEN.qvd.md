---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 37
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMEORDENATIVOSRESUMEN.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `TOR_CODIGO` | text | AC |
| `ANIO_GENERACION` | integer | 2010 |
| `MES_GENERACION` | integer | 1 |
| `FECHA_GENERACION` | date | 04/01/2010 |
| `PERIODO_GENERACION` | integer | 201001 |
| `ANIO_INICIO` | integer | 2009 · 2010 |
| `MES_INICIO` | integer | 12 · 1 |
| `PERIODO_INICIO` | integer | 200912 · 201001 |
| `ORD_RESULTADO` | text |  · E |
| `SCF_CODIGO_ORIGEN` | integer | 28 · 1 · 47 |
| `SEC_CODIGO_ORIGEN` | text | FRAU · LAB |
| `SCF_CODIGO_DESTINO` | integer | 28 · 1 · 47 |
| `SEC_CODIGO_DESTINO` | text | ATSUM · CLIESP |
| `USR_NUMERO_IMPRIME` | unknown |  |
| `ANIO_FIN` | integer |  · 2010 |
| `MES_FIN` | integer |  · 1 |
| `FECHA_FIN` | integer |  · 40199 |
| `PERIODO_FIN` | integer |  · 201001 |
| `USR_NUMERO_ORIGEN` | integer | 4607 · 8451 · 5785 |
| `USR_NUMERO_DESTINO` | integer |  · 9962 |
| `ORD_SITUACION` | text | P · I |
| `ORD_ESTADO` | text | A · D |
| `USR_NUMERO_EJEC_ORD` | unknown |  |
| `HABILES_INICIO` | integer | -2 · 0 |
| `HABILES_FIN` | integer | 0 · 13 |
| `HABILES_CARGA_RESULTADO` | integer | 40 · 860 · 13 |
| `HABILES_INICIO_SUM` | integer | -2 · 0 |
| `HABILES_FIN_SUM` | integer | 0 · 13 |
| `HABILES_CARGA_RESULTADO_SUM` | integer | 40 · 860 · 13 |
| `TARIFA` | integer | 240 · 140 · 180 |
| `ESTADO_ACTUAL_CONTRATO` | text | V · C |
| `EJECUTADO` | flag | NO · SI |
| `ID_CLASE` | integer | 1 |
| `ID_TENSION` | integer | 1 |
| `GRUPO_CONTRATO` | text | CC |
| `ID_ENTE` | integer | 5000 |
| `CANT_ORDENATIVOS` | integer | 1 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/ORDENATIVOS\|ORDENATIVOS]] — match parcial de nombre + 11 columnas en comun
- [[Projects/sigec-explorer/tablas/ORDENATIVOS_HIST\|ORDENATIVOS_HIST]] — 11 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
