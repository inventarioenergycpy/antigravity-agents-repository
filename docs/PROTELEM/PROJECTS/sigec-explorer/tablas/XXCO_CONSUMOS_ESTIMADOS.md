---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 36630
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_CONSUMOS_ESTIMADOS"
---

# 🔧 XXCO_CONSUMOS_ESTIMADOS

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 36,630

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CDR_UNIDAD` | VARCHAR2 | NO | 🔑 PK |  |
| `CES_PERIODO` | NUMBER | NO | 🔑 PK |  |
| `CES_ANIO` | NUMBER | NO | 🔑 PK |  |
| `CES_CONSUMO` | NUMBER | YES |  |  |
| `CES_CONSUMO_DIARIO` | NUMBER | YES |  |  |
| `CES_DIAS` | NUMBER | YES |  |  |
| `CES_FECHA_ESTIMACION` | DATE | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `CPR_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `CES_VL_CONS_PER_ANT` | NUMBER | YES |  |  |
| `CES_VL_CONS_ANIO_ANT` | NUMBER | YES |  |  |
| `CES_VL_PROM_COS_DIARIO` | NUMBER | YES |  |  |
| `CES_FL_LEC_PAR_IMPAR` | VARCHAR2 | YES |  |  |
| `CES_VL_TENDENCIA_CONS` | NUMBER | YES |  |  |
| `CES_VL_CANT_LECT_CALC` | NUMBER | YES |  |  |
| `CES_VL_CANT_LECT_REGULARES` | NUMBER | YES |  |  |
| `CES_FL_CONSUMOS_REGULARES` | VARCHAR2 | YES |  |  |
| `CES_VL_MAYOR_CONS_CALC` | NUMBER | YES |  |  |
| `CES_VL_MENOR_CONS_CALC` | NUMBER | YES |  |  |
| `CES_FL_RIESGO_PER_ANT_MIN` | VARCHAR2 | YES |  |  |
| `CES_FL_RIESGO_ANIO_ANT_MIN` | VARCHAR2 | YES |  |  |
| `CES_FL_RIESGO_PREDICCION` | VARCHAR2 | YES |  |  |
| `CES_FL_CAMBIO_TARIFA` | VARCHAR2 | YES |  |  |
| `CES_FECHA_CARGA` | DATE | YES |  |  |
| `CES_DIAS_PREPOPORCIONADOS` | NUMBER | YES |  |  |
| `CES_CONSUMO_PREOPORCIONADO` | NUMBER | YES |  |  |
| `CES_OBSERVACIONES_CALCULO` | VARCHAR2 | YES |  |  |
