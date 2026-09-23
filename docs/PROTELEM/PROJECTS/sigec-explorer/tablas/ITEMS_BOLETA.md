---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 214
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ITEMS_BOLETA"
---

# 📋 ITEMS_BOLETA

**Filas estimadas:** 214

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `BOL_CLASE` | VARCHAR2 | NO |  |
| `URC_TIPO_DEPOSITO` | VARCHAR2 | NO |  |
| `URC_TIPO_COBRO` | VARCHAR2 | NO |  |
| `BOLETA_PADRE` | VARCHAR2 | NO |  |
| `TIT_CLAVE` | VARCHAR2 | NO |  |
| `IBO_TIPO` | VARCHAR2 | YES |  |
| `IBO_OBLIGATORIO` | VARCHAR2 | YES |  |
| `IBO_ORDEN` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `BOL_CLASE` → [[VALIDACION_BOLETAS]] _BOL_CLASE es PK de VALIDACION_BOLETAS_
