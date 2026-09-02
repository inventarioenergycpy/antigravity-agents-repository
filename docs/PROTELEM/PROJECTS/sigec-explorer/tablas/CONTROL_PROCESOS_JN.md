---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: servicios
num_rows: 22332
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/servicios
aliases:
  - "CONTROL_PROCESOS_JN"
---

# 📝 CONTROL_PROCESOS_JN

**Filas estimadas:** 22,332

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CPR_NUMERO` | NUMBER | YES |  |
| `CPR_TIPO_PROCESO` | VARCHAR2 | YES |  |
| `CPR_FECHA_INICIO` | DATE | YES |  |
| `URC_CODIGO` | NUMBER | YES |  |
| `CPR_NUMERO_PADRE` | NUMBER | YES |  |
| `CPR_CANT_REG` | NUMBER | YES |  |
| `CPR_IMPORTE` | NUMBER | YES |  |
| `CPR_OBSERVACIONES` | VARCHAR2 | YES |  |
| `PRC_CODIGO` | VARCHAR2 | YES |  |
| `SCF_CODIGO` | NUMBER | YES |  |
| `NRO_SESSION` | NUMBER | YES |  |
| `USR_UNIX` | VARCHAR2 | YES |  |
| `NRO_ORACLE` | NUMBER | YES |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |
| `SERVIDOR` | VARCHAR2 | YES |  |
| `TERMINAL` | VARCHAR2 | YES |  |
| `PROGRAMA` | VARCHAR2 | YES |  |
| `OPERACION` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
