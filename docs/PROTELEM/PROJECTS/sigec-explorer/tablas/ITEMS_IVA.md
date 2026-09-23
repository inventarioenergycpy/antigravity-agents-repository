---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 188
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ITEMS_IVA"
---

# 📋 ITEMS_IVA

**Filas estimadas:** 188

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GII_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `IVV_CODIGO` | NUMBER | NO | 🔑 PK |
| `ITV_PORCENTAJE` | NUMBER | NO |  |
| `TIT_CLAVE` | VARCHAR2 | NO | 🔗 → [[TIPOS_ITEM]] |
| `ITV_FECHA_VIGENCIA` | DATE | NO | 🔑 PK |

## FK declaradas → otras tablas

- **ITV_FK_TIT**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
