---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: equipos
num_rows: 2232780
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/equipos
  - documentada/negocio
aliases:
  - "STOCK_EQUIPOS"
---

# 📋 STOCK_EQUIPOS

> [!info] Significado de negocio
> Medidores y equipos físicos (~2,2M filas). PK compuesta (STE_NUMERO, STE_TIPO). Atributos del aparato: marca, modelo, serie, amperaje, estado.

**Prefijo `STE_`:** Stock de equipos — atributos del medidor físico (STOCK_EQUIPOS)

**Filas estimadas:** 2,232,780

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `STE_NUMERO` | NUMBER | NO | 🔑 PK | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `STE_FACTOR_EQUIPO` | NUMBER | NO |  |  |
| `SCF_CODIGO` | NUMBER | YES | 🔗 → [[SUCURSALES]] |  |
| `STE_AMPERAJE` | NUMBER | YES |  |  |
| `STE_MARCA` | VARCHAR2 | YES |  |  |
| `STE_FECHA_BAJA` | DATE | YES |  |  |
| `STE_TIPO` | VARCHAR2 | NO | 🔑 PK | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `STE_TENSION` | NUMBER | YES |  |  |
| `STE_SERIE` | VARCHAR2 | YES |  |  |
| `STE_PRECINTO` | VARCHAR2 | YES |  |  |
| `STE_MODELO` | VARCHAR2 | YES |  |  |
| `STE_ESTADO` | VARCHAR2 | YES |  |  |
| `STE_ANIO_FABRICACION` | NUMBER | YES |  |  |
| `STE_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `STE_CLASE` | VARCHAR2 | YES |  |  |
| `STE_FECHA_ALTA` | DATE | YES |  |  |
| `STE_AMPERAJE_MAXIMO` | NUMBER | YES |  |  |
| `STE_AMPERAJE_NOMINAL` | NUMBER | YES |  |  |
| `STE_FASES` | VARCHAR2 | YES |  |  |
| `STE_HORARIOS` | VARCHAR2 | YES |  |  |
| `STE_MIDE_ACTIVA` | VARCHAR2 | YES |  |  |
| `STE_MIDE_HORA` | VARCHAR2 | YES |  |  |
| `STE_MIDE_POTENCIA` | VARCHAR2 | YES |  |  |
| `STE_MIDE_REACTIVA` | VARCHAR2 | YES |  |  |
| `STE_MIGRADO` | VARCHAR2 | YES |  |  |
| `GRC_CODIGO` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **STE_FK_SCF**: `SCF_CODIGO` → [[SUCURSALES]] (`SCF_CODIGO`)

## Tablas que referencian esta tabla

- [[EQUIPOS]] via `STE_NUMERO`, `STE_TIPO`
- [[XXCO_DATOS_INSPECCION]] via `STE_NUMERO`, `STE_TIPO`
- [[XXCO_MOVIMIENTOS_EQUIPOS]] via `STE_NUMERO`, `STE_TIPO`
