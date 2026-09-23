---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 310
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "DETALLES_BANDA"
---

# 📋 DETALLES_BANDA

**Filas estimadas:** 310

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `DBA_PORC_INFERIOR` | NUMBER | YES |  |  |
| `DBA_PORC_SUPERIOR` | NUMBER | YES |  |  |
| `DBA_MIN_INFERIOR` | NUMBER | YES |  |  |
