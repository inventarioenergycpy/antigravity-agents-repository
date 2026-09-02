---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: cobranza
num_rows: 98
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/cobranza
aliases:
  - "XX_TIPOS_CALIFICACIONES"
---

# 📋 XX_TIPOS_CALIFICACIONES

**Filas estimadas:** 98

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TCA_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `GRF_CODIGO` | VARCHAR2 | NO | 🔗 → [[XX_GRUPOS_CALIFICACIONES]] |
| `TCA_RANGO_DESDE` | VARCHAR2 | NO | 🔑 PK |
| `TCA_RANGO_HASTA` | VARCHAR2 | NO | 🔑 PK |
| `TCA_VALOR` | VARCHAR2 | NO | 🔑 PK |
| `TCA_FECHA_DESDE` | DATE | NO |  |
| `TCA_FECHA_HASTA` | DATE | YES |  |

## FK declaradas → otras tablas

- **TCA_GRF_FK**: `GRF_CODIGO` → [[XX_GRUPOS_CALIFICACIONES]] (`GRF_CODIGO`)
