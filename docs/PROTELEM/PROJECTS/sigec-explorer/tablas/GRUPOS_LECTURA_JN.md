---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 248
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "GRUPOS_LECTURA_JN"
---

# 📝 GRUPOS_LECTURA_JN

**Filas estimadas:** 248

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRL_CODIGO` | VARCHAR2 | YES |  |
| `GRL_FRECUENCIA` | NUMBER | YES |  |
| `SEC_CODIGO` | VARCHAR2 | YES |  |
| `TFR_CODIGO` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |
| `OBSERVA` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `TFR_CODIGO` → [[XXCO_TIPOS_FRECUENCIA]] _TFR_CODIGO es PK de XXCO_TIPOS_FRECUENCIA_
