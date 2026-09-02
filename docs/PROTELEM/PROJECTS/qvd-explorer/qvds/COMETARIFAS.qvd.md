---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 10
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMETARIFAS.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `TCL_CODIGO` | integer | 503 · 504 · 101 · 103 · 201 |
| `TCL_DESCRIPCION` | text | 5.2 USUAR. ESPECIALES · 5.2.b USUAR. ESPECIALES · 1.a/f RESIDENCIAL · 1.a RESIDENCIAL · 2 GENERAL Y DE SERVICIOS |
| `TCL_GRUPO` | integer | 5 · 1 · 2 |
| `TCL_DEFINICION_CONTABLE` | integer | 611 · 05 · 01 |
| `TCL_LEY_PAE` | flag |  · S |
| `TCL_BASE_LEY` | flag |  · S |
| `TCL_GARANTES_FLAG` | flag | N · S |
| `TCL_COOPERATIVAS_FLAG` | flag | N |
| `TCL_LCT_SITIO` | unknown |  |
| `ES_SOCIAL` | flag | NO |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/TARIFAS\|TARIFAS]] — match parcial de nombre + 9 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
