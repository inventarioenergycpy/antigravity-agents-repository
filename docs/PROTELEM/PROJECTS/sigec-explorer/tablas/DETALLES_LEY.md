---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 41
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "DETALLES_LEY"
---

# 📋 DETALLES_LEY

**Filas estimadas:** 41

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TLY_CODIGO` | NUMBER | NO | 🔑 PK |
| `LYD_CODIGO` | NUMBER | NO | 🔑 PK |
| `TIT_CLAVE` | VARCHAR2 | NO | 🔗 → [[TIPOS_ITEM]] |
| `LYD_DESCRIPCION` | VARCHAR2 | YES |  |
| `LYD_FECHA_VIGENCIA` | DATE | YES |  |
| `LYD_FECHA_FIN` | DATE | YES |  |
| `LYD_MINIMO` | NUMBER | YES |  |
| `LYD_PORCENTAJE` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **LYD_FK_TIT**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
