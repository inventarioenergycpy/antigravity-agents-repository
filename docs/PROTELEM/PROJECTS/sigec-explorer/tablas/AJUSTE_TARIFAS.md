---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1451
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "AJUSTE_TARIFAS"
---

# 📋 AJUSTE_TARIFAS

**Filas estimadas:** 1,451

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `TIPO_INDICE` | NUMBER | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
