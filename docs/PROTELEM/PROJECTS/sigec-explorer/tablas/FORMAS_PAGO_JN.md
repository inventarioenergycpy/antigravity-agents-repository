---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 278
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "FORMAS_PAGO_JN"
---

# 📝 FORMAS_PAGO_JN

**Filas estimadas:** 278

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `FPG_NUMERO` | NUMBER | NO |  |
| `URC_CODIGO` | NUMBER | NO |  |
| `FPG_TIPO` | VARCHAR2 | NO |  |
| `FPG_CHEQUE` | NUMBER | YES |  |
| `FPG_DIAS_ACREDITACION` | NUMBER | YES |  |
| `FPG_FECHA` | DATE | YES |  |
| `FPG_IMPORTE` | NUMBER | NO |  |
| `FPG_ESTADO` | VARCHAR2 | YES |  |
| `URC_CODIGO_DEPOSITO` | NUMBER | YES |  |
| `FPG_NRO_AUTORIZA` | NUMBER | YES |  |
| `URC_CODIGO_TARJETA` | NUMBER | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `FPG_SUCURSAL_CHEQUE` | NUMBER | YES |  |
| `BOL_NUMERO` | NUMBER | YES |  |
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
