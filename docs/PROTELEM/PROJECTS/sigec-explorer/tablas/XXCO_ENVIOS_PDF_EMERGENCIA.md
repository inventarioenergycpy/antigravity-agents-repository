---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 550197
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_ENVIOS_PDF_EMERGENCIA"
---

# 🔧 XXCO_ENVIOS_PDF_EMERGENCIA

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 550,197

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SERVICIO_ID` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `DOC_IMPORTE` | NUMBER | YES |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `DOC_FECHA_VENC` | DATE | YES |  |  |
| `DOC_TIPO_CANCELA` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_CANCELA` | NUMBER | YES |  |  |
| `DOC_FECHA_EMISION_CANCELA` | DATE | YES |  |  |
| `EOV_DOC_NUMERO_ENCRIPTADO` | VARCHAR2 | YES |  |  |
| `EOV_ESTADO` | VARCHAR2 | YES |  |  |
| `EOV_FECHA_ENVIO` | DATE | YES |  |  |
| `EOV_ERROR` | VARCHAR2 | YES |  |  |
| `USU_ID` | NUMBER | YES |  |  |
| `EOV_INTENTOS` | NUMBER | YES |  |  |
| `REQUEST_ID` | NUMBER | YES |  |  |
| `EOV_PLANTILLA_HTML` | VARCHAR2 | YES |  |  |
| `EOV_ERROR_MENSAJE` | VARCHAR2 | YES |  |  |
| `EOV_FECHA_PROCESAMIENTO` | DATE | YES |  |  |
| `EOV_NUMERO_RECORDATORIO` | NUMBER | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `REQUEST_ID` → [[TRANSFERENCIAS_PENDIENTES]] _REQUEST_ID es PK de TRANSFERENCIAS_PENDIENTES_
