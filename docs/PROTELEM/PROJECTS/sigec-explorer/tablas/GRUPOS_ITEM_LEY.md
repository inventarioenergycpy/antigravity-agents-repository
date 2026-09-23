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
  - "GRUPOS_ITEM_LEY"
---

# 📋 GRUPOS_ITEM_LEY

**Filas estimadas:** 5

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GIL_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `GIL_DESCRIPCION` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[DETALLES_IMPUESTO]] via `GIL_CODIGO`
- [[TIPOS_ITEM]] via `GIL_CODIGO`
