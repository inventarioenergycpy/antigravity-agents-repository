---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 24
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "GRUPOS_CARGA_RAPIDA_ORD"
---

# 📋 GRUPOS_CARGA_RAPIDA_ORD

**Filas estimadas:** 24

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GCR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `GCR_DESCRIPCION` | VARCHAR2 | NO |  |

## Tablas que referencian esta tabla

- [[DET_GRUPOS_CARGA_RAPIDA_ORD]] via `GCR_CODIGO`
- [[PROCESOS_CARGA_RAPIDA]] via `GCR_CODIGO`
