---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 4008
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "ESCALONES"
---

# 📋 ESCALONES

**Filas estimadas:** 4,008

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[CONCEPTOS_TARIFAS]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CON_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[CONCEPTOS_TARIFAS]] |  |
| `CON_FECHA_VIGENCIA` | DATE | NO | 🔑 PK · 🔗 → [[CONCEPTOS_TARIFAS]] |  |
| `ESC_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `ESC_CANTIDAD_DESDE` | NUMBER | NO |  |  |
| `ESC_CANTIDAD_HASTA` | NUMBER | NO |  |  |
| `ESC_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | YES | 🔗 → [[TIPOS_ITEM]] |  |

## FK declaradas → otras tablas

- **ESC_FK_CON**: `CON_FECHA_VIGENCIA`, `CON_NUMERO`, `TCL_CODIGO` → [[CONCEPTOS_TARIFAS]] (`CON_FECHA_VIGENCIA`, `CON_NUMERO`, `TCL_CODIGO`)
- **ESC_FK_TIT**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
