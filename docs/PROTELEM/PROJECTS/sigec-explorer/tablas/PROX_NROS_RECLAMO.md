---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 9
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PROX_NROS_RECLAMO"
---

# 📋 PROX_NROS_RECLAMO

**Filas estimadas:** 9

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PNR_ANIO` | NUMBER | NO | 🔑 PK |
| `PNR_PROX_NRO_RECLAMO` | NUMBER | YES |  |
| `PNR_PROX_NRO_DENUNCIA` | NUMBER | YES |  |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[SUCURSALES]] |

## FK declaradas → otras tablas

- **PNR_FK_SCF**: `SCF_CODIGO` → [[SUCURSALES]] (`SCF_CODIGO`)
