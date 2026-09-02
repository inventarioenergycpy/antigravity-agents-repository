---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 65
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_VALORES_PARAMETROS"
---

# 📋 XX_VALORES_PARAMETROS

**Filas estimadas:** 65

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `VPA_VALOR_SIGEC` | VARCHAR2 | NO | 🔑 PK |
| `VPA_VALOR_COLECTORA` | VARCHAR2 | NO | 🔑 PK |
| `VPA_DESCRIPCION_SIGEC` | VARCHAR2 | NO |  |
| `ICO_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[XX_PARAMETROS_COLECTORAS]] |
| `PCO_NOMBRE` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XX_PARAMETROS_COLECTORAS]] |
| `GRC_CODIGO` | VARCHAR2 | YES |  |
| `VPA_COLE_DISPLAY` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **FK_VPA_PCO**: `ICO_CODIGO`, `PCO_NOMBRE` → [[XX_PARAMETROS_COLECTORAS]] (`ICO_CODIGO`, `PCO_NOMBRE`)
