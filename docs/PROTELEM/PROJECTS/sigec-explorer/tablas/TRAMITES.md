---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 44779203
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "TRAMITES"
---

# 📋 TRAMITES

> Tabla de trámites

**Filas estimadas:** 44,779,203

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TRT_NUMERO` | NUMBER | NO | 🔑 PK |
| `CPR_NUMERO` | NUMBER | YES |  |
| `TRT_PAGO_TOTAL` | VARCHAR2 | YES |  |
| `TRT_ULTIMA_ACTUALIZACION` | DATE | YES |  |

## Tablas que referencian esta tabla

- [[DOC_TRT_JN]] via `TRT_NUMERO_IN`, `TRT_NUMERO_OUT`
- [[ORDENATIVOS_INT_COBRO]] via `TRT_NUMERO`
