---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 113
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "RUTAS_LECTURAS_JN"
---

# 📝 RUTAS_LECTURAS_JN

**Filas estimadas:** 113

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RTL_CODIGO` | NUMBER | YES |  |
| `RTL_DESCRIPCION` | VARCHAR2 | YES |  |
| `SCF_CODIGO` | NUMBER | YES |  |
| `ZLE_CODIGO` | VARCHAR2 | YES |  |
| `GRL_CODIGO` | VARCHAR2 | YES |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |
| `SEC_CODIGO` | VARCHAR2 | YES |  |
| `JN_TIPO_OPERACION` | VARCHAR2 | YES |  |
| `JN_USER` | NUMBER | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `OBSERVA` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `ZLE_CODIGO` → [[ZONAS_LECTURAS]] _ZLE_CODIGO es PK de ZONAS_LECTURAS_
