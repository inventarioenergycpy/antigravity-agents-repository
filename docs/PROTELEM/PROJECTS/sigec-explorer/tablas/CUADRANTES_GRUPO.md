---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 95
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "CUADRANTES_GRUPO"
---

# 📋 CUADRANTES_GRUPO

**Filas estimadas:** 95

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CUG_GRP_ID` | NUMBER | NO | 🔑 PK · 🔗 → [[GRUPOS]] |
| `CUG_CDR_UNIDAD` | VARCHAR2 | NO | 🔑 PK |
| `CUG_HABILITADO` | VARCHAR2 | NO |  |
| `CUG_VALIDA_CONSUMO` | VARCHAR2 | YES |  |
| `CUG_CONSUMO_FLAG` | VARCHAR2 | YES |  |
| `CUG_CONSUMO` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **CUG_GRP_FK**: `CUG_GRP_ID` → [[GRUPOS]] (`GRP_ID`)
