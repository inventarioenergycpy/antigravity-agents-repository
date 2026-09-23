---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 37236
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "EMPLE_A_REFACTURAR_DOC"
---

# 📋 EMPLE_A_REFACTURAR_DOC

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 37,236

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | NO |  |  |
| `DOC_SALDO` | NUMBER | NO |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_FECHA_EMISION` | DATE | NO |  |  |
| `TAR` | VARCHAR2 | NO |  |  |
| `CLA` | VARCHAR2 | NO |  |  |
| `TAB_NUMERO` | NUMBER | YES |  |  |
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `PAGADO_VIE` | VARCHAR2 | YES |  |  |
| `CANT_FACTU` | NUMBER | YES |  |  |
| `NRO_ORDEN_REFAC` | NUMBER | YES |  |  |
| `FACT_PENDIENTE` | VARCHAR2 | YES |  |  |
| `CNT_CADUCO_ALGUN_PAGO` | VARCHAR2 | YES |  |  |
| `COD_PAGO` | VARCHAR2 | YES |  |  |
| `COD_SITUACION` | VARCHAR2 | YES |  |  |
| `IMPORTE_APLICADO` | NUMBER | YES |  |  |
