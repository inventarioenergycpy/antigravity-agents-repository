---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 27
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_GRUPOS_CALIFICACIONES"
---

# 📋 XX_GRUPOS_CALIFICACIONES

**Filas estimadas:** 27

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRF_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `GRF_DESCRIPCION` | VARCHAR2 | NO |  |
| `GRF_ANULADO` | VARCHAR2 | NO |  |

## Tablas que referencian esta tabla

- [[XX_TARIFAS_GRUPOS]] via `GRF_CODIGO`
- [[XX_TIPOS_CALIFICACIONES]] via `GRF_CODIGO`
