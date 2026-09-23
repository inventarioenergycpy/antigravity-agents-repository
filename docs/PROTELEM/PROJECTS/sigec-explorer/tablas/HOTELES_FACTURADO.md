---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: contratos
num_rows: 11796
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/contratos
  - documentada/negocio
aliases:
  - "HOTELES_FACTURADO"
---

# 📋 HOTELES_FACTURADO

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 11,796

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CUIT` | NUMBER | YES |  |  |
| `RAZON_SOCIAL` | VARCHAR2 | YES |  |  |
| `NRO_CLIENTE` | NUMBER | NO |  | Número de cliente en tablas EXT_VKO_* (integración externa). |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `LOCALIDAD` | VARCHAR2 | NO |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_FECHA_INICIO` | DATE | NO |  |  |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `FECHA_EMISION` | DATE | YES |  |  |
| `PERIODO` | NUMBER | YES |  |  |
| `ANIO` | NUMBER | YES |  |  |
| `CONSU` | NUMBER | YES |  |  |
| `TCL_CODIGO_GRAL` | VARCHAR2 | YES |  | Código de tarifa 'general' en AUDITORIA_CAMMESA. Se une a TARIFAS.TCL_CODIGO para clasificar el consumo por sector/rubro (vía TARIFAS.TCL_GRUPO). |
| `CLA_CODIGO_GRAL` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO_GRAL` | VARCHAR2 | YES |  |  |
| `IMPOR_BASICO` | NUMBER | YES |  |  |
| `IMPOR_COS_FI` | NUMBER | YES |  |  |
| `IMPUESTO_NAC` | NUMBER | YES |  |  |
| `IMPUESTO_IVA` | NUMBER | YES |  |  |
| `IMPUESTO_DGI` | NUMBER | YES |  |  |
| `IMPUESTO_PROV` | NUMBER | YES |  |  |
| `IMPUESTO_MUNIC` | NUMBER | YES |  |  |
| `IMPOR_TOTAL` | NUMBER | YES |  |  |
| `CALLE_NRO` | VARCHAR2 | YES |  |  |
| `DIRECCION` | VARCHAR2 | YES |  |  |
