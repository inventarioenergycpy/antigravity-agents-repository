---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 220
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ARO_PARAM_ADICIONALES"
---

# 📋 ARO_PARAM_ADICIONALES

**Filas estimadas:** 220

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SEC_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[ACCIONES_RESULTADOS_ORDENATIVO]] |
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[ACCIONES_RESULTADOS_ORDENATIVO]] |
| `ARO_ORDEN` | NUMBER | NO | 🔑 PK · 🔗 → [[ACCIONES_RESULTADOS_ORDENATIVO]] |
| `ROD_RESULTADO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[ACCIONES_RESULTADOS_ORDENATIVO]] |
| `APE_PARAMETRO` | VARCHAR2 | NO | 🔑 PK |
| `APE_VALOR` | VARCHAR2 | NO |  |

## FK declaradas → otras tablas

- **APE_ARO_FK**: `TOR_CODIGO`, `SEC_CODIGO`, `ROD_RESULTADO`, `ARO_ORDEN` → [[ACCIONES_RESULTADOS_ORDENATIVO]] (`TOR_CODIGO`, `SEC_CODIGO`, `ROD_RESULTADO`, `ARO_ORDEN`)
