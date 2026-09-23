---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 83
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "SERVICIOS_PE"
---

# 📋 SERVICIOS_PE

**Filas estimadas:** 83

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SPE_CODIGO` | NUMBER | NO | 🔑 PK |
| `SPE_BARRIO` | VARCHAR2 | YES |  |
| `SPE_TOTAL` | NUMBER | YES |  |
| `SPE_CANTIDAD_PM` | NUMBER | YES |  |
| `SPE_CANTIDAD_CN` | NUMBER | YES |  |
| `SPE_CANTIDAD_CX` | NUMBER | YES |  |
| `SPE_REALIZADOS` | NUMBER | YES |  |
| `SPE_PORCENTAJE_OBRA` | NUMBER | YES |  |

## Tablas que referencian esta tabla

- [[SERVICIOS_PE_DETALLE]] via `SPE_CODIGO`
