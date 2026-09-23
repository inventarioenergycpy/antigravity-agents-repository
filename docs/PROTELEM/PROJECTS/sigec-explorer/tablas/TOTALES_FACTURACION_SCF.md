---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "TOTALES_FACTURACION_SCF"
---

# 📋 TOTALES_FACTURACION_SCF

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `DOC_IMPORTE` | NUMBER | YES |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `DOC_SALDO` | NUMBER | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `TFS_FECHA` | DATE | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_ANIO` | NUMBER | YES |  |  |
