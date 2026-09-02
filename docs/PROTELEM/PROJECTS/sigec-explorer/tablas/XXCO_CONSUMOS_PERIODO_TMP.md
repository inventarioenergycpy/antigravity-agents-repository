---
tipo: tabla
categoria: temp
owner: XXSIGEC
num_rows: 36
tags:
  - sigec-explorer
  - tabla
  - temp
  - documentada/negocio
aliases:
  - "XXCO_CONSUMOS_PERIODO_TMP"
---

# ⏱️ XXCO_CONSUMOS_PERIODO_TMP

**Filas estimadas:** 36

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CONSUMO` | NUMBER | YES |  |  |
| `ANIO` | NUMBER | YES |  |  |
| `PERIODO` | NUMBER | YES |  |  |
| `PROMEDIO` | NUMBER | YES |  |  |
