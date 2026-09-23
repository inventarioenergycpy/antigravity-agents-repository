---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 14464
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "SECTORES_USUARIOS"
---

# 📋 SECTORES_USUARIOS

**Filas estimadas:** 14,464

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `USR_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[USUARIOS]] |
| `SEC_CODIGO` | VARCHAR2 | NO | 🔑 PK |

## FK declaradas → otras tablas

- **SEC_USR_FK**: `USR_NUMERO` → [[USUARIOS]] (`USR_NUMERO`)
