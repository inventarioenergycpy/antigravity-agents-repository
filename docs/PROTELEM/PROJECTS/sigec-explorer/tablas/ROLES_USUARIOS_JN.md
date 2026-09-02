---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 6092
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "ROLES_USUARIOS_JN"
---

# 📝 ROLES_USUARIOS_JN

**Filas estimadas:** 6,092

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `JN_NUMERO` | NUMBER | NO | 🔑 PK |
| `USR_CODIGO` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `ROL_CODIGO` | VARCHAR2 | NO |  |
| `USR_NUMERO` | NUMBER | YES |  |
| `JN_OPERACION` | VARCHAR2 | NO |  |
| `JN_VALOR_OLD` | VARCHAR2 | YES |  |
| `JN_VALOR_NEW` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
