---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_INTERFASES_COLECTORAS"
---

# 📋 XX_INTERFASES_COLECTORAS

**Filas estimadas:** 1

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ICO_CODIGO` | NUMBER | NO | 🔑 PK |
| `ICO_NOMBRE` | VARCHAR2 | NO |  |
| `ICO_DESCRIPCION` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[XX_PARAMETROS_COLECTORAS]] via `ICO_CODIGO`
- [[XX_TIPOS_COLECTORAS]] via `ICO_CODIGO`
