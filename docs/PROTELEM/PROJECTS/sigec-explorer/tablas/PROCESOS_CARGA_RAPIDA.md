---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 75
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PROCESOS_CARGA_RAPIDA"
---

# 📋 PROCESOS_CARGA_RAPIDA

**Filas estimadas:** 75

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GCR_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[GRUPOS_CARGA_RAPIDA_ORD]] |
| `PCA_PROCESO` | VARCHAR2 | NO | 🔑 PK |
| `PCA_ORDEN` | NUMBER | NO |  |

## FK declaradas → otras tablas

- **PCA_GCR_FK**: `GCR_CODIGO` → [[GRUPOS_CARGA_RAPIDA_ORD]] (`GCR_CODIGO`)
