---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 333657
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_LECTURAS_LABORATORIO"
---

# 🔧 XXCO_LECTURAS_LABORATORIO

**Filas estimadas:** 333,657

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LEL_FECHA_LECTURA` | DATE | NO |  |  |
| `LEL_VALOR_LEIDO` | NUMBER | NO |  |  |
| `GRM_NUMERO` | NUMBER | NO | 🔗 → [[EQUIPOS]] |  |
| `EQP_ORDEN` | NUMBER | NO | 🔗 → [[EQUIPOS]] |  |
| `SRV_CODIGO` | NUMBER | NO | 🔗 → [[EQUIPOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CDR_UNIDAD` | VARCHAR2 | YES | 🔗 → [[CUADRANTES]] |  |
| `ORD_NUMERO` | NUMBER | YES | 🔗 → [[ORDENATIVOS]] |  |
| `LEL_CODIGO_MEDIDOR` | VARCHAR2 | YES |  |  |
| `LEL_FECHA_TRANSFERENCIA` | DATE | YES |  |  |
| `LEL_FECHA_CARGA` | DATE | YES |  |  |

## FK declaradas → otras tablas

- **LEL_CDR_FK**: `SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`, `CDR_UNIDAD` → [[CUADRANTES]] (`SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`, `CDR_UNIDAD`)
- **LEL_EQP_FK**: `SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN` → [[EQUIPOS]] (`SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`)
- **LEL_ORD_FK**: `ORD_NUMERO` → [[ORDENATIVOS]] (`ORD_NUMERO`)
