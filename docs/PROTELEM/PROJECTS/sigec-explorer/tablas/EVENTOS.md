---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 127
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "EVENTOS"
---

# 📋 EVENTOS

**Filas estimadas:** 127

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PRC_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[PROCESOS]] |
| `EVE_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `EVE_DESCRIPCION` | VARCHAR2 | NO |  |

## FK declaradas → otras tablas

- **EVE_CORRESPONDER**: `PRC_CODIGO` → [[PROCESOS]] (`PRC_CODIGO`)

## Tablas que referencian esta tabla

- [[TRANSICIONES]] via `EVE_CODIGO`, `PRC_CODIGO`
