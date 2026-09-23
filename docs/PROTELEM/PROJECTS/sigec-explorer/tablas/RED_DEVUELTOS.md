---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 9657
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "RED_DEVUELTOS"
---

# 📋 RED_DEVUELTOS

**Filas estimadas:** 9,657

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RTI_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `RDE_ARCHIVO_DEV` | VARCHAR2 | NO | 🔑 PK |
| `RDE_FECHA_RED` | DATE | NO | 🔑 PK |
| `RDE_FECHA_PROCESO` | DATE | YES |  |
| `RDE_CANT_ERROR` | NUMBER | YES |  |

## Tablas que referencian esta tabla

- [[RED_DEVUELTOS_ERR]] via `RDE_ARCHIVO_DEV`, `RDE_FECHA_RED`, `RTI_TIPO`
