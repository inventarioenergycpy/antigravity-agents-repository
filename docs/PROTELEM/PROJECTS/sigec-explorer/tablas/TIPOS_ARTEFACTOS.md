---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 82
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "TIPOS_ARTEFACTOS"
---

# 📋 TIPOS_ARTEFACTOS

**Filas estimadas:** 82

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TIA_CODIGO` | NUMBER | NO | 🔑 PK |
| `TIA_DESCRIPCION` | VARCHAR2 | NO |  |
| `TIA_CONSUMO` | NUMBER | YES |  |
| `TIA_MOSTRAR_EN_LISTA` | VARCHAR2 | YES |  |
| `TIA_ITEM_OTROS` | VARCHAR2 | YES |  |
| `USR_CODIGO` | VARCHAR2 | YES |  |
| `TIA_FECHA_CARGA` | DATE | YES |  |
| `TIA_FECHA_FIN` | DATE | YES |  |
| `SUB_CODIGO` | NUMBER | YES | 🔗 → [[XXCO_ARTEFACTOS_SUBCATEGORIAS]] |

## FK declaradas → otras tablas

- **XXCO_TIA_SUB_CODIGO_FK**: `SUB_CODIGO` → [[XXCO_ARTEFACTOS_SUBCATEGORIAS]] (`SUB_CODIGO`)

## FK inferidas (alta confianza)

- `SUB_CODIGO` → [[XXCO_ARTEFACTOS_SUBCATEGORIAS]] _SUB_CODIGO es PK de XXCO_ARTEFACTOS_SUBCATEGORIAS_
