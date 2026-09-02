---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: lecturas
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "XXCO_LCT_0400_TMP"
---

# ⏱️ XXCO_LCT_0400_TMP

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `VAC_NUMERO` | NUMBER | NO |  |  |
| `GRL_CODIGO` | VARCHAR2 | NO |  |  |
| `GRF_CODIGO` | VARCHAR2 | NO |  |  |
| `CRF_ANIO` | NUMBER | NO |  |  |
| `CRF_PERIODO` | NUMBER | NO |  |  |
| `CRF_ANIO2` | NUMBER | YES |  |  |
| `CRF_PERIODO2` | NUMBER | YES |  |  |
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `SRV_ESTADO` | VARCHAR2 | NO |  |  |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_ESTADO` | VARCHAR2 | NO |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `GRM_NUMERO` | NUMBER | YES |  |  |
| `EQP_ORDEN` | NUMBER | YES |  |  |
| `STE_TIPO` | VARCHAR2 | YES |  | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `VLE_VALIDACION` | VARCHAR2 | NO |  |  |
| `VAC_DEMANDA_CONTRATADA` | NUMBER | YES |  |  |
| `VAC_DEMANDA_REGISTRADA` | NUMBER | YES |  |  |
| `VAC_CONSUMO` | NUMBER | YES |  |  |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `FACTURABLE` | VARCHAR2 | NO |  |  |
| `LCT_DIAS` | NUMBER | YES |  |  |
| `VAC_CONSUMO_PROMEDIO` | NUMBER | YES |  |  |
| `VAC_CONSUMO_ANIO_ANTERIOR` | NUMBER | YES |  |  |
| `TCU_GRUPO` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `LCT_FECHA_LECTURA` | DATE | YES |  | Fecha en que se tomó la lectura. |
| `LCT_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `VAC_FECHA_CARGA` | DATE | YES |  |  |
| `USR_NUMERO_CARGA` | NUMBER | YES |  |  |
| `RTA_CODIGO_PARAM` | NUMBER | YES |  |  |
| `RTL_CODIGO_PARAM` | NUMBER | YES |  |  |
| `VAC_NUMERO_MAX` | NUMBER | YES |  |  |
