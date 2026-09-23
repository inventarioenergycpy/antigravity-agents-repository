---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 5582
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "SEGUIMIENTO_IMP_FACTURAS_JN"
---

# 📝 SEGUIMIENTO_IMP_FACTURAS_JN

**Filas estimadas:** 5,582

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SIF_GRUPO_CLIENTE` | VARCHAR2 | NO |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |
| `CRF_ANIO` | NUMBER | YES |  |
| `CRF_PERIODO` | NUMBER | YES |  |
| `SIF_SECUENCIA` | NUMBER | NO |  |
| `SIF_CANT_SECUENCIA` | NUMBER | NO |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |
| `SIF_DOC_NRO_DESDE` | VARCHAR2 | YES |  |
| `SIF_DOC_NRO_HASTA` | VARCHAR2 | YES |  |
| `SIF_ESTADO` | VARCHAR2 | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `SIF_NOM_ARCHIVO` | VARCHAR2 | YES |  |
| `SIF_NUMERO` | NUMBER | YES |  |
| `USR_UNIX` | VARCHAR2 | YES |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |
| `SERVIDOR` | VARCHAR2 | YES |  |
| `TERMINAL` | VARCHAR2 | YES |  |
| `OPERACION` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |
| `OBSERVACION` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `SIF_NUMERO` → [[SEGUIMIENTO_IMP_FACTURAS]] _SIF_NUMERO es PK de SEGUIMIENTO_IMP_FACTURAS_
