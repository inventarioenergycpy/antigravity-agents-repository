---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 84440
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "RECLAMOS_JN"
---

# 📝 RECLAMOS_JN

**Filas estimadas:** 84,440

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RCL_NUMERO` | NUMBER | YES |  |
| `TRT_NUMERO` | NUMBER | YES |  |
| `USR_NUMERO` | VARCHAR2 | YES |  |
| `USR_RED` | VARCHAR2 | YES |  |
| `USR_ORA` | VARCHAR2 | YES |  |
| `USR_MAQUINA` | VARCHAR2 | YES |  |
| `USR_PROGRAMA` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
