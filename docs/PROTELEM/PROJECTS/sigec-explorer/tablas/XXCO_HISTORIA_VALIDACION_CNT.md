---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 3649420
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_HISTORIA_VALIDACION_CNT"
---

# 🔧 XXCO_HISTORIA_VALIDACION_CNT

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

> REGISTRO HISTORICO DE LOS ERRORES/PROBLEMAS DETECTADOS EN LOS CONTRATOS POR EL PROCESO DE VALIDACION DE CONTRATOS. SOLAMENTE SE REGISTRAN AQUELLOS CASOS EN DONDE EL CONTRATO QUEDA COMO NO FACTURABLE. SE MANTIENE UNA HISTORIA DE UN AÑO.

**Filas estimadas:** 3,649,420

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `GRL_CODIGO` | VARCHAR2 | NO |  |  |
| `CRF_ANIO` | NUMBER | NO |  |  |
| `CRF_PERIODO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `VLE_VALIDACION` | VARCHAR2 | NO |  |  |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `SRV_ESTADO` | VARCHAR2 | NO |  |  |
| `CNT_ESTADO` | VARCHAR2 | NO |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `STE_TIPO` | VARCHAR2 | YES |  | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `DEMANDA_CONTRATADA` | NUMBER | YES |  |  |
| `DEMANDA_REGISTRADA` | NUMBER | YES |  |  |
| `CONSUMO` | NUMBER | YES |  |  |
| `LCT_DIAS` | NUMBER | YES |  |  |
| `CONSUMO_PROMEDIO` | NUMBER | YES |  |  |
| `CONSUMO_ANIO_ANTERIOR` | NUMBER | YES |  |  |
| `TCU_GRUPO` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `HVC_FECHA_EJECUCION` | DATE | YES |  |  |
| `USR_CODIGO` | VARCHAR2 | YES |  |  |
