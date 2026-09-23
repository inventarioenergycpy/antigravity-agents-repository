---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 792
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "DETALLES_PENALIZACION"
---

# 📋 DETALLES_PENALIZACION

**Filas estimadas:** 792

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[PENALIZACIONES]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[PENALIZACIONES]] |  |
| `CDR_UNIDAD` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TIPOS_CUADRANTE]] |  |
| `DPE_PORCENTAJE_DESDE` | NUMBER | NO | 🔑 PK |  |
| `DPE_PORCENTAJE_HASTA` | NUMBER | YES |  |  |
| `DPE_PERIODOS` | NUMBER | YES |  |  |
| `DPE_COBRA_EXCESO` | VARCHAR2 | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | NO | 🔗 → [[TIPOS_ITEM]] |  |
| `DPE_TIPO_PENALIZACION` | VARCHAR2 | YES |  |  |
| `DPE_CONSUMO_DESDE` | NUMBER | YES |  |  |
| `DPE_CONSUMO_HASTA` | NUMBER | YES |  |  |
| `TFA_CODIGO` | VARCHAR2 | YES |  |  |
| `DPE_PORC_CONSUMO_ANTERIOR` | NUMBER | YES |  |  |
| `DPE_PORC_PRECIO_ESCALON` | NUMBER | YES |  |  |
| `CDR_UNIDAD_AUX` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **DPE_FK_PEN**: `TCL_CODIGO`, `CLA_CODIGO` → [[PENALIZACIONES]] (`TCL_CODIGO`, `CLA_CODIGO`)
- **DPE_FK_TCU**: `CDR_UNIDAD` → [[TIPOS_CUADRANTE]] (`CDR_UNIDAD`)
- **DPE_FK_TIT**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
