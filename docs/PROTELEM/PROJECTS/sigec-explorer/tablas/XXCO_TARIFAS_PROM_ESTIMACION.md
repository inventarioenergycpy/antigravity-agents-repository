---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 112
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_TARIFAS_PROM_ESTIMACION"
---

# 🔧 XXCO_TARIFAS_PROM_ESTIMACION

**Filas estimadas:** 112

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ANIO` | NUMBER | YES |  |  |
| `PERIODO` | NUMBER | YES |  |  |
| `TCL_CODIGO` | NUMBER | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | NUMBER | YES |  |  |
| `TEN_CODIGO` | NUMBER | YES |  |  |
| `CONS_PROMERDIO` | NUMBER | YES |  |  |
