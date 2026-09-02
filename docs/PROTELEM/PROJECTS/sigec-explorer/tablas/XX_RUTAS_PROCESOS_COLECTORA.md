---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 170103
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_RUTAS_PROCESOS_COLECTORA"
---

# 📋 XX_RUTAS_PROCESOS_COLECTORA

**Filas estimadas:** 170,103

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PCL_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[XX_PROCESOS_COLECTORAS]] |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |
| `RTA_CODIGO` | NUMBER | NO | 🔑 PK |
| `RPA_CANTIDAD_SRV` | NUMBER | YES |  |
| `RPA_CANTIDAD_CDR` | NUMBER | YES |  |
| `RTL_CODIGO` | NUMBER | NO | 🔑 PK |
| `GRL_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `ZLE_CODIGO` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **RPA_PCL_FK**: `PCL_NUMERO` → [[XX_PROCESOS_COLECTORAS]] (`PCL_NUMERO`)

## FK inferidas (alta confianza)

- `ZLE_CODIGO` → [[ZONAS_LECTURAS]] _ZLE_CODIGO es PK de ZONAS_LECTURAS_
