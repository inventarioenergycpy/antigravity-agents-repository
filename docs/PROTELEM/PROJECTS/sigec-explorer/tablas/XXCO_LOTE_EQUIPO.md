---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 53580
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_LOTE_EQUIPO"
---

# 🔧 XXCO_LOTE_EQUIPO

**Filas estimadas:** 53,580

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `LEQ_NUMERO` | NUMBER | NO | 🔑 PK |
| `LEQ_DESCRIPCION` | VARCHAR2 | YES |  |
| `LEQ_FECHA_CREACION` | DATE | NO |  |
| `LEQ_FECHA_ASIGNACION` | DATE | YES |  |
| `USR_NUMERO_CREACION` | NUMBER | NO | 🔗 → [[USUARIOS]] |
| `USR_NUMERO_ASIGNACION` | NUMBER | YES |  |
| `SEC_CODIGO_CREACION` | VARCHAR2 | NO | 🔗 → [[SECTORES]] |
| `SEC_CODIGO_ASIGNADO` | VARCHAR2 | NO | 🔗 → [[SECTORES]] |
| `SCF_CODIGO_CREACION` | NUMBER | NO | 🔗 → [[SUCURSALES]] |
| `SCF_CODIGO_ASIGNACION` | NUMBER | NO | 🔗 → [[SUCURSALES]] |
| `USR_NUMERO_RECEPCION` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **SYS_C00157573**: `USR_NUMERO_CREACION` → [[USUARIOS]] (`USR_NUMERO`)
- **SYS_C00157574**: `SEC_CODIGO_CREACION` → [[SECTORES]] (`SEC_CODIGO`)
- **SYS_C00157575**: `SEC_CODIGO_ASIGNADO` → [[SECTORES]] (`SEC_CODIGO`)
- **XXCO_LOTE_EQUIPO_FK**: `SCF_CODIGO_CREACION` → [[SUCURSALES]] (`SCF_CODIGO`)
- **XXCO_LOTE_EQUIPO_FK2**: `SCF_CODIGO_ASIGNACION` → [[SUCURSALES]] (`SCF_CODIGO`)
