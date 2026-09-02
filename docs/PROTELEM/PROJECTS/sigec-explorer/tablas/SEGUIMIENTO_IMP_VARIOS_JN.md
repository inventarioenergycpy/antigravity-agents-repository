---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 13332
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "SEGUIMIENTO_IMP_VARIOS_JN"
---

# 📝 SEGUIMIENTO_IMP_VARIOS_JN

**Filas estimadas:** 13,332

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SIV_TIPO_IMPRESION` | VARCHAR2 | NO |  |
| `SIV_DISTRITO_ORIGEN` | NUMBER | NO |  |
| `CPR_NUMERO` | NUMBER | NO |  |
| `SIV_FECHA_GENERADA` | VARCHAR2 | YES |  |
| `SIV_ESTADO` | VARCHAR2 | YES |  |
| `SIV_NUMERO` | NUMBER | YES |  |
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
- `SIV_NUMERO` → [[SEGUIMIENTO_IMP_VARIOS]] _SIV_NUMERO es PK de SEGUIMIENTO_IMP_VARIOS_
