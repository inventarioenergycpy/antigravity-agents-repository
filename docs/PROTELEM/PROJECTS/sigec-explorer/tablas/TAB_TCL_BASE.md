---
tipo: tabla
categoria: base
owner: XXSIGEC
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "TAB_TCL_BASE"
---

# 📋 TAB_TCL_BASE

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO_BASE` | VARCHAR2 | YES |  |  |
| `CLA_CODIGO_BASE` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO_BASE` | VARCHAR2 | YES |  |  |
| `TAB_NUMERO` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
