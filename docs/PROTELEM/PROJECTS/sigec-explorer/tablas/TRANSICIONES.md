---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 385
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "TRANSICIONES"
---

# 📋 TRANSICIONES

**Filas estimadas:** 385

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PRC_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[PROCESOS]] |
| `EST_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[ESTADOS]] |
| `EVE_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[EVENTOS]] |
| `TRA_PROXIMO_ESTADO` | VARCHAR2 | YES | 🔗 → [[ESTADOS]] |

## FK declaradas → otras tablas

- **TRA_CORRESPONDER**: `PRC_CODIGO`, `EVE_CODIGO` → [[EVENTOS]] (`PRC_CODIGO`, `EVE_CODIGO`)
- **TRA_CORRESPONDER_A**: `PRC_CODIGO`, `EST_CODIGO` → [[ESTADOS]] (`PRC_CODIGO`, `EST_CODIGO`)
- **TRA_PERTENECER**: `PRC_CODIGO`, `TRA_PROXIMO_ESTADO` → [[ESTADOS]] (`PRC_CODIGO`, `EST_CODIGO`)
- **TRA_PERTENECER_A**: `PRC_CODIGO` → [[PROCESOS]] (`PRC_CODIGO`)
