---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: equipos
num_rows: 27563
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/equipos
  - documentada/negocio
aliases:
  - "XXCO_DATOS_INSPECCION"
---

# 🔧 XXCO_DATOS_INSPECCION

**Prefijo `STE_`:** Stock de equipos — atributos del medidor físico (STOCK_EQUIPOS)

**Filas estimadas:** 27,563

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DAI_COSENO_FI` | NUMBER | YES |  |  |
| `ORD_NUMERO` | NUMBER | YES | 🔗 → [[ORDENATIVOS]] |  |
| `DAI_DEMANDA15` | NUMBER | YES |  |  |
| `DAI_DIFERENCIA_RELOJ` | VARCHAR2 | YES |  |  |
| `DAI_POT_INSTANTANEA` | NUMBER | YES |  |  |
| `DAI_MEDIDOR` | VARCHAR2 | YES |  |  |
| `DAI_DEMANDA` | VARCHAR2 | YES |  |  |
| `DAI_TRANS_TENSION` | VARCHAR2 | YES |  |  |
| `DAI_TRANS_CORRIENTE` | VARCHAR2 | YES |  |  |
| `DAI_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `STE_NUMERO` | NUMBER | NO | 🔗 → [[STOCK_EQUIPOS]] | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `DAI_FECHA_CARGA` | DATE | NO |  |  |
| `DAI_FECHA_LECTURA` | DATE | YES |  |  |
| `EQP_ORDEN` | NUMBER | NO |  |  |
| `STE_TIPO` | VARCHAR2 | NO | 🔗 → [[STOCK_EQUIPOS]] | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `DAI_FECHA_VERIFICACION` | DATE | YES |  |  |
| `DAI_USUARIO_VERIFICACION` | NUMBER | YES |  |  |
| `DAI_FECHA_ULT_MODIF` | DATE | YES |  |  |
| `DAI_USR_ULT_MODIF` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **DAI_ORD_FK**: `ORD_NUMERO` → [[ORDENATIVOS]] (`ORD_NUMERO`)
- **DAI_STE_FK**: `STE_NUMERO`, `STE_TIPO` → [[STOCK_EQUIPOS]] (`STE_NUMERO`, `STE_TIPO`)
