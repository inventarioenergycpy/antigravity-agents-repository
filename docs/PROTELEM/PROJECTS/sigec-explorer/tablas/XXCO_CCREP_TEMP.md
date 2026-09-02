---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: documentos
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_CCREP_TEMP"
---

# ⏱️ XXCO_CCREP_TEMP

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_FECHA_EMISION` | VARCHAR2 | YES |  |  |
| `DOC_VENC_NRO` | NUMBER | YES |  | Numero de vencimiento aplicado al documento, NO una fecha. Poblado en 13,6M de 14,09M facturas 2025. Correlaciona con cobranza: saldo promedio $150 cuando vale 1, contra $82.112 cuando viene NULL (468.868 docs) — el NULL marca al impago. Para mostrar la fecha usar DOC_FECHA_VENC_1. |
| `DOC_FECHA_VENC` | VARCHAR2 | YES |  |  |
| `DOC_IMPORTE` | NUMBER | YES |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `DOC_IMPORTE_DEBE` | NUMBER | YES |  |  |
| `DOC_IMPORTE_HABER` | NUMBER | YES |  |  |
| `SALDO_CC` | NUMBER | YES |  |  |
