---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 3348
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ROLES_ITEMS"
---

# 📋 ROLES_ITEMS

**Filas estimadas:** 3,348

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ROL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[ROLES_SIGEC]] |
| `IME_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[ITEMS_MENU]] |

## FK declaradas → otras tablas

- **RIT_IME_FK**: `IME_CODIGO` → [[ITEMS_MENU]] (`IME_CODIGO`)
- **RIT_ROL_FK**: `ROL_CODIGO` → [[ROLES_SIGEC]] (`ROL_CODIGO`)
