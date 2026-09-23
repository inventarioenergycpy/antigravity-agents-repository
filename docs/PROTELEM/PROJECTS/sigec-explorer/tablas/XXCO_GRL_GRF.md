---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 2138
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_GRL_GRF"
---

# 🔧 XXCO_GRL_GRF

**Filas estimadas:** 2,138

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[GRUPOS_LECTURA]] |
| `GRF_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[GRUPOS_FACTURACION]] |
| `GRF_DEFAULT` | VARCHAR2 | YES |  |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |
| `ZON_CODIGO` | VARCHAR2 | NO |  |

## FK declaradas → otras tablas

- **XXCO_GRL_GRF_FK_GRF**: `GRF_CODIGO` → [[GRUPOS_FACTURACION]] (`GRF_CODIGO`)
- **XXCO_GRL_GRF_FK_GRL**: `GRL_CODIGO` → [[GRUPOS_LECTURA]] (`GRL_CODIGO`)

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
