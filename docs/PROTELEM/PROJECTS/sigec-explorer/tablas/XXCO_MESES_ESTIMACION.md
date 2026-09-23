---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 1
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_MESES_ESTIMACION"
---

# 🔧 XXCO_MESES_ESTIMACION

**Filas estimadas:** 1

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `MES_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `MES_FECHA_INICIO` | DATE | NO |  |  |
| `MES_FECHA_FIN` | DATE | YES |  |  |
| `MES_OBSERVACION` | VARCHAR2 | YES |  |  |

## Tablas que referencian esta tabla

- [[XXCO_MESES_ESTIMACION_DET]] via `MES_CODIGO`
