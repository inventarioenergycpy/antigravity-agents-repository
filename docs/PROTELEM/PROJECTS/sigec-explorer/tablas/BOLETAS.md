---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 2182650
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "BOLETAS"
---

# 📋 BOLETAS

**Filas estimadas:** 2,182,650

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `BOL_CLASE` | VARCHAR2 | NO |  |
| `BOL_NUMERO` | NUMBER | NO | 🔑 PK |
| `URC_CODIGO_DEPOSITO` | NUMBER | NO | 🔑 PK |
| `URC_CODIGO_COBRO` | NUMBER | NO |  |
| `PAC_CODIGO` | NUMBER | NO |  |
| `BOL_FECHA_INGRESO` | DATE | NO |  |
| `BOL_FECHA_BOLETA` | DATE | YES |  |
| `BOL_FECHA_ACREDITACION` | DATE | YES |  |
| `BOL_FECHA_RENDICION` | DATE | YES |  |
| `BOL_IMPORTE` | NUMBER | YES |  |
| `BOL_NUMERO_PADRE` | NUMBER | YES |  |
| `URC_CODIGO_PADRE` | NUMBER | YES |  |
| `CPR_NUMERO` | NUMBER | NO |  |
| `ASI_NUMERO` | NUMBER | YES |  |
| `BOL_ESTADO` | VARCHAR2 | YES |  |
| `BOL_FECHA_COBRO` | DATE | YES |  |
| `BOL_FECHA_DEPOSITO` | DATE | YES |  |
| `USR_NUMERO` | NUMBER | NO |  |
| `USR_NUMERO_ASOCIA` | NUMBER | YES |  |
| `BOL_FECHA_TESORERIA` | DATE | YES |  |
| `CPR_NUMERO_INTERFACE` | NUMBER | YES |  |
| `BOL_OBSERVACIONES` | VARCHAR2 | YES |  |
| `STATEMENT_LINE_ID` | NUMBER | YES |  |
| `BOL_ULTIMA_ACTUALIZACION` | DATE | YES |  |

## FK inferidas (alta confianza)

- `BOL_CLASE` → [[VALIDACION_BOLETAS]] _BOL_CLASE es PK de VALIDACION_BOLETAS_
- `PAC_CODIGO` → [[PLAZOS_ACREDITACION]] _PAC_CODIGO es PK de PLAZOS_ACREDITACION_
