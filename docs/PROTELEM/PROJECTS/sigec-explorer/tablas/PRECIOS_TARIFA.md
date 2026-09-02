---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 69890
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "PRECIOS_TARIFA"
---

# 📋 PRECIOS_TARIFA

**Filas estimadas:** 69,890

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TAB_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `TCL_CODIGO` | VARCHAR2 | NO | 🔗 → [[CLASES]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO | 🔗 → [[CLASES]] |  |
| `TEN_CODIGO` | VARCHAR2 | NO | 🔗 → [[TENSIONES]] |  |
| `TAB_FECHA_VIGENCIA` | DATE | NO |  |  |
| `TAB_FECHA_CARGA` | DATE | NO |  |  |
| `TAB_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `TAB_ESTADO` | VARCHAR2 | NO |  |  |
| `TAB_CONSUMO_LIMITE` | NUMBER | YES |  |  |
| `TCL_CODIGO_ALT` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO_ALT` | VARCHAR2 | YES |  |  |
| `CLA_CODIGO_ALT` | VARCHAR2 | YES |  |  |
| `TCU_GRUPO_ALT` | VARCHAR2 | YES |  |  |
| `TAB_CON_SUBSIDIO` | VARCHAR2 | YES |  |  |
| `TAB_COSTO_MEM` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **TAB_FK_CLA**: `TCL_CODIGO`, `CLA_CODIGO` → [[CLASES]] (`TCL_CODIGO`, `CLA_CODIGO`)
- **TAB_FK_TEN**: `TEN_CODIGO` → [[TENSIONES]] (`TEN_CODIGO`)

## Tablas que referencian esta tabla

- [[DETALLES_LISTA]] via `TAB_NUMERO`
