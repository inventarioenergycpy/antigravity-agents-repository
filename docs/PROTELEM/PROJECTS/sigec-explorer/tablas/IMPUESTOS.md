---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 7
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "IMPUESTOS"
---

# 📋 IMPUESTOS

**Filas estimadas:** 7

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `IMP_CODIGO` | NUMBER | NO | 🔑 PK |
| `IMP_DESCRIPCION` | VARCHAR2 | YES |  |
| `IMP_GRUPO` | VARCHAR2 | YES |  |
| `IMP_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[DETALLES_IMPUESTO]] via `IMP_CODIGO`
