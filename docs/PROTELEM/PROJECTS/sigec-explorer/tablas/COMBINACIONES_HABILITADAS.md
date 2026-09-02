---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1174
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "COMBINACIONES_HABILITADAS"
---

# 📋 COMBINACIONES_HABILITADAS

**Filas estimadas:** 1,174

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CLA_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[CLASES]] |  |
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[CLASES]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `TEN_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TENSIONES]] |  |
| `CHB_ESTADO` | VARCHAR2 | YES |  |  |
| `MSF_NUMERO` | NUMBER | YES |  |  |
| `CHB_EXC_DEMANDA_FLAG` | VARCHAR2 | YES |  |  |
| `CHB_ESTADO_FACTURACION` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **CHB_FK_CLA**: `TCL_CODIGO`, `CLA_CODIGO` → [[CLASES]] (`TCL_CODIGO`, `CLA_CODIGO`)
- **CHB_FK_TEN**: `TEN_CODIGO` → [[TENSIONES]] (`TEN_CODIGO`)
