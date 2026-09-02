---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1609
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "GRUPOS_CORRIDA"
---

# 📋 GRUPOS_CORRIDA

**Filas estimadas:** 1,609

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRC_ID` | NUMBER | NO | 🔑 PK |
| `GRC_FECHA_CORRIDA` | DATE | NO |  |
| `GRC_ANIO_PERIODO` | VARCHAR2 | NO |  |
| `GRC_ARCHIVO_SUM` | VARCHAR2 | YES |  |
| `GRC_ARCHIVO_DET` | VARCHAR2 | YES |  |
| `GRC_GRP_ID` | NUMBER | NO | 🔗 → [[GRUPOS]] |
| `GRC_USR_NUMERO` | NUMBER | NO |  |

## FK declaradas → otras tablas

- **GRC_GRP_FK**: `GRC_GRP_ID` → [[GRUPOS]] (`GRP_ID`)
