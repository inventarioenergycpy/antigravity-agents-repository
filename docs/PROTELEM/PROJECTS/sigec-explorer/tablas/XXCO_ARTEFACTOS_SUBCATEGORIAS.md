---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 16
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_ARTEFACTOS_SUBCATEGORIAS"
---

# 🔧 XXCO_ARTEFACTOS_SUBCATEGORIAS

**Filas estimadas:** 16

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SUB_CODIGO` | NUMBER | NO | 🔑 PK |
| `SUB_DESCRIPCION` | VARCHAR2 | YES |  |
| `CAT_CODIGO` | NUMBER | YES | 🔗 → [[XXCO_ARTEFACTOS_CATEGORIAS]] |
| `SUB_FECHA_ALTA` | DATE | YES |  |
| `SUB_FECHA_BAJA` | DATE | YES |  |
| `SUB_USER_ALTA` | VARCHAR2 | YES |  |
| `SUB_USER_BAJA` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **XXCO_SUB_CAT_FK**: `CAT_CODIGO` → [[XXCO_ARTEFACTOS_CATEGORIAS]] (`CAT_CODIGO`)

## Tablas que referencian esta tabla

- [[TIPOS_ARTEFACTOS]] via `SUB_CODIGO`
