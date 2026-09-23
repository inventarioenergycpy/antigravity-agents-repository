---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 462
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_VALORES_COND_PROC"
---

# 📋 XX_VALORES_COND_PROC

**Filas estimadas:** 462

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `COP_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[XX_CONDICIONES_PROCESOS]] |
| `VCP_VALOR` | VARCHAR2 | NO | 🔑 PK |
| `VCP_TIPO_CONDICION` | VARCHAR2 | NO |  |

## FK declaradas → otras tablas

- **VCP_COP_FK**: `COP_CODIGO` → [[XX_CONDICIONES_PROCESOS]] (`COP_CODIGO`)
