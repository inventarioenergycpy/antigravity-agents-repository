---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 790777
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "CRONOGRAMAS_LECTURA"
---

# 📋 CRONOGRAMAS_LECTURA

**Filas estimadas:** 790,777

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |
| `RTL_CODIGO` | NUMBER | NO | 🔑 PK |
| `GRL_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `CRL_PERIODO` | NUMBER | NO | 🔑 PK |
| `CRL_ANIO` | NUMBER | NO | 🔑 PK |
| `CRL_FECHA_PREVISTA` | DATE | YES |  |
| `CRL_FECHA_EMISION` | DATE | YES |  |
| `CRL_FECHA_CONTROL` | DATE | YES |  |
| `CRL_FECHA_OK` | DATE | YES |  |
| `CRL_ESTADO` | VARCHAR2 | NO |  |
| `USR_NUMERO_TOMA` | NUMBER | YES |  |
| `USR_NUMERO_TOMA_ANT` | NUMBER | YES |  |
| `CRL_NUMERO_BIMESTRE` | NUMBER | YES |  |
| `CRL_ANIO_BIMESTRE` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `CRL_ESTADO` → [[XXCO_CRONOGRAMAS_LCT_EST_HIST]] _CRL_ESTADO es PK de XXCO_CRONOGRAMAS_LCT_EST_HIST_
- `USR_NUMERO_TOMA` → [[XXCO_ALTAS_COLECTOR]] _USR_NUMERO_TOMA es PK de XXCO_ALTAS_COLECTOR_
