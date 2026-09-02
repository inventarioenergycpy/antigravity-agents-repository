---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 281
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "CUADRANTES_TARIFA_DET"
---

# 📋 CUADRANTES_TARIFA_DET

**Filas estimadas:** 281

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TARIFAS]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CDR_UNIDAD` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TIPOS_CUADRANTE]] |  |
| `CTD_ORDEN` | NUMBER | NO |  |  |

## FK declaradas → otras tablas

- **CTD_FK_TCL**: `TCL_CODIGO` → [[TARIFAS]] (`TCL_CODIGO`)
- **CTD_FK_TCU**: `CDR_UNIDAD` → [[TIPOS_CUADRANTE]] (`CDR_UNIDAD`)
