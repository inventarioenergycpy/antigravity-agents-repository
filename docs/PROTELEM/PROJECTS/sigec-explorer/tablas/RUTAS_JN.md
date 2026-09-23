---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 11644
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "RUTAS_JN"
---

# 📝 RUTAS_JN

**Filas estimadas:** 11,644

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RTA_CODIGO` | NUMBER | YES |  |
| `SCF_CODIGO` | NUMBER | YES |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |
| `RTA_GRUPO` | VARCHAR2 | YES |  |
| `GRL_CODIGO_SUGERIDO` | VARCHAR2 | YES |  |
| `COD_MOVIM` | VARCHAR2 | YES |  |
| `JN_USER` | NUMBER | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `OBSERVA` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
