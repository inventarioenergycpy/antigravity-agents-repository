---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "CONSUMOS_MINIMOS"
---

# 📋 CONSUMOS_MINIMOS

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CAT_CODIGO` | VARCHAR2 | NO |  |  |
| `CSM_CANTIDAD` | NUMBER | NO |  |  |
