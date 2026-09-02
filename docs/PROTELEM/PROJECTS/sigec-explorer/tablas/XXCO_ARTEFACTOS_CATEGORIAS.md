---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 6
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_ARTEFACTOS_CATEGORIAS"
---

# 🔧 XXCO_ARTEFACTOS_CATEGORIAS

**Filas estimadas:** 6

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CAT_CODIGO` | NUMBER | NO | 🔑 PK |
| `CAT_DESCRIPCION` | VARCHAR2 | YES |  |
| `CAT_FECHA_ALTA` | DATE | YES |  |
| `CAT_FECHA_BAJA` | DATE | YES |  |
| `CAT_USER_ALTA` | VARCHAR2 | YES |  |
| `CAT_USER_BAJA` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[XXCO_ARTEFACTOS_SUBCATEGORIAS]] via `CAT_CODIGO`
