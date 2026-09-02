---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 2
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ETAPAS"
---

# 📋 ETAPAS

**Filas estimadas:** 2

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ETS_CODIGO` | NUMBER | NO | 🔑 PK |
| `ETS_ORDEN` | NUMBER | NO |  |
| `ETS_OBSERVACIONES` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[ACCIONES]] via `ETS_CODIGO`
- [[ACCIONES_TIPO]] via `ETS_CODIGO`
