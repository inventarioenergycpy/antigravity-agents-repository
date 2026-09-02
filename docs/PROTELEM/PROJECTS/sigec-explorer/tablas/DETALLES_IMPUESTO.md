---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 17
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "DETALLES_IMPUESTO"
---

# 📋 DETALLES_IMPUESTO

**Filas estimadas:** 17

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GIL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[GRUPOS_ITEM_LEY]] |
| `IMP_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[IMPUESTOS]] |
| `TLY_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[TIPOS_LEY]] |

## FK declaradas → otras tablas

- **DIM_FK_GIL**: `GIL_CODIGO` → [[GRUPOS_ITEM_LEY]] (`GIL_CODIGO`)
- **DIM_FK_IMP**: `IMP_CODIGO` → [[IMPUESTOS]] (`IMP_CODIGO`)
- **DIM_FK_TLY**: `TLY_CODIGO` → [[TIPOS_LEY]] (`TLY_CODIGO`)
