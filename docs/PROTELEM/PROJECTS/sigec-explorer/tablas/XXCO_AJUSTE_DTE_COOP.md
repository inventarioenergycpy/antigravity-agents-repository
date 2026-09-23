---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 3717
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_AJUSTE_DTE_COOP"
---

# 🔧 XXCO_AJUSTE_DTE_COOP

**Filas estimadas:** 3,717

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ADC_NEMO` | VARCHAR2 | YES |  |  |
| `ADC_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `ADC_MUNICIPIO` | VARCHAR2 | YES |  |  |
| `ADC_IMPORTE` | NUMBER | YES |  |  |
| `ADC_ANIO` | NUMBER | YES |  |  |
| `ADC_PERIODO` | NUMBER | YES |  |  |
| `ADC_FECHA_CARGA` | DATE | YES |  |  |
| `ADC_IAF_FECHA_GENERACION` | DATE | YES |  |  |
| `ADC_TIPO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `IAF_NUMERO` | NUMBER | YES |  |  |
