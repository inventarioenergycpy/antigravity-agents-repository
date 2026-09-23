---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 94
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_PARAM_VALIDADOR_LECTURAS"
---

# 🔧 XXCO_PARAM_VALIDADOR_LECTURAS

**Filas estimadas:** 94

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `VLE_GCO_GRUPO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[GRUPOS_CONTRATO]] |
| `VLE_VALIDACION` | VARCHAR2 | NO | 🔑 PK |
| `VLE_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `VLE_DESCRIPCION` | VARCHAR2 | YES |  |
| `VLE_ESTADO` | VARCHAR2 | NO |  |
| `VLE_IMPRIME_DETALLE` | VARCHAR2 | YES |  |
| `VLE_VALOR` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **VLE_GCO_FK**: `VLE_GCO_GRUPO` → [[GRUPOS_CONTRATO]] (`GCO_GRUPO`)
