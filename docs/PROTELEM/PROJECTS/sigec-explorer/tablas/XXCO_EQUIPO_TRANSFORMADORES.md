---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 7354
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_EQUIPO_TRANSFORMADORES"
---

# 🔧 XXCO_EQUIPO_TRANSFORMADORES

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 7,354

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `EQT_FECHA_INSTALACION` | DATE | NO | 🔑 PK |  |
| `EQT_FECHA_RETIRO` | DATE | YES |  |  |
| `EQP_ORDEN` | NUMBER | NO | 🔑 PK · 🔗 → [[EQUIPOS]] |  |
| `GRM_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[EQUIPOS]] |  |
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[EQUIPOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `TRS_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_TRANSFORMADORES]] |  |
| `ORD_NUMERO` | NUMBER | YES | 🔗 → [[ORDENATIVOS]] |  |

## FK declaradas → otras tablas

- **EQT_EQP_FK**: `SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN` → [[EQUIPOS]] (`SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`)
- **EQT_ORD_FK**: `ORD_NUMERO` → [[ORDENATIVOS]] (`ORD_NUMERO`)
- **EQT_TRS_FK**: `TRS_CODIGO` → [[XXCO_TRANSFORMADORES]] (`TRS_CODIGO`)

## Tablas que referencian esta tabla

- [[XXCO_MEDICIONES]] via `EQP_ORDEN`, `EQT_FECHA_INSTALACION`, `GRM_NUMERO`, `SRV_CODIGO`, `TRS_CODIGO`
