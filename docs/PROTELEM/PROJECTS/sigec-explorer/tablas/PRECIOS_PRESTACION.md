---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 3594
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PRECIOS_PRESTACION"
---

# 📋 PRECIOS_PRESTACION

**Filas estimadas:** 3,594

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TIT_CLAVE` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TIPOS_ITEM]] |
| `PPR_FECHA_VIGENCIA` | DATE | NO | 🔑 PK |
| `PPR_PRECIO` | NUMBER | NO |  |

## FK declaradas → otras tablas

- **PPR_FK_TIT**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
