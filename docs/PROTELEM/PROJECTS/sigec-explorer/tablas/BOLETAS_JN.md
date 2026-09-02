---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: documentos
num_rows: 136733
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/documentos
aliases:
  - "BOLETAS_JN"
---

# 📝 BOLETAS_JN

**Filas estimadas:** 136,733

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `BOL_CLASE` | VARCHAR2 | YES |  |
| `BOL_NUMERO` | NUMBER | YES |  |
| `URC_CODIGO_DEPOSITO` | NUMBER | YES |  |
| `URC_CODIGO_COBRO` | NUMBER | YES |  |
| `BOL_FECHA_INGRESO` | DATE | YES |  |
| `BOL_FECHA_BOLETA` | DATE | YES |  |
| `BOL_FECHA_ACREDITACION` | DATE | YES |  |
| `BOL_FECHA_DEPOSITO` | DATE | YES |  |
| `BOL_FECHA_COBRO` | DATE | YES |  |
| `URC_CODIGO_PADRE` | NUMBER | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `USR_NUMERO` | NUMBER | YES |  |
| `NRO_SESSION` | NUMBER | YES |  |
| `USR_UNIX` | VARCHAR2 | YES |  |
| `NRO_ORACLE` | NUMBER | YES |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |
| `SERVIDOR` | VARCHAR2 | YES |  |
| `TERMINAL` | VARCHAR2 | YES |  |
| `PROGRAMA` | VARCHAR2 | YES |  |
| `OPERACION` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |
| `ASI_NUMERO` | NUMBER | YES |  |
| `OBSERVACION` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `BOL_CLASE` → [[VALIDACION_BOLETAS]] _BOL_CLASE es PK de VALIDACION_BOLETAS_
