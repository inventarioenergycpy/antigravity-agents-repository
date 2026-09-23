---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 15
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "CATEGORIAS"
---

# 📋 CATEGORIAS

**Filas estimadas:** 15

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CAT_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `CAT_DESCRIPCION` | VARCHAR2 | NO |  |
| `CAT_GRUPO` | VARCHAR2 | NO |  |
| `CAT_CODIGO1` | VARCHAR2 | YES |  |
| `CAT_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[CONTRATOS]] via `CAT_CODIGO`
