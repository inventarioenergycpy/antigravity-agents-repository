---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 11
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMEINFORMESVARIOS_ALICUOTA.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `INV_NUMERO` | integer | 4015 |
| `TIT_CLAVE` | text | OIM |
| `TIV_CODIGO` | text | OIM |
| `TIV_SIGNO` | text | NEG |
| `SCF_CODIGO` | integer | 1 |
| `AGF_CODIGO` | integer | 1000 |
| `TIV_TIPO` | text | COB |
| `DIE_MES_EMISION` | integer | 201104 · 201201 · 201205 · 201410 · 201504 |
| `ALI_CUOTA` | integer | 10 |
| `DIE_IMPORTE` | decimal | -0,43 · -6,98 · -6,08 · -2,26 · -0,35 |
| `DIE_CANTIDAD_ITEMS` | integer | 1 · 2 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/XX_DETALLE_INFORMES_VARIOS\|XX_DETALLE_INFORMES_VARIOS]] — 10 columnas en comun
- [[Projects/sigec-explorer/tablas/XX_TOTALES_INFORMES_VARIOS\|XX_TOTALES_INFORMES_VARIOS]] — 7 columnas en comun
- [[Projects/sigec-explorer/tablas/XX_TIT_INFORMES_ESTATALES\|XX_TIT_INFORMES_ESTATALES]] — 3 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
