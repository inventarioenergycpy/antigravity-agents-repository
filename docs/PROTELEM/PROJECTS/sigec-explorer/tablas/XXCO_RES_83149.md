---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 1621
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_RES_83149"
---

# 🔧 XXCO_RES_83149

**Filas estimadas:** 1,621

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ID_REPORTE` | NUMBER | YES |  |
| `ANIO` | NUMBER | YES |  |
| `PERIODO` | NUMBER | YES |  |
| `FECHA` | DATE | YES |  |
| `USR_NUMERO` | NUMBER | YES |  |
| `ESTADO` | VARCHAR2 | YES |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |
| `FECHA_CIERRE` | DATE | YES |  |
| `USR_NUMERO_CIERRE` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
- `ID_REPORTE` → [[XXCO_RES_83149_DET]] _ID_REPORTE es PK de XXCO_RES_83149_DET_
