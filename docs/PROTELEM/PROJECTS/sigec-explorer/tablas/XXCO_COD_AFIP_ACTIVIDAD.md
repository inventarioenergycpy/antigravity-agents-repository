---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 973
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_COD_AFIP_ACTIVIDAD"
---

# 🔧 XXCO_COD_AFIP_ACTIVIDAD

**Filas estimadas:** 973

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CAA_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `CAA_DENOMINACION` | VARCHAR2 | YES |  |
| `CAA_GRUPO` | VARCHAR2 | NO | 🔑 PK |
| `GAA_CODIGO` | VARCHAR2 | YES | 🔗 → [[XXCO_GRUPOS_AFIP_ACTIVIDAD]] |
| `CAA_CODIGO_PADRE` | VARCHAR2 | YES |  |
| `CAA_SUBSIDIADA` | VARCHAR2 | YES |  |
| `CAA_FECHA_RETIRO_SUIBSIDIO` | DATE | YES |  |

## FK declaradas → otras tablas

- **XXCO_CAA_GAA**: `GAA_CODIGO` → [[XXCO_GRUPOS_AFIP_ACTIVIDAD]] (`GAA_CODIGO`)

## FK inferidas (alta confianza)

- `GAA_CODIGO` → [[XXCO_GRUPOS_AFIP_ACTIVIDAD]] _GAA_CODIGO es PK de XXCO_GRUPOS_AFIP_ACTIVIDAD_
