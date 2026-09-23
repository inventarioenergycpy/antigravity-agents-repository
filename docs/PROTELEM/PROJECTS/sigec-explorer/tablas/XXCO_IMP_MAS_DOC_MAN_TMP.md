---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: documentos
num_rows: 356847
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_IMP_MAS_DOC_MAN_TMP"
---

# ⏱️ XXCO_IMP_MAS_DOC_MAN_TMP

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 356,847

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `MDM_ESTADO` | VARCHAR2 | NO |  |  |
| `MDM_FECHA_GENERADO` | DATE | NO |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `MDM_FECHA_PROCESADO` | DATE | YES |  |  |
| `DOC_FECHA_EMISION` | DATE | YES |  |  |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `DOC_FECHA_VENC_2` | DATE | YES |  |  |
| `DOC_FECHA_VENC_3` | DATE | YES |  |  |
| `DOC_IMPORTE` | NUMBER | YES |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `MDM_DISCRIMINA_IVA` | VARCHAR2 | YES |  |  |
| `CNT_IVV_CODIGO` | NUMBER | YES |  |  |
| `USR_NUMERO_CANCELA` | NUMBER | YES |  |  |
| `DOC_SALDO` | NUMBER | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `MDM_DATOS_CANCELA` | VARCHAR2 | YES |  |  |
| `MDM_IMPRIME_SIN_SALDO` | VARCHAR2 | YES |  |  |
| `PERIODO` | NUMBER | YES |  |  |
