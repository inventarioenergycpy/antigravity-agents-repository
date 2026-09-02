---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 623
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ITEMS_MENU"
---

# 📋 ITEMS_MENU

**Filas estimadas:** 623

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `IME_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `IME_CODIGO_PADRE` | VARCHAR2 | YES |  |
| `IME_DESCRIPCION` | VARCHAR2 | NO |  |
| `IME_HABILITADO` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[ROLES_ITEMS]] via `IME_CODIGO`
