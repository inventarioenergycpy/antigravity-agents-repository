---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 12
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "TIPOS_LEY"
---

# 📋 TIPOS_LEY

**Filas estimadas:** 12

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TLY_CODIGO` | NUMBER | NO | 🔑 PK |
| `TLY_DESCRIPCION` | VARCHAR2 | NO |  |
| `TLY_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[DETALLES_IMPUESTO]] via `TLY_CODIGO`
