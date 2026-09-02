---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 7
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "RED_TIPOS"
---

# 📋 RED_TIPOS

**Filas estimadas:** 7

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RTI_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `RTI_DESCRIPCION` | VARCHAR2 | YES |  |
| `RTI_CONCURRENTE` | VARCHAR2 | YES |  |
| `RTI_PAGO_MASIVO` | VARCHAR2 | YES |  |
| `RTI_ACTIVO` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[RED_MONITOR]] via `RTI_TIPO`
