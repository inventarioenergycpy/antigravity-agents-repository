---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 148
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_ITEMS_ING_BRUTOS"
---

# 🔧 XXCO_ITEMS_ING_BRUTOS

**Filas estimadas:** 148

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CIB_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_CATEGORIAS_ING_BRUTOS]] |
| `TIT_CLAVE` | VARCHAR2 | YES | 🔗 → [[TIPOS_ITEM]] |
| `IIB_GRUPO_IB` | VARCHAR2 | NO | 🔑 PK |
| `IIB_PORCENTAJE` | NUMBER | YES |  |
| `IIB_FECHA_VIGENCIA` | DATE | NO | 🔑 PK |

## FK declaradas → otras tablas

- **IIB_FK_CIB**: `CIB_CODIGO` → [[XXCO_CATEGORIAS_ING_BRUTOS]] (`CIB_CODIGO`)
- **IIB_FK_TTT**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
