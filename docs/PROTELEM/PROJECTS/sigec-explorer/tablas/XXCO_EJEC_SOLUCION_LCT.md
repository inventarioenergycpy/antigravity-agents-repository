---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 623
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_EJEC_SOLUCION_LCT"
---

# 🔧 XXCO_EJEC_SOLUCION_LCT

**Filas estimadas:** 623

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `VAL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_SOLUCIONES_ERRORES_LCT]] |
| `SEL_SECUENCIA` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_SOLUCIONES_ERRORES_LCT]] |
| `ESEL_SECUENCIA` | NUMBER | NO | 🔑 PK |
| `ESEL_TIPO_EJECUCION` | VARCHAR2 | YES |  |
| `ESEL_EJECUCION` | VARCHAR2 | YES |  |
| `ESEL_PARAMETROS` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **ESEL_SEL_FK**: `VAL_CODIGO`, `SEL_SECUENCIA` → [[XXCO_SOLUCIONES_ERRORES_LCT]] (`VAL_CODIGO`, `SEL_SECUENCIA`)
