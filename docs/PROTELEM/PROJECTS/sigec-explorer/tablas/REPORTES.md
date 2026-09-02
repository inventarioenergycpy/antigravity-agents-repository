---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 351
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "REPORTES"
---

# 📋 REPORTES

**Filas estimadas:** 351

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `REP_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `REP_DESCRIPCION` | VARCHAR2 | NO |  |
| `REP_PRIORIDAD` | NUMBER | NO |  |
| `REP_CONDICION_IMPRESION` | VARCHAR2 | YES |  |
| `REP_BORRA_ARCHIVO` | VARCHAR2 | YES |  |
| `REP_TIPO_COMANDO` | VARCHAR2 | NO |  |

## Tablas que referencian esta tabla

- [[CONTROL_REPORTES]] via `REP_CODIGO`
