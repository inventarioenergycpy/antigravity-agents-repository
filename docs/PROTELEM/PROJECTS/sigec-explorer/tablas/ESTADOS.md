---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 196
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ESTADOS"
---

# 📋 ESTADOS

**Filas estimadas:** 196

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PRC_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[PROCESOS]] |
| `EST_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `EST_DESCRIPCION` | VARCHAR2 | NO |  |
| `EST_ESTADO_INICIAL` | VARCHAR2 | YES |  |
| `EST_FACTURABLE` | VARCHAR2 | YES |  |
| `EST_ATRIBUTO1` | VARCHAR2 | YES |  |
| `EST_ATRIBUTO2` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **EST_CORRESPONDER**: `PRC_CODIGO` → [[PROCESOS]] (`PRC_CODIGO`)

## Tablas que referencian esta tabla

- [[TRANSICIONES]] via `EST_CODIGO`, `PRC_CODIGO`, `TRA_PROXIMO_ESTADO`
