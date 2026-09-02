---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 4
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_ESTADOS_PROCESO_COLECT"
---

# 📋 XX_ESTADOS_PROCESO_COLECT

**Filas estimadas:** 4

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `EPC_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `EPC_DESCRIPCION` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[XX_PROCESOS_COLECTORAS]] via `EPC_CODIGO`
