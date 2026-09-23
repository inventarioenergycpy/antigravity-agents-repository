---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 23527
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "DETALLES_BOLETA_JN"
---

# 📝 DETALLES_BOLETA_JN

**Filas estimadas:** 23,527

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `BOL_NUMERO` | NUMBER | YES |  |
| `URC_CODIGO_DEPOSITO` | NUMBER | YES |  |
| `TIT_CLAVE` | VARCHAR2 | YES |  |
| `DBO_IMPORTE` | NUMBER | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |
| `OBSERVACION` | VARCHAR2 | YES |  |
| `USR_UNIX` | VARCHAR2 | YES |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |
| `SERVIDOR` | VARCHAR2 | YES |  |
| `DBO_COMPROBANTE` | VARCHAR2 | YES |  |
| `DBO_FACTURA` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
