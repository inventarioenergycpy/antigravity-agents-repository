---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 8428637
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "DEBITO_TARJETA_COBRADO"
---

# 📋 DEBITO_TARJETA_COBRADO

> Tabla donde la Tarjeta informa lo cobrado.

**Filas estimadas:** 8,428,637

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DTC_TIPO_REG` | NUMBER | NO |  |  |
| `DTC_COD_TARJETA` | VARCHAR2 | NO |  |  |
| `DTC_NRO_TARJETA` | VARCHAR2 | NO |  |  |
| `DTC_FECHA_PRESENTACION` | DATE | YES |  |  |
| `DTC_FECHA_PROCESO` | DATE | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DTC_CANT_DEBITOS` | NUMBER | YES |  |  |
| `DTC_IMPORTE` | NUMBER | YES |  |  |
| `DTC_COD_RECHAZO` | VARCHAR2 | YES |  |  |
| `DTC_ESTADO` | VARCHAR2 | YES |  |  |
| `DTC_FECHA_CARGA` | DATE | YES |  |  |
| `DTC_ORDEN` | NUMBER | YES |  |  |
| `DTC_DOC_NUMERO` | NUMBER | YES |  |  |
| `DTC_FECHA_ENVIO_INTIMA` | DATE | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `CPR_NUMERO_DEBITO` | NUMBER | YES |  |  |
| `DTC_ARCHIVO` | VARCHAR2 | YES |  |  |
| `CRF_ANIO` | NUMBER | YES |  |  |
| `CRF_PERIODO` | NUMBER | YES |  |  |
| `DTC_DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DTC_NUMERO_FINAN` | NUMBER | YES |  |  |
