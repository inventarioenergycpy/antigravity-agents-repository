---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 7751
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "RED_MONITOR"
---

# 📋 RED_MONITOR

**Filas estimadas:** 7,751

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RTI_TIPO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[RED_TIPOS]] |
| `RMO_ARCHIVO` | VARCHAR2 | NO | 🔑 PK |
| `RMO_CUOTA` | VARCHAR2 | NO | 🔑 PK |
| `RMO_ANIO` | NUMBER | NO | 🔑 PK |
| `RMO_FECHA_GENERACION` | DATE | YES |  |
| `RMO_VOLUMEN` | VARCHAR2 | YES |  |
| `RMO_CANT_REG` | NUMBER | YES |  |
| `RMO_IMPORTE_1` | NUMBER | NO |  |
| `RMO_IMPORTE_2` | NUMBER | NO |  |
| `RMO_FECHA_ULTIMA` | DATE | NO |  |
| `RMO_TAMANIO` | NUMBER | YES |  |
| `RMO_SEQ` | NUMBER | YES |  |
| `RMO_ORDEN` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **RTI_TIPO_FK**: `RTI_TIPO` → [[RED_TIPOS]] (`RTI_TIPO`)
