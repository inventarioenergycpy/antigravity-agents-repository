---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 292
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_ASIGNACION_COLECTORAS"
---

# 📋 XX_ASIGNACION_COLECTORAS

**Filas estimadas:** 292

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ACO_FECHA_HASTA` | DATE | YES |  |
| `ACO_FECHA_DESDE` | DATE | NO | 🔑 PK |
| `CLE_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XX_COLECTORAS]] |
| `ACO_OBSERVACIONES` | VARCHAR2 | YES |  |
| `USR_NUMERO` | NUMBER | NO | 🔗 → [[USUARIOS]] |

## FK declaradas → otras tablas

- **FK_ACO_CLE**: `CLE_CODIGO` → [[XX_COLECTORAS]] (`CLE_CODIGO`)
- **FK_ACO_USR**: `USR_NUMERO` → [[USUARIOS]] (`USR_NUMERO`)
