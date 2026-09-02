---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 549023
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
aliases:
  - "VKO_DETALLE_MORA"
---

# 📋 VKO_DETALLE_MORA

**Filas estimadas:** 549,023

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CAP_NRO_PLAN` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[VKO_DETALLE_DEUDA]] |
| `DOC_TIPO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[VKO_DETALLE_DEUDA]] |
| `DOC_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[VKO_DETALLE_DEUDA]] |
| `DEM_CONCEPTO` | VARCHAR2 | NO | 🔑 PK |
| `DEM_IMPORTE` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **DEM_DED_FK**: `CAP_NRO_PLAN`, `DOC_TIPO`, `DOC_NUMERO` → [[VKO_DETALLE_DEUDA]] (`CAP_NRO_PLAN`, `DOC_TIPO`, `DOC_NUMERO`)
