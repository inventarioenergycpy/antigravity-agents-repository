---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 23
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "DETALLES_IVA_ADICIONAL"
---

# 📋 DETALLES_IVA_ADICIONAL

**Filas estimadas:** 23

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `IVV_CODIGO` | NUMBER | NO | 🔑 PK |
| `ADI_FECHA_VIGENCIA` | DATE | NO | 🔑 PK |
| `ADI_PORCENTAJE` | NUMBER | NO |  |
| `TIT_CLAVE` | VARCHAR2 | YES | 🔗 → [[TIPOS_ITEM]] |

## FK declaradas → otras tablas

- **ADI_FK_TIT**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
