---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_RANGOS_LECTURAS_ESTIMADAS"
---

# 🔧 XXCO_RANGOS_LECTURAS_ESTIMADAS

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RLE_CODIGO` | VARCHAR2 | NO |  |
| `RLE_DESCRIPCION` | VARCHAR2 | YES |  |
| `RLE_CANTIDAD` | NUMBER | YES |  |
| `RLE_FECHA_PRODUCCION` | DATE | YES |  |
| `RLE_FECHA_PROCESADO` | DATE | YES |  |
| `RTL_CODIGO` | NUMBER | YES |  |
| `RTL_ANIO` | NUMBER | YES |  |
| `RTL_PERIODO` | NUMBER | YES |  |
| `RLE_ACTUAL` | VARCHAR2 | YES |  |
| `RLE_NUMERO` | NUMBER | YES |  |
| `RLE_ESTADO` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `RTL_ANIO` → [[XXCO_ALTAS_COLECTOR]] _RTL_ANIO es PK de XXCO_ALTAS_COLECTOR_
- `RTL_PERIODO` → [[XXCO_ALTAS_COLECTOR]] _RTL_PERIODO es PK de XXCO_ALTAS_COLECTOR_
