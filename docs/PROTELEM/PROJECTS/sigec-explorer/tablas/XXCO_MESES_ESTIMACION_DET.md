---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 12
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_MESES_ESTIMACION_DET"
---

# 🔧 XXCO_MESES_ESTIMACION_DET

**Filas estimadas:** 12

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `MES_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_MESES_ESTIMACION]] |
| `MES_NRO` | NUMBER | NO | 🔑 PK |
| `MES_DESCRIPCION` | VARCHAR2 | NO |  |
| `MES_VALOR` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **XXCO_MESES_ESTIMACION_FK**: `MES_CODIGO` → [[XXCO_MESES_ESTIMACION]] (`MES_CODIGO`)
