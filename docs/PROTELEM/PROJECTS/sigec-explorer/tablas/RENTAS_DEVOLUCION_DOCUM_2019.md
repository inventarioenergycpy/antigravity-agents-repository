---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 150910
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "RENTAS_DEVOLUCION_DOCUM_2019"
---

# 📋 RENTAS_DEVOLUCION_DOCUM_2019

**Filas estimadas:** 150,910

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TIPO_DNI` | VARCHAR2 | YES |  |  |
| `NRO_DNI` | VARCHAR2 | YES |  |  |
| `RAZON_SOCIAL` | VARCHAR2 | YES |  |  |
| `CONTRATO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | VARCHAR2 | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | VARCHAR2 | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `NRO_FACTURA` | VARCHAR2 | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | VARCHAR2 | YES |  |  |
| `FECHA_ALTA` | VARCHAR2 | YES |  |  |
| `PERIODO` | VARCHAR2 | YES |  |  |
| `VTO_ORIGINAL` | VARCHAR2 | YES |  |  |
| `CAPITAL_FACTURA` | VARCHAR2 | YES |  |  |
