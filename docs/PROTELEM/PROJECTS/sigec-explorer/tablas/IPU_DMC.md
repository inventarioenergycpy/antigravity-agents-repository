---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 329
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "IPU_DMC"
---

# 📋 IPU_DMC

**Filas estimadas:** 329

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TIT_CLAVE` | VARCHAR2 | NO |  |
| `IPU_PROCESO` | VARCHAR2 | NO |  |
| `MCO_CODIGO_HABER` | VARCHAR2 | NO |  |
| `DMC_ELEMENTO_FIJO` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `IPU_PROCESO` → [[IMPUTACIONES]] _IPU_PROCESO es PK de IMPUTACIONES_
