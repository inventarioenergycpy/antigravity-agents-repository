---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 5
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "PRECIOS_CONTRIB_REEMBOL"
---

# 📋 PRECIOS_CONTRIB_REEMBOL

**Filas estimadas:** 5

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PCR_FECHA_VIGENCIA` | DATE | NO | 🔑 PK |  |
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[CLASES]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[CLASES]] |  |
| `TEN_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TENSIONES]] |  |
| `PCR_PRECIO_CONSTANTE` | NUMBER | YES |  |  |
| `PCR_PRECIO_POR_DEMANDA` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **PCR_FK_CLA**: `TCL_CODIGO`, `CLA_CODIGO` → [[CLASES]] (`TCL_CODIGO`, `CLA_CODIGO`)
- **PCR_FK_TEN**: `TEN_CODIGO` → [[TENSIONES]] (`TEN_CODIGO`)
