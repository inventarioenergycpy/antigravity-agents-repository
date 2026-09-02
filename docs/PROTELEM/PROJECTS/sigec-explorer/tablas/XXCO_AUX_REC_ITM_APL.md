---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_AUX_REC_ITM_APL"
---

# 🔧 XXCO_AUX_REC_ITM_APL

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `DOC_FECHA_EMISION` | VARCHAR2 | YES |  |  |
| `DOC_FECHA_VENC` | VARCHAR2 | YES |  |  |
| `DOC_IVV_CODIGO` | NUMBER | YES |  |  |
| `DOC_SALDO` | NUMBER | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `DOC_RECARGO_VENC_2` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_3` | NUMBER | YES |  |  |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | VARCHAR2 | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `APL_IMPORTE` | NUMBER | YES |  |  |
| `APL_VENC_NRO` | NUMBER | YES |  |  |
| `APL_FECHA` | VARCHAR2 | YES |  |  |
| `DOC_TIPO_DOC` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_DOC` | NUMBER | YES |  |  |
| `DOC_MENSAJE` | VARCHAR2 | YES |  |  |
