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
  - "XX_PARAMETROS_COLECTORAS"
---

# 📋 XX_PARAMETROS_COLECTORAS

**Filas estimadas:** 4

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PCO_NOMBRE` | VARCHAR2 | NO | 🔑 PK |
| `PCO_DESCRIPCION` | VARCHAR2 | YES |  |
| `PCO_TABLA_ASOCIADA` | VARCHAR2 | YES |  |
| `ICO_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[XX_INTERFASES_COLECTORAS]] |
| `PCO_NOMBRE_ARCHIVO` | VARCHAR2 | NO |  |
| `PCO_TAMANIO_ARCHIVO` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **FK_PCO_ICO**: `ICO_CODIGO` → [[XX_INTERFASES_COLECTORAS]] (`ICO_CODIGO`)

## Tablas que referencian esta tabla

- [[XX_VALORES_PARAMETROS]] via `ICO_CODIGO`, `PCO_NOMBRE`
