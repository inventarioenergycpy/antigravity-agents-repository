---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 3
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "TENSIONES"
---

# 📋 TENSIONES

**Filas estimadas:** 3

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TEN_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TEN_DESCRIPCION` | VARCHAR2 | NO |  |
| `TEN_GRUPO` | VARCHAR2 | NO |  |

## Tablas que referencian esta tabla

- [[COMBINACIONES_HABILITADAS]] via `TEN_CODIGO`
- [[CONTRATOS]] via `TEN_CODIGO`
- [[PRECIOS_CONTRIB_REEMBOL]] via `TEN_CODIGO`
- [[PRECIOS_TARIFA]] via `TEN_CODIGO`
