---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 835
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "PENALIZACIONES"
---

# 📋 PENALIZACIONES

**Filas estimadas:** 835

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[CLASES]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[CLASES]] |  |
| `PEN_BONIFICA_COS_FI` | VARCHAR2 | NO |  |  |
| `PEN_COS_FI_MAX` | NUMBER | YES |  |  |
| `TIT_CLAVE_BONIF` | VARCHAR2 | NO | 🔗 → [[TIPOS_ITEM]] |  |
| `PEN_PENALIZA_COS_FI` | VARCHAR2 | NO |  |  |
| `PEN_COS_FI_MIN` | NUMBER | YES |  |  |
| `TIT_CLAVE_PENALIZ` | VARCHAR2 | NO | 🔗 → [[TIPOS_ITEM]] |  |

## FK declaradas → otras tablas

- **PEN_FK_CLA**: `TCL_CODIGO`, `CLA_CODIGO` → [[CLASES]] (`TCL_CODIGO`, `CLA_CODIGO`)
- **PEN_FK_TIT_BONIF**: `TIT_CLAVE_BONIF` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
- **PEN_FK_TIT_PENALIZ**: `TIT_CLAVE_PENALIZ` → [[TIPOS_ITEM]] (`TIT_CLAVE`)

## Tablas que referencian esta tabla

- [[DETALLES_PENALIZACION]] via `CLA_CODIGO`, `TCL_CODIGO`
