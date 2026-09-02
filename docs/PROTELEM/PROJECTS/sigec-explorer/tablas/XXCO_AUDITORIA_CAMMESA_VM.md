---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 48887837
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_AUDITORIA_CAMMESA_VM"
---

# 🔧 XXCO_AUDITORIA_CAMMESA_VM

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 48,887,837

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `FECHA_LEC` | DATE | YES |  |  |
| `FECHA_LEC_ANT` | DATE | YES |  |  |
| `FECHA_EMISION` | DATE | YES |  |  |
| `TIPO_LEC` | VARCHAR2 | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | NO | 🔑 PK |  |
| `DOC_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `PERIODO` | NUMBER | YES |  |  |
| `ANIO` | NUMBER | YES |  |  |
| `POT_FAC_PTA` | NUMBER | YES |  |  |
| `POT_FAC_FTA` | NUMBER | YES |  |  |
| `POT_C_PTA` | NUMBER | YES |  |  |
| `POT_C_FTA` | NUMBER | YES |  |  |
| `CONS_PICO` | NUMBER | YES |  |  |
| `CONS_RESTO` | NUMBER | YES |  |  |
| `CONS_VALLE` | NUMBER | YES |  |  |
| `POT_LCT_PTA` | NUMBER | YES |  |  |
| `POT_LCT_FTA` | NUMBER | YES |  |  |
| `GRUPO_CAMMESA` | CHAR | YES |  |  |
| `CONS_DIARIO` | NUMBER | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `CONS_ENERGIA` | NUMBER | YES |  | Consumo de energía facturado (kWh) en AUDITORIA_CAMMESA. El consumo total del período se arma sumando CONS_ENERGIA+CONS_PICO+CONS_VALLE+CONS_RESTO. |
| `TCL_CODIGO_GRAL` | VARCHAR2 | YES |  | Código de tarifa 'general' en AUDITORIA_CAMMESA. Se une a TARIFAS.TCL_CODIGO para clasificar el consumo por sector/rubro (vía TARIFAS.TCL_GRUPO). |
| `CLA_CODIGO_GRAL` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO_GRAL` | VARCHAR2 | YES |  |  |
| `CONS_ERT` | NUMBER | YES |  |  |
| `TFA_CODIGO` | VARCHAR2 | YES |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `CONS_ENE_D` | NUMBER | YES |  |  |
| `CONS_ENE_N` | NUMBER | YES |  |  |
| `EDI_NUMERO` | NUMBER | YES |  |  |
| `DOC_IMPORTE_BASICO` | NUMBER | YES |  | NO USAR como neto de la factura: coincide con DOC_IMPORTE_GRAVADO en solo el 70,6% y es MENOR en el 28,2% (muestra 322.120 docs de 2025). Poblada al 100% pero con semántica distinta al neto gravado. Para el neto usar DOC_IMPORTE_GRAVADO. |
| `IMPORTE_ENERGIA_SIN_SUB` | NUMBER | YES |  |  |
| `IMPORTE_ENERGIA_CON_SUB` | NUMBER | YES |  |  |
| `IMPORTE_CARGO_FIJO` | NUMBER | YES |  |  |
| `IMPORTE_CARGO_OBRA` | NUMBER | YES |  |  |
| `IMPORTE_IMPUESTO_NACIONAL` | NUMBER | YES |  |  |
| `IMPORTE_IMPUESTO_PROVINCIAL` | NUMBER | YES |  |  |
| `IMPORTE_SUBSIDIO` | NUMBER | YES |  |  |
| `IMPORTE_COSENO_FI` | NUMBER | YES |  |  |
| `CONSUMO_PICO_CS` | NUMBER | YES |  |  |
| `CONSUMO_RESTO_CS` | NUMBER | YES |  |  |
| `CONSUMO_VALLE_CS` | NUMBER | YES |  |  |
| `CONSUMO_ENERGIA_CS` | NUMBER | YES |  |  |
| `CONSUMO_PICO_SS` | NUMBER | YES |  |  |
| `CONSUMO_RESTO_SS` | NUMBER | YES |  |  |
| `CONSUMO_VALLE_SS` | NUMBER | YES |  |  |
| `CONSUMO_ENERGIA_SS` | NUMBER | YES |  |  |
| `DOC_PRELIQUIDACION` | VARCHAR2 | YES |  |  |
| `FECHA_EMISION_COMPLETA` | DATE | YES |  |  |
| `AJUSTE_IMPORTE_COSENO_FI` | NUMBER | YES |  |  |
| `IMPORTE_FACTURACION_NETA` | NUMBER | YES |  |  |
