---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1331357
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "RECLAMOS_ASOCIADOS"
---

# 📋 RECLAMOS_ASOCIADOS

**Filas estimadas:** 1,331,357

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RCL_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[RECLAMOS]] |
| `TRO_CODIGO` | VARCHAR2 | NO | 🔑 PK |

## FK declaradas → otras tablas

- **RAS_RCL_FK**: `RCL_NUMERO` → [[RECLAMOS]] (`RCL_NUMERO`)
