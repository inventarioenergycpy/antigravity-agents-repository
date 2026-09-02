---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: equipos
num_rows: 14
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/equipos
aliases:
  - "ACCIONES_TIPO"
---

# 📋 ACCIONES_TIPO

**Filas estimadas:** 14

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ACT_CODIGO` | NUMBER | NO | 🔑 PK |
| `ACT_ORDEN` | NUMBER | YES |  |
| `ACT_DESCRIPCION` | VARCHAR2 | NO |  |
| `ETS_CODIGO` | NUMBER | YES | 🔗 → [[ETAPAS]] |

## FK declaradas → otras tablas

- **ACT_ETS_FK**: `ETS_CODIGO` → [[ETAPAS]] (`ETS_CODIGO`)

## FK inferidas (alta confianza)

- `ETS_CODIGO` → [[ETAPAS]] _ETS_CODIGO es PK de ETAPAS_
