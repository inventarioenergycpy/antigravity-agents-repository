---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 6111
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "RUTAS_LECTURAS"
---

# 📋 RUTAS_LECTURAS

**Filas estimadas:** 6,111

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RTL_CODIGO` | NUMBER | NO | 🔑 PK |
| `RTL_DESCRIPCION` | VARCHAR2 | YES |  |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |
| `ZLE_CODIGO` | VARCHAR2 | YES |  |
| `GRL_CODIGO` | VARCHAR2 | YES | 🔗 → [[GRUPOS_LECTURA]] |
| `GCO_GRUPO` | VARCHAR2 | YES |  |
| `SEC_CODIGO` | VARCHAR2 | YES |  |
| `RTL_ESTADO` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **RTL_GRL_FK**: `GRL_CODIGO` → [[GRUPOS_LECTURA]] (`GRL_CODIGO`)

## FK inferidas (alta confianza)

- `ZLE_CODIGO` → [[ZONAS_LECTURAS]] _ZLE_CODIGO es PK de ZONAS_LECTURAS_
