---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: equipos
num_rows: 4097250
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/equipos
  - documentada/negocio
aliases:
  - "EQUIPOS"
---

# 📋 EQUIPOS

> [!info] Significado de negocio
> Instalaciones de medidores: tabla puente entre el punto de medición del suministro (SRV_CODIGO, GRM_NUMERO) y el medidor físico (STE_NUMERO, STE_TIPO). PK (SRV_CODIGO, GRM_NUMERO, EQP_ORDEN). ~4M filas.

**Prefijo `EQP_`:** Equipos instalados en puntos de medición (EQUIPOS)

**Filas estimadas:** 4,097,250

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[PUNTOS_MEDICION]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[PUNTOS_MEDICION]] |  |
| `EQP_ORDEN` | NUMBER | NO | 🔑 PK |  |
| `STE_TIPO` | VARCHAR2 | NO | 🔗 → [[STOCK_EQUIPOS]] | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `STE_NUMERO` | NUMBER | NO | 🔗 → [[STOCK_EQUIPOS]] | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `EQP_FACTOR_INTENSIDAD` | NUMBER | NO |  |  |
| `EQP_FACTOR_TENSION` | NUMBER | NO |  |  |
| `EQP_FECHA_INSTAL` | DATE | YES |  |  |
| `EQP_PRECINTO` | VARCHAR2 | YES |  |  |
| `EQP_FECHA_RETIRO` | DATE | YES |  |  |
| `EQP_ESTADO` | VARCHAR2 | YES |  |  |
| `EQP_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `EQP_PROGRAMA` | VARCHAR2 | YES |  |  |
| `EQP_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
| `EQP_ULTIMA_ACTUALIZACION_MDM` | DATE | YES |  |  |

## FK declaradas → otras tablas

- **EQP_FK_GRM**: `SRV_CODIGO`, `GRM_NUMERO` → [[PUNTOS_MEDICION]] (`SRV_CODIGO`, `GRM_NUMERO`)
- **EQP_FK_STE**: `STE_NUMERO`, `STE_TIPO` → [[STOCK_EQUIPOS]] (`STE_NUMERO`, `STE_TIPO`)

## Tablas que referencian esta tabla

- [[CUADRANTES]] via `EQP_ORDEN`, `GRM_NUMERO`, `SRV_CODIGO`
- [[XXCO_EQUIPO_TRANSFORMADORES]] via `EQP_ORDEN`, `GRM_NUMERO`, `SRV_CODIGO`
- [[XXCO_LECTURAS_LABORATORIO]] via `EQP_ORDEN`, `GRM_NUMERO`, `SRV_CODIGO`
- [[XXCO_MOVIMIENTOS_EQUIPOS]] via `EQP_ORDEN_INSTALADO`, `GRM_NUMERO_INSTALADO`, `SRV_CODIGO_INSTALADO`
- [[XXCO_PRECINTOS]] via `EQP_ORDEN`, `GRM_NUMERO`, `SRV_CODIGO`
