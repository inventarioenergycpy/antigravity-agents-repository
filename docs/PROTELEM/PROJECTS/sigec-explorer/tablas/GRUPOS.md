---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 23
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "GRUPOS"
---

# 📋 GRUPOS

**Filas estimadas:** 23

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRP_ID` | NUMBER | NO | 🔑 PK |
| `GRP_FECHA_CARGA` | DATE | NO |  |
| `GRP_VALOR_DESDE` | NUMBER | NO |  |
| `GRP_VALOR_HASTA` | NUMBER | NO |  |
| `GRP_RESTRICCION` | VARCHAR2 | NO |  |
| `GRP_DETALLADO` | VARCHAR2 | YES |  |
| `GRP_PRIORIDAD` | NUMBER | YES |  |

## Tablas que referencian esta tabla

- [[CUADRANTES_GRUPO]] via `CUG_GRP_ID`
- [[GRUPOS_CORRIDA]] via `GRC_GRP_ID`
- [[GRUPOS_TARIFA]] via `GTA_GRP_ID`
