---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 19673
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "CRONOGRAMAS_LECTURA_JN"
---

# 📝 CRONOGRAMAS_LECTURA_JN

**Filas estimadas:** 19,673

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SCF_CODIGO` | NUMBER | NO |  |
| `GRL_CODIGO` | VARCHAR2 | NO |  |
| `RTL_CODIGO` | NUMBER | NO |  |
| `CRL_PERIODO` | NUMBER | NO |  |
| `CRL_ANIO` | NUMBER | NO |  |
| `CRL_FECHA_PREVISTA` | DATE | YES |  |
| `CRL_FECHA_EMISION` | DATE | YES |  |
| `JN_USER` | NUMBER | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `OBSERVACION` | VARCHAR2 | YES |  |
| `ANIO_BIMESTRE` | NUMBER | YES |  |
| `NRO_BIMESTRE` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
