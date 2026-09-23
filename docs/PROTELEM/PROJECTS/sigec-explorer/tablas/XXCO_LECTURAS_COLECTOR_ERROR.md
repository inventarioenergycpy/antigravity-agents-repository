---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 2605597
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_LECTURAS_COLECTOR_ERROR"
---

# 🔧 XXCO_LECTURAS_COLECTOR_ERROR

**Filas estimadas:** 2,605,597

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `LCE_NUMERO` | NUMBER | NO | 🔑 PK |
| `LCR_FECHA_ERROR` | DATE | NO |  |
| `LCR_ERROR` | VARCHAR2 | NO |  |
| `LCT_DESCRIPCION_ERROR` | VARCHAR2 | YES |  |
| `GRL_CODIGO` | VARCHAR2 | NO |  |
| `CRL_PERIODO` | NUMBER | NO |  |
| `CRL_ANIO` | NUMBER | NO |  |
| `SCF_CODIGO` | NUMBER | NO |  |
| `RTL_CODIGO` | NUMBER | NO |  |
| `LCR_FECHA_PROCESO` | DATE | NO |  |
| `LCE_CANTIDAD` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `LCR_FECHA_PROCESO` → [[XXCO_CRONOGRAMAS_LECTURA_TOT]] _LCR_FECHA_PROCESO es PK de XXCO_CRONOGRAMAS_LECTURA_TOT_
