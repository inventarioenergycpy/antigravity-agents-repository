---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 13
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "IMPRESORES_ORDENATIVOS"
---

# 📋 IMPRESORES_ORDENATIVOS

**Filas estimadas:** 13

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `IMO_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `IMO_DESCRIPCION` | VARCHAR2 | YES |  |
| `IMO_GEN_CODBAR` | VARCHAR2 | YES |  |
| `IMO_COR_Y_CODBAR` | NUMBER | YES |  |
| `IMO_COR_X_CODBAR` | NUMBER | YES |  |

## Tablas que referencian esta tabla

- [[TIPOS_ORDENATIVO]] via `IMO_CODIGO`
