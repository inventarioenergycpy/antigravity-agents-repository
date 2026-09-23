---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1749
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "RANGO_POTENCIAS"
---

# 📋 RANGO_POTENCIAS

**Filas estimadas:** 1,749

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[CLASES]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[CLASES]] |  |
| `CDR_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TIPOS_CUADRANTE]] |  |
| `RPT_MINIMO` | NUMBER | YES |  |  |
| `RPT_MAXIMO` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **RPT_FK_CLA**: `TCL_CODIGO`, `CLA_CODIGO` → [[CLASES]] (`TCL_CODIGO`, `CLA_CODIGO`)
- **RPT_FK_TCU**: `CDR_CODIGO` → [[TIPOS_CUADRANTE]] (`CDR_UNIDAD`)
