---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "USUARIOS_JN"
---

# 📝 USUARIOS_JN

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `USR_NUMERO` | NUMBER | YES |  |
| `USR_CODIGO` | VARCHAR2 | YES |  |
| `SEC_CODIGO` | VARCHAR2 | YES |  |
| `SCF_CODIGO` | NUMBER | YES |  |
| `PRT_CODIGO` | VARCHAR2 | YES |  |
| `PRT_CODIGO_2` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |
| `OBSERVA` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `PRT_CODIGO` → [[IMPRESORAS]] _PRT_CODIGO es PK de IMPRESORAS_
