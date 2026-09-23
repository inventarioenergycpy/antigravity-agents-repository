---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 277
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "XX_TARIFAS_GRUPOS"
---

# 📋 XX_TARIFAS_GRUPOS

**Filas estimadas:** 277

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `GRF_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XX_GRUPOS_CALIFICACIONES]] |  |
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TARIFAS]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[CLASES]] |  |
| `TRG_FECHA_DESDE` | DATE | NO |  |  |
| `TRG_FECHA_HASTA` | DATE | YES |  |  |

## FK declaradas → otras tablas

- **TRG_CLA_FK**: `TCL_CODIGO`, `CLA_CODIGO` → [[CLASES]] (`TCL_CODIGO`, `CLA_CODIGO`)
- **TRG_GRF_FK**: `GRF_CODIGO` → [[XX_GRUPOS_CALIFICACIONES]] (`GRF_CODIGO`)
- **TRG_TAR_FK**: `TCL_CODIGO` → [[TARIFAS]] (`TCL_CODIGO`)
