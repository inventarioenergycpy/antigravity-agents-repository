---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 10206
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_TRANSFORMADORES"
---

# 🔧 XXCO_TRANSFORMADORES

**Filas estimadas:** 10,206

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TRS_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TRS_FECHA_ALTA` | DATE | NO |  |
| `TRS_FECHA_BAJA` | DATE | YES |  |
| `TRS_MARCA` | VARCHAR2 | NO |  |
| `TRS_CLASE` | VARCHAR2 | YES |  |
| `TRS_RELACION` | VARCHAR2 | YES |  |
| `TRS_VOLTAJE_AMP` | NUMBER | YES |  |
| `TRS_AISLACION` | VARCHAR2 | YES |  |
| `TRS_TIPO` | VARCHAR2 | NO |  |

## Tablas que referencian esta tabla

- [[XXCO_EQUIPO_TRANSFORMADORES]] via `TRS_CODIGO`
