---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 770
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_TARIFAS_COEFICIENTE_SEN"
---

# 🔧 XXCO_TARIFAS_COEFICIENTE_SEN

**Filas estimadas:** 770

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `TCS_COEFICIENTE` | NUMBER | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `TCS_ANIO` | NUMBER | YES |  |  |
| `TCS_PERIODO` | NUMBER | YES |  |  |
