---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 5902
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "XX_PROCESOS_COLECTORAS_JN"
---

# 📝 XX_PROCESOS_COLECTORAS_JN

**Filas estimadas:** 5,902

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PCL_NUMERO` | NUMBER | YES |  |
| `JN_USUARIO` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `EPC_CODIGO_ANT` | VARCHAR2 | YES |  |
| `EPC_CODIGO_POS` | VARCHAR2 | YES |  |
| `PCL_OBSERVACIONES` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
