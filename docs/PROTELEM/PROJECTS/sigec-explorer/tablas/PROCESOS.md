---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 49
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PROCESOS"
---

# 📋 PROCESOS

**Filas estimadas:** 49

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PRC_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `PRC_DESCRIPCION` | VARCHAR2 | NO |  |

## Tablas que referencian esta tabla

- [[ESTADOS]] via `PRC_CODIGO`
- [[EVENTOS]] via `PRC_CODIGO`
- [[TRANSICIONES]] via `PRC_CODIGO`
