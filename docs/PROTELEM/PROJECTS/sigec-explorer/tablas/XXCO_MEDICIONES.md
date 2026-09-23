---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_MEDICIONES"
---

# 🔧 XXCO_MEDICIONES

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `MEN_FECHA_MEDICION` | DATE | NO | 🔑 PK |  |
| `MEN_VALOR_PRIMARIO` | NUMBER | YES |  |  |
| `MEN_VALOR_SECUNDARIO` | NUMBER | NO |  |  |
| `EQT_FECHA_INSTALACION` | DATE | NO | 🔑 PK · 🔗 → [[XXCO_EQUIPO_TRANSFORMADORES]] |  |
| `GRM_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_EQUIPO_TRANSFORMADORES]] |  |
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_EQUIPO_TRANSFORMADORES]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `EQP_ORDEN` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_EQUIPO_TRANSFORMADORES]] |  |
| `TRS_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_EQUIPO_TRANSFORMADORES]] |  |
| `ORD_NUMERO` | NUMBER | NO | 🔗 → [[ORDENATIVOS]] |  |

## FK declaradas → otras tablas

- **MEN_EQT_FK**: `SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`, `TRS_CODIGO`, `EQT_FECHA_INSTALACION` → [[XXCO_EQUIPO_TRANSFORMADORES]] (`SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`, `TRS_CODIGO`, `EQT_FECHA_INSTALACION`)
- **MEN_ORD_FK**: `ORD_NUMERO` → [[ORDENATIVOS]] (`ORD_NUMERO`)
