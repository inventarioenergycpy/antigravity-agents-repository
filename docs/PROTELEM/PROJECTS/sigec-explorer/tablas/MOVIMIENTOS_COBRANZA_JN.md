---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: cobranza
num_rows: 776277
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/cobranza
aliases:
  - "MOVIMIENTOS_COBRANZA_JN"
---

# 📝 MOVIMIENTOS_COBRANZA_JN

**Prefijo `MOV_`:** Movimientos de cobranza (MOVIMIENTOS_COBRANZA)

**Filas estimadas:** 776,277

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `MOV_NUMERO` | NUMBER | NO |  |
| `CPR_NUMERO` | NUMBER | NO |  |
| `URC_CODIGO` | NUMBER | NO |  |
| `MOV_TRANSACCION` | NUMBER | NO |  |
| `MOV_FECHA` | DATE | NO |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |
| `DOC_NUMERO` | NUMBER | YES |  |
| `MOV_IMPORTE` | NUMBER | NO |  |
| `MOV_ERROR` | VARCHAR2 | YES |  |
| `MOV_WARN` | VARCHAR2 | YES |  |
| `MOV_DIFERENCIA` | NUMBER | YES |  |
| `MOV_TRANSACCION_ORIGINAL` | NUMBER | YES |  |
| `MOV_ON_LINE` | VARCHAR2 | YES |  |
| `MOV_ARCHIVO_COBRANZA` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |
| `USR_UNIX` | VARCHAR2 | YES |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |
| `SERVIDOR` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
