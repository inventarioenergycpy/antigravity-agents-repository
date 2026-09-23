---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 9057670
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "SALDOS_CONTABLE_CATEG"
---

# 📋 SALDOS_CONTABLE_CATEG

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 9,057,670

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `DOC_FECHA_EMISION` | DATE | YES |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `DOC_SALDO` | NUMBER | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `SEGMENT_4_CLASE` | VARCHAR2 | YES |  |  |
| `SEGMENT_3_DISTRITO` | VARCHAR2 | YES |  |  |
| `SEGMENT_4_CUENTA` | VARCHAR2 | YES |  |  |
| `SCC_CODIGO` | NUMBER | YES |  |  |
| `CNT_CALLE_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_NRO_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_PISO_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_DEPTO_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_DIRECCION_PAGO` | VARCHAR2 | YES |  |  |
| `LOCALIDAD` | VARCHAR2 | YES |  |  |
