---
tipo: tabla
categoria: hist
owner: XXSIGEC
num_rows: 3487830
tags:
  - sigec-explorer
  - tabla
  - hist
aliases:
  - "XXCO_CRONOGRAMAS_LCT_EST_HIST"
---

# 📂 XXCO_CRONOGRAMAS_LCT_EST_HIST

**Filas estimadas:** 3,487,830

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRL_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `CRL_ANIO` | NUMBER | NO | 🔑 PK |
| `CRL_PERIODO` | NUMBER | NO | 🔑 PK |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |
| `RTL_CODIGO` | NUMBER | NO | 🔑 PK |
| `CRL_ESTADO` | VARCHAR2 | NO | 🔑 PK |
| `USR_NUMERO` | NUMBER | YES |  |
| `CLE_FECHA` | DATE | NO | 🔑 PK |
| `MODULO` | VARCHAR2 | YES |  |
| `CLIENT_INFO` | VARCHAR2 | YES |  |
| `MACHINE` | VARCHAR2 | YES |  |
| `USR_NUMERO_TOMA` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `USR_NUMERO_TOMA` → [[XXCO_ALTAS_COLECTOR]] _USR_NUMERO_TOMA es PK de XXCO_ALTAS_COLECTOR_
