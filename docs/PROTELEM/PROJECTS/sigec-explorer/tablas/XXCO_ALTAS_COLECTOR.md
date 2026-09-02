---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 50733
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_ALTAS_COLECTOR"
---

# 🔧 XXCO_ALTAS_COLECTOR

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

> Altas cargadas por colectoras

**Filas estimadas:** 50,733

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `SRV_ORDEN_LECTURA` | NUMBER | YES |  |  |
| `SRV_DIRECCION` | VARCHAR2 | YES |  |  |
| `SRV_CALLE` | VARCHAR2 | YES |  |  |
| `SRV_NRO` | NUMBER | YES |  |  |
| `SRV_PISO` | VARCHAR2 | YES |  |  |
| `SRV_DEPTO` | VARCHAR2 | YES |  |  |
| `SRV_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `SRV_ORDEN_LECTURA_ANTERIOR` | NUMBER | YES |  |  |
| `GRL_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `RTL_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `SRV_ACCESO_MEDIDOR` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `RTL_ANIO` | NUMBER | NO | 🔑 PK |  |
| `RTL_PERIODO` | NUMBER | NO | 🔑 PK |  |
| `STE_TIPO` | VARCHAR2 | YES |  | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `USR_NUMERO_TOMA` | NUMBER | NO | 🔑 PK |  |
| `GRM_NUMERO` | NUMBER | YES |  |  |
| `ALC_FECHA_CARGA` | DATE | YES |  |  |
