---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_EXT_DEC_CAMMESA_DETALLE"
---

# 🔧 XXCO_EXT_DEC_CAMMESA_DETALLE

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `RAZON_SOCIAL` | VARCHAR2 | YES |  |  |
| `CUIT` | NUMBER | YES |  |  |
| `TIPO_DOC` | VARCHAR2 | YES |  |  |
| `NRO_DOCUMENTO` | NUMBER | YES |  |  |
| `DIRECCION` | VARCHAR2 | YES |  |  |
| `CALLE` | VARCHAR2 | YES |  |  |
| `NRO` | NUMBER | YES |  |  |
| `PISO` | VARCHAR2 | YES |  |  |
| `DTO` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `ENERGIA_PICO` | NUMBER | YES |  |  |
| `ENERGIA_VALLE` | NUMBER | YES |  |  |
| `ENERGIA_RESTO` | NUMBER | YES |  |  |
| `ENERGIA` | NUMBER | YES |  |  |
| `ENERGIA_PICO_CS` | NUMBER | YES |  |  |
| `ENERGIA_VALLE_CS` | NUMBER | YES |  |  |
| `ENERGIA_RESTO_CS` | NUMBER | YES |  |  |
| `ENERGIA_CS` | NUMBER | YES |  |  |
| `ENERGIA_PICO_SS` | NUMBER | YES |  |  |
| `ENERGIA_VALLE_SS` | NUMBER | YES |  |  |
| `ENERGIA_RESTO_SS` | NUMBER | YES |  |  |
| `ENERGIA_SS` | NUMBER | YES |  |  |
| `MAX_DEM` | NUMBER | YES |  |  |
| `GUDI` | VARCHAR2 | YES |  |  |
| `COD_ACT` | VARCHAR2 | YES |  |  |
| `CUIT_AFIP` | NUMBER | YES |  |  |
| `PORC_SUBSIDIO` | NUMBER | YES |  |  |
| `COND_DEB_PRELIQ` | VARCHAR2 | YES |  |  |
