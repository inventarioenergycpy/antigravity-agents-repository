---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1440
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "CUADRANTES_TARIFA"
---

# 📋 CUADRANTES_TARIFA

**Filas estimadas:** 1,440

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TARIFAS]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CDR_UNIDAD` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TIPOS_CUADRANTE]] |  |
| `CXT_ORDEN` | NUMBER | NO |  |  |
| `SCF_CODIGO_HABILITADOS` | VARCHAR2 | YES |  |  |
| `CLA_CODIGO_HABILITADOS` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **CXT_FK_TCL**: `TCL_CODIGO` → [[TARIFAS]] (`TCL_CODIGO`)
- **CXT_FK_TCU**: `CDR_UNIDAD` → [[TIPOS_CUADRANTE]] (`CDR_UNIDAD`)
