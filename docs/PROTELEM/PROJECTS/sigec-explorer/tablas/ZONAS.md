---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 11
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ZONAS"
---

# 📋 ZONAS

**Filas estimadas:** 11

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ZON_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `ZON_DESCRIPCION` | VARCHAR2 | NO |  |
| `ZON_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[DIRECCIONES_MAIL]] via `ZON_CODIGO`
- [[SUCURSALES]] via `ZON_CODIGO`
