---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 9
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "TIPOS_MOV_ELEMENTOS"
---

# 📋 TIPOS_MOV_ELEMENTOS

**Filas estimadas:** 9

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TME_ID` | VARCHAR2 | NO | 🔑 PK |
| `TME_DESCRIPCION` | VARCHAR2 | YES |  |
| `TME_TIPO_OPERADOR` | NUMBER | YES |  |
| `TME_VISIBLE` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[STOCK_ELEMENTOS]] via `TME_ID`
