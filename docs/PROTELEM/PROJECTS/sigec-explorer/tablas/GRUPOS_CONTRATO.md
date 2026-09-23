---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 8
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "GRUPOS_CONTRATO"
---

# 📋 GRUPOS_CONTRATO

**Filas estimadas:** 8

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GCO_GRUPO` | VARCHAR2 | NO | 🔑 PK |
| `GCO_DESCRIPCION` | VARCHAR2 | NO |  |
| `GCO_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |
| `GCO_TIPO` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[XXCO_PARAM_VALIDADOR_LECTURAS]] via `VLE_GCO_GRUPO`
