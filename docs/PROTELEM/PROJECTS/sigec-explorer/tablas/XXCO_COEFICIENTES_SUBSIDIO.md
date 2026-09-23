---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 2368
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_COEFICIENTES_SUBSIDIO"
---

# 🔧 XXCO_COEFICIENTES_SUBSIDIO

**Filas estimadas:** 2,368

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `CON_NUMERO` | NUMBER | YES |  |  |
| `ESC_NUMERO` | NUMBER | YES |  |  |
| `FECHA_VIGENCIA_SIN_SUBSIDIO` | DATE | NO |  |  |
| `TAB_NUMERO_SIN_SUBSIDIO` | NUMBER | NO |  |  |
| `PRECIO_UNIT_SIN_SUBSIDIO` | NUMBER | NO |  |  |
| `FECHA_VIGENCIA_CON_SUBSIDIO` | DATE | NO |  |  |
| `TAB_NUMERO_CON_SUBSIDIO` | NUMBER | NO |  |  |
| `PRECIO_UNIT_CON_SUBSIDIO` | NUMBER | NO |  |  |
