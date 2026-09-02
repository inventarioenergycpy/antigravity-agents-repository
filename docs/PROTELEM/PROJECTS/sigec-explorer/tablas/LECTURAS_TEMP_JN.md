---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 75167
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "LECTURAS_TEMP_JN"
---

# 📝 LECTURAS_TEMP_JN

**Filas estimadas:** 75,167

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TIPO_REGISTRO` | VARCHAR2 | YES |  |
| `ERROR_LECTURA` | VARCHAR2 | YES |  |
| `GRL_CODIGO` | VARCHAR2 | YES |  |
| `RTA_CODIGO_DESDE` | NUMBER | YES |  |
| `RTA_CODIGO_HASTA` | NUMBER | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `JN_USUARIO` | VARCHAR2 | YES |  |
| `JN_OBSERVACIONES` | VARCHAR2 | YES |  |
| `JN_PROGRAMA` | VARCHAR2 | YES |  |
| `ZONA` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
