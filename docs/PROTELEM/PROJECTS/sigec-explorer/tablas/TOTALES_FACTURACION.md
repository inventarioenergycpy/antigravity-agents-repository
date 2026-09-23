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
  - "TOTALES_FACTURACION"
---

# 📋 TOTALES_FACTURACION

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TTF_ANIO` | NUMBER | NO | 🔑 PK |  |
| `TTF_PERIODO` | NUMBER | NO | 🔑 PK |  |
| `CAT_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `TEN_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `TTF_DEMANDA` | NUMBER | YES |  |  |
| `TTF_ENERGIA` | NUMBER | YES |  |  |
| `TTF_I_IMPUESTOS` | NUMBER | YES |  |  |
| `TTF_I_TOTAL` | NUMBER | YES |  |  |
| `TTF_I_BASICO` | NUMBER | YES |  |  |
