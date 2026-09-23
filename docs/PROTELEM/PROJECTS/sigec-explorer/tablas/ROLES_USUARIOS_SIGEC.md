---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 15191
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ROLES_USUARIOS_SIGEC"
---

# 📋 ROLES_USUARIOS_SIGEC

**Filas estimadas:** 15,191

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `USR_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[USUARIOS]] |
| `ROL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[ROLES_SIGEC]] |

## FK declaradas → otras tablas

- **RUS_ROL_FK**: `ROL_CODIGO` → [[ROLES_SIGEC]] (`ROL_CODIGO`)
- **RUS_USR_FK**: `USR_NUMERO` → [[USUARIOS]] (`USR_NUMERO`)
