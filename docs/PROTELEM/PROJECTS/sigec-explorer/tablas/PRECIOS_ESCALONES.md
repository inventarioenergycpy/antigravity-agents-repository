---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 292443
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PRECIOS_ESCALONES"
---

# 📋 PRECIOS_ESCALONES

**Filas estimadas:** 292,443

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TAB_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[DETALLES_LISTA]] |
| `CON_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[DETALLES_LISTA]] |
| `ESC_NUMERO` | NUMBER | NO | 🔑 PK |
| `PES_PRECIO_UNIT` | NUMBER | NO |  |
| `PES_MONEDA` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **PES_FK_DLI**: `CON_NUMERO`, `TAB_NUMERO` → [[DETALLES_LISTA]] (`CON_NUMERO`, `TAB_NUMERO`)
