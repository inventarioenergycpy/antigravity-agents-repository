---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 1541
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_REPLICAS_TARIFAS_CONFEC"
---

# 🔧 XXCO_REPLICAS_TARIFAS_CONFEC

**Filas estimadas:** 1,541

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PCC_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_TARIFAS_BASE_CONFECCIONES]] |
| `TCL_CODIGO_BASE` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_TARIFAS_BASE_CONFECCIONES]] |
| `CLA_CODIGOS` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_TARIFAS_BASE_CONFECCIONES]] |
| `TEN_CODIGOS` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_TARIFAS_BASE_CONFECCIONES]] |
| `TCL_CODIGO_BASE_REP` | VARCHAR2 | NO | 🔑 PK |
| `CLA_CODIGOS_REP` | VARCHAR2 | NO | 🔑 PK |
| `TEN_CODIGOS_REP` | VARCHAR2 | NO | 🔑 PK |
| `RTC_VARIACION_REPLICA` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **XXCO_TBC_RTC_FK**: `PCC_NUMERO`, `TCL_CODIGO_BASE`, `CLA_CODIGOS`, `TEN_CODIGOS` → [[XXCO_TARIFAS_BASE_CONFECCIONES]] (`PCC_NUMERO`, `TCL_CODIGO_BASE`, `CLA_CODIGOS`, `TEN_CODIGOS`)
