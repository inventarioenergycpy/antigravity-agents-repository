---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 263113
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_ESTADISTICAS"
---

# 🔧 XXCO_ESTADISTICAS

**Filas estimadas:** 263,113

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CRF_ANIO` | NUMBER | NO | 🔑 PK |
| `CRF_PERIODO` | NUMBER | NO | 🔑 PK |
| `GRF_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `EST_FECHA_EST` | DATE | YES |  |
| `EST_IMPORTE` | NUMBER | YES |  |
| `EST_TIPO` | VARCHAR2 | YES |  |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |
| `EST_CODIGO` | NUMBER | NO | 🔑 PK |
| `EST_CASOS` | NUMBER | YES |  |
| `EST_COMPROBANTES` | NUMBER | NO | 🔑 PK |

## Tablas que referencian esta tabla

- [[XXCO_ESTADISTICAS_POST]] via `CRF_ANIO`, `CRF_PERIODO`, `EST_CODIGO`, `EST_COMPROBANTES`, `GRF_CODIGO`, `SCF_CODIGO`
