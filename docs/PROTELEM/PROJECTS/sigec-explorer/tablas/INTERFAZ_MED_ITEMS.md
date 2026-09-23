---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 6690600
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "INTERFAZ_MED_ITEMS"
---

# 📋 INTERFAZ_MED_ITEMS

**Filas estimadas:** 6,690,600

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `IMI_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `IMD_ID` | NUMBER | NO | 🔑 PK · 🔗 → [[INTERFAZ_MED_ORD]] |
| `IMI_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `IMI_VALOR` | NUMBER | YES |  |
| `IMI_UNIDAD` | VARCHAR2 | YES |  |
| `IMI_ENTEROS` | NUMBER | YES |  |
| `IMI_PORCENTAJE_ERROR` | NUMBER | YES |  |
| `IMI_CANT_DEM_PERDIDA` | NUMBER | YES |  |
| `IMI_CANT_DEM_VACIO` | NUMBER | YES |  |
| `IMI_CANT_PUESTA_CERO` | NUMBER | YES |  |
| `IMI_DECIMALES` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **IMI_IMD_FK**: `IMD_ID` → [[INTERFAZ_MED_ORD]] (`IMD_ID`)
