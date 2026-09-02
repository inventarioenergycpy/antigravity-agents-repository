---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 4623
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_CALCULO_RECIBO_WEB"
---

# 🔧 XXCO_CALCULO_RECIBO_WEB

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 4,623

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_ID` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `DOC_VENC_NRO` | VARCHAR2 | YES |  | Numero de vencimiento aplicado al documento, NO una fecha. Poblado en 13,6M de 14,09M facturas 2025. Correlaciona con cobranza: saldo promedio $150 cuando vale 1, contra $82.112 cuando viene NULL (468.868 docs) — el NULL marca al impago. Para mostrar la fecha usar DOC_FECHA_VENC_1. |
| `DOC_FECHA_VENC` | DATE | YES |  |  |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `DOC_FECHA_VENC_ACT` | DATE | YES |  |  |
| `DOC_SALDO_ACTUAL` | NUMBER | YES |  |  |
| `DOC_INTERESES` | NUMBER | YES |  |  |
| `DOC_IMPUESTOS_INTERESES` | NUMBER | YES |  |  |
| `DOC_IMPUESTOS_MAS_INTERESES` | NUMBER | YES |  |  |
| `DOC_INTIMADO` | VARCHAR2 | YES |  |  |
| `DOC_ETAPA_ORDENATIVO` | VARCHAR2 | YES |  |  |
| `TRT_NUMERO` | NUMBER | YES |  |  |
| `DOC_RECONEXION` | NUMBER | YES |  |  |
| `DOC_TIT_RECONEXION` | VARCHAR2 | YES |  |  |
| `DOC_IMPUESTOS_RECONEXION` | NUMBER | YES |  |  |
| `DOC_IMPUESTOS_MAS_RECONEXION` | NUMBER | YES |  |  |
| `DOC_SITUACION` | VARCHAR2 | YES |  | Situacion del documento de deuda en DETALLE_SALDO. El valor 'G' = en Gestion Judicial y tiene correlacion 1:1 con FECHA_PASE_GJ (los 158.883 documentos con pase a GJ tienen DOC_SITUACION='G'): es el indicador equivalente y mas simple de usar. NO existe estado de retorno: 157.751 siguen con saldo pendiente, 1.132 sin SALDO_ACTUAL y CERO saldados. |
| `DOC_FECHA_INTERESES` | DATE | YES |  |  |
| `DOC_FECHA_VENC_2` | DATE | YES |  |  |
| `DOC_FECHA_VENC_3` | DATE | YES |  |  |
| `DOC_FECHA_EMISION` | DATE | YES |  |  |
| `DOC_IMPORTE` | NUMBER | YES |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `DOC_SALDO` | NUMBER | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `DOC_RECARGO_VENC_2` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_3` | NUMBER | YES |  |  |
