---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 195
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ROLES_SIGEC"
---

# 📋 ROLES_SIGEC

**Filas estimadas:** 195

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ROL_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `ROL_DESCRIPCION` | VARCHAR2 | NO |  |
| `ROL_TIPO` | VARCHAR2 | NO |  |

## Tablas que referencian esta tabla

- [[ROLES_ITEMS]] via `ROL_CODIGO`
- [[ROLES_PROGRAMAS]] via `ROL_CODIGO`
- [[ROLES_USUARIOS_SIGEC]] via `ROL_CODIGO`
