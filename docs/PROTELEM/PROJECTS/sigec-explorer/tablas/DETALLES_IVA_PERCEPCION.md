---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 33
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "DETALLES_IVA_PERCEPCION"
---

# 📋 DETALLES_IVA_PERCEPCION

**Filas estimadas:** 33

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `IVV_CODIGO` | NUMBER | NO | 🔑 PK |
| `DPP_MINIMO` | NUMBER | YES |  |
| `DPP_FECHA_VIGENCIA` | DATE | NO | 🔑 PK |
| `DPP_PORCENTAJE` | NUMBER | YES |  |
| `TIT_CLAVE` | VARCHAR2 | YES | 🔗 → [[TIPOS_ITEM]] |

## FK declaradas → otras tablas

- **DPP_FK_TIT**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
