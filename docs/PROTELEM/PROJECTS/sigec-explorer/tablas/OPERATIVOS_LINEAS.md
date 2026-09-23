---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 3426
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "OPERATIVOS_LINEAS"
---

# 📋 OPERATIVOS_LINEAS

**Filas estimadas:** 3,426

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `OPE_NUMERO` | NUMBER | YES | 🔗 → [[OPERATIVOS]] |
| `LIN_CODIGO` | VARCHAR2 | YES |  |
| `OLI_OBSERVACIONES` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **OLI_OPE_FK**: `OPE_NUMERO` → [[OPERATIVOS]] (`OPE_NUMERO`)

## FK inferidas (alta confianza)

- `OPE_NUMERO` → [[OPERATIVOS]] _OPE_NUMERO es PK de OPERATIVOS_
