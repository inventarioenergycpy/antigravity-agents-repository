---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 15
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMEGRPS_FACT.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `GRF_CODIGO` | integer | 01 · 02 · 03 · 05 · 06 |
| `GRF_DESCRIPCION` | text | PLAN 01 - C.C. · PLAN 02 - C.C. · Plan 03 · Plan 05 · Plan 06 |
| `GRF_CODIGO_ANTERIOR` | unknown |  |
| `GRF_FECHA_ESTAD_INTIM` | date | 2010-10-20 00:00:00.000000 · 2011-04-28 00:00:00.000000 · 2010-12-02 00:00:00.000000 |
| `GRF_FECHA_INTIMACION` | date | 2016-10-13 00:00:00.000000 · 2013-09-26 00:00:00.000000 · 2010-11-08 00:00:00.000000 · 2010-11-15 00:00:00.000000 |
| `GRF_CONFIRMA` | unknown |  |
| `TFA_CODIGO` | text | M |
| `GCO_GRUPO` | text | CC |
| `GRF_AUXILIAR` | flag | N |
| `GRF_PAR_IMPAR` | text |  · I |
| `GRF_MESES_LECTURA` | text |  · 01,03,05,07,09,11 |
| `GRF_TIPO_GRUPO` | text | COMUNES |
| `GRF_ESTADO` | text | I |
| `GRF_VARIABLE` | flag | N |
| `GRF_FACTURABLE` | flag | S |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/GRUPOS_FACTURACION\|GRUPOS_FACTURACION]] — 15 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
