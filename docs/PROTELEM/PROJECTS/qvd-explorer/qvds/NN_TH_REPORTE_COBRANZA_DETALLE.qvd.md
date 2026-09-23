---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 31
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 NN_TH_REPORTE_COBRANZA_DETALLE.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `PERIODO_VTO` | integer | 202602 · 202603 |
| `FECHA_VENCIMIENTO` | date | 2026-02-27 00:00:00.000000 · 2026-03-16 00:00:00.000000 |
| `FECHA_EMISION` | date | 2023-09-15 00:00:00.000000 · 2026-01-29 00:00:00.000000 |
| `DOC_NUMERO` | integer | 63617383 · 703204907 · 703204910 · 703204911 · 703202010 |
| `DOC_TIPO` | text | F |
| `ID_TARIFA_BASE` | integer | 188 · 140 |
| `ORIGEN` | text | CONSUMO |
| `TABLA_ORIGEN` | text | TH_FACTURACION_CONSUMO |
| `ID_SUCURSAL` | integer | 1 |
| `CONDICION_SUBSIDIO_CONTRATO` | text | SN2 · SN3 · SN1 |
| `ES_TARIFA_SOCIAL` | text | SP · NO |
| `CON_DEUDA` | flag | SI · NO |
| `IMPORTE_ORIGINAL` | decimal | 484.1 · 16227 · 187813.7 · 7441.8 · 32630.4 |
| `FECHA_ESTADO_DEUDA_ACTUAL` | date | 2023-09-15 00:00:00.000000 · 2026-03-13 00:00:00.000000 · 2026-03-28 00:00:00.000000 · 2026-03-12 00:00:00.000000 · 2026-03-10 00:00:00.000000 |
| `ESTADO_DEUDA_ACTUAL` | text | V · C |
| `ID_SUMINISTRO_CONTRATO` | integer | 283461901 · 44533205 · 44666003 · 44685206 · 274374504 |
| `FECHA_CARGA` | date | 2026-05-31 23:30:50.000000 |
| `ID_TARIFA_BASE_ACTUAL` | integer | 189 · 140 |
| `IMPORTE_COBRADO_PARC_VENC_0_3` | decimal | 0 · 16227 · 7441.8 · 32630.4 |
| `IMPORTE_COBRADO_PARC_VENC_4_7` | integer | 0 |
| `IMPORTE_COBRADO_PARC_VENC_8_10` | integer | 0 |
| `IMPORTE_COBRADO_PARC_VENC_MAS_10` | decimal | 0 · 187813.7 |
| `IMPORTE_COBRADO_PARC_VENC_0_30` | decimal | 0 · 16227 · 187813.7 · 7441.8 · 32630.4 |
| `IMPORTE_COBRADO_PARC_VENC_31_60` | integer | 0 |
| `IMPORTE_COBRADO_PARC_VENC_61_90` | integer | 0 |
| `IMPORTE_COBRADO_PARC_VENC_MAS_90` | integer | 0 |
| `IMPORTE_ADEUDADO_PARC_VENC_0_30` | integer | 0 |
| `IMPORTE_ADEUDADO_PARC_VENC_31_60` | integer | 0 |
| `IMPORTE_ADEUDADO_PARC_VENC_61_90` | integer | 0 |
| `IMPORTE_ADEUDADO_PARC_ACTUAL` | integer | 0 |
| `SUM_DEBE_MAS_2_DOCS` | flag | SI · NO |

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
