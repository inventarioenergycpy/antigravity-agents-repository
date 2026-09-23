---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 474570
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_LOTE_ORDENATIVOS_MOV"
---

# 🔧 XXCO_LOTE_ORDENATIVOS_MOV

**Filas estimadas:** 474,570

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `LOR_NUMERO` | NUMBER | NO | 🔑 PK |
| `LOR_DENOMINACION` | VARCHAR2 | NO |  |
| `LOR_FECHA` | DATE | NO |  |
| `USR_NUMERO_ASIGNADO` | NUMBER | YES |  |
| `SIN_NUMERO` | NUMBER | YES |  |
| `USR_NUMERO` | NUMBER | NO |  |
| `SCF_CODIGO` | NUMBER | NO |  |
| `LOR_FECHA_CREACION` | DATE | NO |  |
| `SEC_CODIGO` | VARCHAR2 | NO |  |
| `USR_NUMERO_ASIGNA` | NUMBER | YES |  |
| `LOR_FECHA_ASIGNACION` | DATE | YES |  |
| `APP_ID` | NUMBER | YES |  |
| `SIN_DIRECCION` | VARCHAR2 | YES |  |
| `LOF_NUMERO` | NUMBER | YES |  |
| `LOF_FECHA` | DATE | YES |  |
| `MDM_PLANNED_START_DATE` | DATE | YES |  |
| `MDM_PLANNED_END_DATE` | DATE | YES |  |

## FK inferidas (alta confianza)

- `APP_ID` → [[XXCO_OBSERVACIONES_ORDENATIVO]] _APP_ID es PK de XXCO_OBSERVACIONES_ORDENATIVO_
- `SIN_NUMERO` → [[XXCO_OBSERVACIONES_ORDENATIVO]] _SIN_NUMERO es PK de XXCO_OBSERVACIONES_ORDENATIVO_
- `LOF_NUMERO` → [[XXCO_LOTES_ORD_FILTROS]] _LOF_NUMERO es PK de XXCO_LOTES_ORD_FILTROS_
