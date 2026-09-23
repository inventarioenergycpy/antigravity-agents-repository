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
  - "CONVERSION_CAT"
---

# 📋 CONVERSION_CAT

**Filas estimadas:** 49

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CATEGORIA_ATT` | VARCHAR2 | NO | 🔑 PK |  |
| `CAT_CODIGO` | NUMBER | YES |  |  |
| `TCL_CODIGO` | NUMBER | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | NUMBER | YES |  |  |
| `TEN_CODIGO` | NUMBER | YES |  |  |
