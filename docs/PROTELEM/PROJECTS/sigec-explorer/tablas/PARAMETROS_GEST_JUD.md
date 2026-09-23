---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 6
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PARAMETROS_GEST_JUD"
---

# 📋 PARAMETROS_GEST_JUD

**Filas estimadas:** 6

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PAR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `PAR_TIPO` | VARCHAR2 | NO |  |
| `PAR_DESCRIPCION` | VARCHAR2 | NO |  |
| `SCF_CODIGO` | VARCHAR2 | NO |  |
| `PAR_IMPORTE` | NUMBER | YES |  |
| `PAR_FECHA` | DATE | YES |  |
| `PAR_PORCENTAJE` | NUMBER | YES |  |

## Tablas que referencian esta tabla

- [[ACCIONES_PARAMETROS]] via `PAR_CODIGO`
