---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 118437
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_CONCEPTOS_CONFECCIONES"
---

# 🔧 XXCO_CONCEPTOS_CONFECCIONES

**Filas estimadas:** 118,437

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PCC_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_TARIFAS_BASE_CONFECCIONES]] |  |
| `TCL_CODIGO_BASE` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_TARIFAS_BASE_CONFECCIONES]] |  |
| `CCR_CLASES` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_TARIFAS_BASE_CONFECCIONES]] |  |
| `CCR_TENSIONES` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_TARIFAS_BASE_CONFECCIONES]] |  |
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CON_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `ESC_NUMERO` | VARCHAR2 | NO | 🔑 PK |  |
| `CCR_PRECIO_SIN_SUBSIDIO` | NUMBER | YES |  |  |
| `CCR_PRECIO_CON_SUBSIDIO` | NUMBER | YES |  |  |
| `CCR_CANTIDAD` | NUMBER | YES |  |  |
| `TCL_CONSUMO_DESDE` | NUMBER | YES |  |  |
| `TCL_CONSUMO_HASTA` | NUMBER | YES |  |  |
| `ESC_CANTIDAD_DESDE` | NUMBER | YES |  |  |
| `ESC_CANTIDAD_HASTA` | NUMBER | YES |  |  |
| `TCL_CODIGO_ALT` | VARCHAR2 | YES |  |  |
| `TCU_GRUPO_ALT` | VARCHAR2 | YES |  |  |
| `CCR_PRECIO_CON_SUBSIDIO_2` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **XXCO_TBC_CCR_FK**: `PCC_NUMERO`, `TCL_CODIGO_BASE`, `CCR_CLASES`, `CCR_TENSIONES` → [[XXCO_TARIFAS_BASE_CONFECCIONES]] (`PCC_NUMERO`, `TCL_CODIGO_BASE`, `CLA_CODIGOS`, `TEN_CODIGOS`)
