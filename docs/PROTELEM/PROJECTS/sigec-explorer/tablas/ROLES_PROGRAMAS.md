---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 66
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ROLES_PROGRAMAS"
---

# 📋 ROLES_PROGRAMAS

**Filas estimadas:** 66

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PRG_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[PROGRAMAS]] |
| `ROL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[ROLES_SIGEC]] |

## FK declaradas → otras tablas

- **RPG_PRG_FK**: `PRG_CODIGO` → [[PROGRAMAS]] (`PRG_CODIGO`)
- **RPG_ROL_FK**: `ROL_CODIGO` → [[ROLES_SIGEC]] (`ROL_CODIGO`)
