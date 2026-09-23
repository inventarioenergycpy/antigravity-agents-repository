---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ACCIONES_PARAMETROS"
---

# 📋 ACCIONES_PARAMETROS

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PAR_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[PARAMETROS_GEST_JUD]] |
| `ACC_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[ACCIONES]] |

## FK declaradas → otras tablas

- **ACP_ACC_FK**: `ACC_NUMERO` → [[ACCIONES]] (`ACC_NUMERO`)
- **ACP_PGJ_FK**: `PAR_CODIGO` → [[PARAMETROS_GEST_JUD]] (`PAR_CODIGO`)
