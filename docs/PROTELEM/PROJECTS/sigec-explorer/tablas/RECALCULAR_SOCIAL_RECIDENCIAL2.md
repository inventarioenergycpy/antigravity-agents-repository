---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 49
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "RECALCULAR_SOCIAL_RECIDENCIAL2"
---

# 📋 RECALCULAR_SOCIAL_RECIDENCIAL2

**Filas estimadas:** 49

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `TAB_NUMERO` | NUMBER | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | NO |  |  |
| `ITM_CANTIDAD` | NUMBER | YES |  |  |
| `ITM_PRECIO_UNIT` | NUMBER | YES |  |  |
| `ITM_IMPORTE` | NUMBER | NO |  |  |
| `TAB_CONSUMO_LIMITE` | NUMBER | YES |  |  |
| `TAB_FECHA_VIGENCIA` | DATE | NO |  |  |
| `TAB_190` | NUMBER | YES |  |  |
