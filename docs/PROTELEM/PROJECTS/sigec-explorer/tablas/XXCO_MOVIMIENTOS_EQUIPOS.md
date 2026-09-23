---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: equipos
num_rows: 8990383
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/equipos
  - documentada/negocio
aliases:
  - "XXCO_MOVIMIENTOS_EQUIPOS"
---

# 🔧 XXCO_MOVIMIENTOS_EQUIPOS

**Prefijo `STE_`:** Stock de equipos — atributos del medidor físico (STOCK_EQUIPOS)

**Filas estimadas:** 8,990,383

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `STE_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[STOCK_EQUIPOS]] | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `MEQ_ORDEN` | NUMBER | NO | 🔑 PK |  |
| `STE_TIPO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[STOCK_EQUIPOS]] | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `GRM_NUMERO_INSTALADO` | NUMBER | YES | 🔗 → [[EQUIPOS]] |  |
| `EQP_ORDEN_INSTALADO` | NUMBER | YES | 🔗 → [[EQUIPOS]] |  |
| `SRV_CODIGO_INSTALADO` | NUMBER | YES | 🔗 → [[EQUIPOS]] |  |
| `USR_NUMERO_ASIGNADO` | NUMBER | YES |  |  |
| `SEC_CODIGO_ASIGNADO` | VARCHAR2 | NO | 🔗 → [[SECTORES]] |  |
| `LEQ_NUMERO_ASIGNADO` | NUMBER | YES |  |  |
| `MEQ_FECHA_ENTRADA` | DATE | NO |  |  |
| `MEQ_FECHA_SALIDA` | DATE | YES |  |  |
| `MEQ_FECHA_MOVIMIENTO` | DATE | NO |  |  |
| `USR_NUMERO_MOVIMIENTO` | NUMBER | NO | 🔗 → [[USUARIOS]] |  |
| `SCF_CODIGO_ASIGNADO` | NUMBER | NO | 🔗 → [[SUCURSALES]] |  |
| `MEQ_TIPO` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **SYS_C00157568**: `SEC_CODIGO_ASIGNADO` → [[SECTORES]] (`SEC_CODIGO`)
- **SYS_C00157569**: `USR_NUMERO_MOVIMIENTO` → [[USUARIOS]] (`USR_NUMERO`)
- **XXCO_MOVIMIENTOS_EQUIPOS_FK1**: `STE_NUMERO`, `STE_TIPO` → [[STOCK_EQUIPOS]] (`STE_NUMERO`, `STE_TIPO`)
- **XXCO_MOVIMIENTOS_EQUIPOS_FK2**: `SRV_CODIGO_INSTALADO`, `GRM_NUMERO_INSTALADO`, `EQP_ORDEN_INSTALADO` → [[EQUIPOS]] (`SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`)
- **XXCO_MOVIMIENTOS_EQUIPOS_FK4**: `SCF_CODIGO_ASIGNADO` → [[SUCURSALES]] (`SCF_CODIGO`)
