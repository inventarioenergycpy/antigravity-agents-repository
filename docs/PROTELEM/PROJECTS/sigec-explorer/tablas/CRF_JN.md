---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 457627
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "CRF_JN"
---

# 📝 CRF_JN

**Filas estimadas:** 457,627

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRF_CODIGO` | VARCHAR2 | YES |  |
| `CRF_ANIO` | NUMBER | YES |  |
| `CRF_PERIODO` | NUMBER | YES |  |
| `MPA_TIPO_MEDIO` | VARCHAR2 | YES |  |
| `CRF_FECHA_LECTURA` | DATE | YES |  |
| `CRF_FECHA_PREVISTA` | DATE | YES |  |
| `CRF_FECHA_PRECIOS` | DATE | YES |  |
| `CRF_DIAS_VENC_1` | NUMBER | YES |  |
| `CRF_DIAS_VENC_2` | NUMBER | YES |  |
| `CRF_DIAS_VENC_3` | NUMBER | YES |  |
| `CRF_DIAS_VENC` | NUMBER | YES |  |
| `JN_USER` | NUMBER | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `CRF_FECHA_LECTURA_MIN` | DATE | YES |  |
| `OBSERVACION` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
