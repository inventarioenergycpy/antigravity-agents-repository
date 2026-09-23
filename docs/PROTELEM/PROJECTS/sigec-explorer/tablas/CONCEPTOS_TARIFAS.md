---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 6592
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "CONCEPTOS_TARIFAS"
---

# 📋 CONCEPTOS_TARIFAS

**Filas estimadas:** 6,592

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TARIFAS]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CON_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `CON_FECHA_VIGENCIA` | DATE | NO | 🔑 PK |  |
| `CON_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `CON_TIPO` | VARCHAR2 | NO |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES | 🔗 → [[TIPOS_CUADRANTE]] |  |
| `CON_ESCALON` | VARCHAR2 | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | YES | 🔗 → [[TIPOS_ITEM]] |  |
| `CON_POR_DIA` | VARCHAR2 | YES |  |  |
| `CON_EMISION_VIGENCIA_DESDE` | DATE | YES |  |  |
| `CON_EMISION_VIGENCIA_HASTA` | DATE | YES |  |  |

## FK declaradas → otras tablas

- **CON_FK_TCL**: `TCL_CODIGO` → [[TARIFAS]] (`TCL_CODIGO`)
- **CON_FK_TCU**: `CDR_UNIDAD` → [[TIPOS_CUADRANTE]] (`CDR_UNIDAD`)
- **CON_FK_TIT**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)

## Tablas que referencian esta tabla

- [[ESCALONES]] via `CON_FECHA_VIGENCIA`, `CON_NUMERO`, `TCL_CODIGO`
