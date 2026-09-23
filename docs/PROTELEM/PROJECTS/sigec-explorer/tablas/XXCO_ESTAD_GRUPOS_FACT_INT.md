---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 25476
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_ESTAD_GRUPOS_FACT_INT"
---

# 🔧 XXCO_ESTAD_GRUPOS_FACT_INT

**Filas estimadas:** 25,476

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CRF_ANIO` | NUMBER | YES | 🔗 → [[XXCO_ESTAD_GRUPOS_FACT]] |
| `CRF_PERIODO` | NUMBER | YES | 🔗 → [[XXCO_ESTAD_GRUPOS_FACT]] |
| `GRF_CODIGO` | VARCHAR2 | YES | 🔗 → [[XXCO_ESTAD_GRUPOS_FACT]] |
| `SCF_CODIGO` | NUMBER | YES | 🔗 → [[XXCO_ESTAD_GRUPOS_FACT]] |
| `EST_ESTADO` | VARCHAR2 | YES |  |
| `FECHA_REAL_INTIMACION` | DATE | YES |  |
| `FECHA_CARGA` | DATE | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `EGI_CODIGO` | NUMBER | NO | 🔑 PK |
| `EST_CODIGO` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **XXCO_ESTAD_GRUPOS_FACT_INT_R01**: `GRF_CODIGO`, `CRF_PERIODO`, `CRF_ANIO`, `SCF_CODIGO` → [[XXCO_ESTAD_GRUPOS_FACT]] (`GRF_CODIGO`, `CRF_PERIODO`, `CRF_ANIO`, `SCF_CODIGO`)
