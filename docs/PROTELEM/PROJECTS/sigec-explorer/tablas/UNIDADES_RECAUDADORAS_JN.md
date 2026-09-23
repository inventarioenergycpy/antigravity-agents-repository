---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 1822
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "UNIDADES_RECAUDADORAS_JN"
---

# 📝 UNIDADES_RECAUDADORAS_JN

**Filas estimadas:** 1,822

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `URC_CODIGO` | NUMBER | YES |  |
| `URC_DESCRIPCION` | VARCHAR2 | YES |  |
| `URC_TIPO` | VARCHAR2 | YES |  |
| `URC_GRUPO` | VARCHAR2 | YES |  |
| `URC_CODIGO_MADRE` | NUMBER | YES |  |
| `URC_TIPO_LOTE` | VARCHAR2 | YES |  |
| `URC_MONEDA` | VARCHAR2 | YES |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `OBSERVACION` | VARCHAR2 | YES |  |
| `URC_CUIT` | NUMBER | YES |  |
| `URC_RAZON_SOCIAL` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
