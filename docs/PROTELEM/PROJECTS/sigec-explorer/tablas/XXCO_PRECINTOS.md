---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 54883
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_PRECINTOS"
---

# 🔧 XXCO_PRECINTOS

**Filas estimadas:** 54,883

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRO_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `PRO_TIPO` | VARCHAR2 | NO |  |  |
| `PRO_NUMERO` | VARCHAR2 | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO | 🔗 → [[EQUIPOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO | 🔗 → [[EQUIPOS]] |  |
| `EQP_ORDEN` | NUMBER | NO | 🔗 → [[EQUIPOS]] |  |
| `PRO_FECHA_ALTA` | DATE | NO |  |  |
| `PRO_FECHA_BAJA` | DATE | YES |  |  |
| `ORD_NUMERO` | NUMBER | YES | 🔗 → [[ORDENATIVOS]] |  |
| `PRO_ESTADO` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **PRO_EQP_FK**: `SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN` → [[EQUIPOS]] (`SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`)
- **PRO_ORD_FK**: `ORD_NUMERO` → [[ORDENATIVOS]] (`ORD_NUMERO`)
