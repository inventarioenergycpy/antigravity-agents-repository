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
  - "CRONOGRAMAS"
---

# 📋 CRONOGRAMAS

**Filas estimadas:** 12

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRF_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `CRO_ANIO` | NUMBER | NO | 🔑 PK |
| `CRO_PERIODO` | NUMBER | NO | 🔑 PK |
| `CRO_FECHA_PREVISTA` | DATE | NO |  |
| `CRO_FECHA_EMISION` | DATE | YES |  |
| `CRO_FECHA_CONTROL` | DATE | YES |  |
| `CRO_FECHA_OK` | DATE | YES |  |
| `CRO_ESTADO` | VARCHAR2 | YES |  |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |
