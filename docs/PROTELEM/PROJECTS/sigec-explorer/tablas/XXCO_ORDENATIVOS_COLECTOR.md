---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 5107023
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_ORDENATIVOS_COLECTOR"
---

# 🔧 XXCO_ORDENATIVOS_COLECTOR

**Filas estimadas:** 5,107,023

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ORC_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `RTL_ANIO` | NUMBER | YES |  |  |
| `RTL_PERIODO` | NUMBER | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `USR_NUMERO_TOMA` | NUMBER | YES |  |  |
| `GRM_NUMERO` | NUMBER | YES |  |  |
| `ORD_DATOS_ADICIONALES` | VARCHAR2 | YES |  |  |
| `ORC_FECHA_CARGA` | DATE | YES |  |  |
| `ORD_NUMERO` | NUMBER | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `ORD_DATOS_ASOCIACION` | VARCHAR2 | YES |  |  |
| `ORC_FECHA_REVISION` | DATE | YES |  |  |
| `USR_NUMERO_REVISION` | NUMBER | YES |  |  |
| `ORC_ID_FOTO` | VARCHAR2 | YES |  |  |
| `ORC_GENERAR_ORD` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `USR_NUMERO_TOMA` → [[XXCO_ALTAS_COLECTOR]] _USR_NUMERO_TOMA es PK de XXCO_ALTAS_COLECTOR_
- `RTL_ANIO` → [[XXCO_ALTAS_COLECTOR]] _RTL_ANIO es PK de XXCO_ALTAS_COLECTOR_
- `RTL_PERIODO` → [[XXCO_ALTAS_COLECTOR]] _RTL_PERIODO es PK de XXCO_ALTAS_COLECTOR_
