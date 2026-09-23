---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 4849173
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "CUADRANTES"
---

# 📋 CUADRANTES

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 4,849,173

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[EQUIPOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[EQUIPOS]] |  |
| `EQP_ORDEN` | NUMBER | NO | 🔑 PK · 🔗 → [[EQUIPOS]] |  |
| `CDR_ORDEN` | NUMBER | NO |  |  |
| `CDR_UNIDAD` | VARCHAR2 | NO | 🔑 PK |  |
| `CDR_ENTEROS` | NUMBER | NO |  |  |
| `CDR_DECIMALES` | NUMBER | NO |  |  |
| `CDR_ACUMULATIVO` | VARCHAR2 | YES |  |  |
| `CDR_FACTOR_ENTREGA` | NUMBER | NO |  |  |
| `CDR_FACTOR` | NUMBER | NO |  |  |
| `CDR_REFERENCIA` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **CDR_FK_EQP**: `SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN` → [[EQUIPOS]] (`SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`)

## Tablas que referencian esta tabla

- [[LECTURAS]] via `CDR_UNIDAD`, `EQP_ORDEN`, `GRM_NUMERO`, `SRV_CODIGO`
- [[XXCO_LECTURAS_COLECTOR]] via `CDR_UNIDAD`, `EQP_ORDEN`, `GRM_NUMERO`, `SRV_CODIGO`
- [[XXCO_LECTURAS_LABORATORIO]] via `CDR_UNIDAD`, `EQP_ORDEN`, `GRM_NUMERO`, `SRV_CODIGO`
