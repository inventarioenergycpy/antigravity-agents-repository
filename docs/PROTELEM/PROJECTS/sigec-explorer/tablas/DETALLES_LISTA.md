---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 336020
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "DETALLES_LISTA"
---

# 📋 DETALLES_LISTA

**Filas estimadas:** 336,020

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TAB_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[PRECIOS_TARIFA]] |
| `CON_NUMERO` | NUMBER | NO | 🔑 PK |
| `DLI_PRECIO_UNIT` | NUMBER | NO |  |
| `DLI_OBSERVACIONES` | VARCHAR2 | YES |  |
| `DLI_CANTIDAD` | NUMBER | YES |  |
| `DLI_MONEDA` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **DLI_FK_TAB**: `TAB_NUMERO` → [[PRECIOS_TARIFA]] (`TAB_NUMERO`)

## Tablas que referencian esta tabla

- [[PRECIOS_ESCALONES]] via `CON_NUMERO`, `TAB_NUMERO`
