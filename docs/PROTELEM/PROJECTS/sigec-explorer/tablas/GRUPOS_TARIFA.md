---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1011
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "GRUPOS_TARIFA"
---

# 📋 GRUPOS_TARIFA

**Filas estimadas:** 1,011

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GTA_GRP_ID` | NUMBER | NO | 🔑 PK · 🔗 → [[GRUPOS]] |
| `GTA_HABILITADO` | VARCHAR2 | NO |  |
| `GTA_TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `GTA_CLA_CODIGO` | VARCHAR2 | NO | 🔑 PK |

## FK declaradas → otras tablas

- **GTA_GRP_FK**: `GTA_GRP_ID` → [[GRUPOS]] (`GRP_ID`)
