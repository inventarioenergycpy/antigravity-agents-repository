---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 5
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "GRUPOS_USUARIO"
---

# 📋 GRUPOS_USUARIO

**Filas estimadas:** 5

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRU_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `GRU_DESCRIPCION` | VARCHAR2 | NO |  |
| `GRU_PRIORIDAD` | NUMBER | NO |  |

## Tablas que referencian esta tabla

- [[USUARIOS]] via `GRU_CODIGO`
