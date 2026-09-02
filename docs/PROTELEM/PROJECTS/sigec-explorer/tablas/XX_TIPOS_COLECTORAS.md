---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 2
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_TIPOS_COLECTORAS"
---

# 📋 XX_TIPOS_COLECTORAS

**Filas estimadas:** 2

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TCO_CODIGO` | NUMBER | NO | 🔑 PK |
| `TCO_DESCRIPCION` | VARCHAR2 | NO |  |
| `TCO_MODELO` | VARCHAR2 | YES |  |
| `TCO_MARCA` | VARCHAR2 | YES |  |
| `TCO_OBSERVACIONES` | VARCHAR2 | YES |  |
| `ICO_CODIGO` | NUMBER | NO | 🔗 → [[XX_INTERFASES_COLECTORAS]] |

## FK declaradas → otras tablas

- **FK_TCO_ICO**: `ICO_CODIGO` → [[XX_INTERFASES_COLECTORAS]] (`ICO_CODIGO`)

## Tablas que referencian esta tabla

- [[XX_COLECTORAS]] via `TCO_CODIGO`
