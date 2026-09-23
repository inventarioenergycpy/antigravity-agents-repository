---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 55
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "DOC_COMPEN_GOB_SEGUNDA"
---

# 📋 DOC_COMPEN_GOB_SEGUNDA

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 55

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_FECHA_EMISION` | DATE | NO |  |  |
| `DOC_IMPORTE` | NUMBER | NO |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `DOC_SALDO` | NUMBER | NO |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `DOC_FECHA_VENC` | DATE | YES |  |  |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `DOC_FECHA_VENC_2` | DATE | YES |  |  |
| `DOC_FECHA_VENC_3` | DATE | YES |  |  |
| `DOC_FECHA_INTERESES` | DATE | YES |  |  |
| `DOC_RECARGO_VENC_2` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_3` | NUMBER | YES |  |  |
| `DOC_VENC_NRO` | VARCHAR2 | YES |  | Numero de vencimiento aplicado al documento, NO una fecha. Poblado en 13,6M de 14,09M facturas 2025. Correlaciona con cobranza: saldo promedio $150 cuando vale 1, contra $82.112 cuando viene NULL (468.868 docs) — el NULL marca al impago. Para mostrar la fecha usar DOC_FECHA_VENC_1. |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `DOC_SITUACION` | VARCHAR2 | YES |  | Situacion del documento de deuda en DETALLE_SALDO. El valor 'G' = en Gestion Judicial y tiene correlacion 1:1 con FECHA_PASE_GJ (los 158.883 documentos con pase a GJ tienen DOC_SITUACION='G'): es el indicador equivalente y mas simple de usar. NO existe estado de retorno: 157.751 siguen con saldo pendiente, 1.132 sin SALDO_ACTUAL y CERO saldados. |
| `DOC_ESTADO` | VARCHAR2 | NO |  | Estado del documento: 'D' = definitivo, el 100% de las facturas 2025. Su par DOC_SITUACION viene NULL salvo excepciones: 'G' gestión judicial (7.502 facturas 2025, $2.195M), 'M' (1.230), 'X' (98), 'I' (1). Ver también DOC_SITUACION en DETALLE_SALDO. |
