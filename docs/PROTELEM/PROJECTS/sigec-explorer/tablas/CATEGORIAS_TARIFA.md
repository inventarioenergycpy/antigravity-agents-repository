---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 249
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "CATEGORIAS_TARIFA"
---

# 📋 CATEGORIAS_TARIFA

**Filas estimadas:** 249

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CAT_CODIGO` | VARCHAR2 | NO |  |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
