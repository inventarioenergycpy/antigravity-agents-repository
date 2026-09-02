---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 34
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_CATEGORIAS_ING_BRUTOS"
---

# 🔧 XXCO_CATEGORIAS_ING_BRUTOS

**Filas estimadas:** 34

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CIB_CODIGO` | NUMBER | NO | 🔑 PK |
| `CIB_DESCRIPCION` | VARCHAR2 | YES |  |
| `CIB_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |
| `CIB_REQ_NRO_IB` | VARCHAR2 | YES |  |
| `CIB_REQ_FECHA_TOPE` | VARCHAR2 | YES |  |
| `CIB_TIPO_CONVENIO` | CHAR | YES |  |
| `CIB_INGRESABLE` | CHAR | YES |  |
| `CIB_PORCENTAJE_LUA` | NUMBER | YES |  |

## Tablas que referencian esta tabla

- [[XXCO_ITEMS_ING_BRUTOS]] via `CIB_CODIGO`
