---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 4996
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_DOC_CORREO_XML"
---

# 🔧 XXCO_DOC_CORREO_XML

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 4,996

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_NRO` | NUMBER | NO | 🔑 PK |  |
| `TIPO_FACT` | VARCHAR2 | YES |  |  |
| `TIPO_TEMPLATE` | VARCHAR2 | YES |  |  |
| `DISTRIBUYE_EPEC` | VARCHAR2 | YES |  |  |
| `TIPO_ENVIO` | NUMBER | YES |  |  |
| `TIENE_SUBSIDIO` | VARCHAR2 | YES |  |  |
| `NRO_GUION` | VARCHAR2 | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | VARCHAR2 | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | VARCHAR2 | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PRS_CUIT` | NUMBER | YES |  |  |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `CNT_CALLE_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_DIRECCION_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_C_POSTAL_PAGO` | NUMBER | YES |  |  |
| `SRV_CALLE` | VARCHAR2 | YES |  |  |
| `SRV_DIRECCION` | VARCHAR2 | YES |  |  |
| `SRV_C_POSTAL` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO_SRV` | NUMBER | YES |  |  |
| `SCF_DESCRIPCION_SRV` | VARCHAR2 | YES |  |  |
| `SCF_TELEFONO` | VARCHAR2 | YES |  |  |
| `AGF_NOMBRE` | VARCHAR2 | YES |  |  |
| `TCL_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `IVV_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `CIB_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `PRS_INSCRIPCION_IB` | VARCHAR2 | YES |  |  |
| `DOC_FECHA_EMISION` | VARCHAR2 | YES |  |  |
| `DOC_FECHA_VENC_1` | VARCHAR2 | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `DOC_FECHA_VENC_2` | VARCHAR2 | YES |  |  |
| `DOC_FECHA_VENC_3` | VARCHAR2 | YES |  |  |
| `DOC_ANIO` | VARCHAR2 | YES |  |  |
| `DOC_PERIODO` | VARCHAR2 | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_IMPORTE` | VARCHAR2 | YES |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `DOC_IMPORTE_ORIGINAL` | VARCHAR2 | YES |  |  |
| `DOC_SALDO` | VARCHAR2 | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `DOC_RECARGO_VENC_2` | VARCHAR2 | YES |  |  |
| `DOC_VENCIMIENTO_2` | VARCHAR2 | YES |  |  |
| `DOC_IMP_BASICO_REC_2` | VARCHAR2 | YES |  |  |
| `DOC_IVA_REC_2` | VARCHAR2 | YES |  |  |
| `DOC_IVA_ADIC_REC_2` | VARCHAR2 | YES |  |  |
| `DOC_IVA_PERC_REC_2` | VARCHAR2 | YES |  |  |
| `DOC_IMPUESTO_REC_2` | VARCHAR2 | YES |  |  |
| `DOC_REDONDEO_REC_2` | VARCHAR2 | YES |  |  |
| `DOC_RECARGO_VENC_3` | VARCHAR2 | YES |  |  |
| `DOC_VENCIMIENTO_3` | VARCHAR2 | YES |  |  |
| `DOC_IMP_BASICO_REC_3` | VARCHAR2 | YES |  |  |
| `DOC_IVA_REC_3` | VARCHAR2 | YES |  |  |
| `DOC_IVA_ADIC_REC_3` | VARCHAR2 | YES |  |  |
| `DOC_IVA_PERC_REC_3` | VARCHAR2 | YES |  |  |
| `DOC_IMPUESTO_REC_3` | VARCHAR2 | YES |  |  |
| `DOC_REDONDEO_REC_3` | VARCHAR2 | YES |  |  |
| `MPA_TIPO_MEDIO_PAGO` | VARCHAR2 | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `SRV_ORDEN_LECTURA` | NUMBER | YES |  |  |
| `DOC_COSENO_FI` | VARCHAR2 | YES |  |  |
| `DOC_FECHA_LECTURA_MIN` | VARCHAR2 | YES |  |  |
| `DOC_FECHA_LECTURA_MAX` | VARCHAR2 | YES |  |  |
| `DOC_PROXIMO_VENCIMIENTO` | VARCHAR2 | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `TEN_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `DOC_DEMANDA_PICO_FACTURADA` | VARCHAR2 | YES |  |  |
| `DOC_DEMANDA_PICO_CONTRATADA` | VARCHAR2 | YES |  |  |
| `DOC_DEMANDA_FUERA_FACTURADA` | VARCHAR2 | YES |  |  |
| `DOC_DEMANDA_FUERA_CONTRATADA` | VARCHAR2 | YES |  |  |
| `IVV_TIPO_FORMULARIO` | VARCHAR2 | YES |  |  |
| `TCE_NUMERO_COMPLETO` | VARCHAR2 | YES |  |  |
| `CESP_NUMERO` | VARCHAR2 | YES |  |  |
| `CESP_FECHA_VENC` | VARCHAR2 | YES |  |  |
| `CODIGO_BARRA` | VARCHAR2 | YES |  |  |
| `ITE_LIST` | ITELIST_T | YES |  |  |
| `ITERES_LIST` | ITERESLIST_T | YES |  |  |
| `CONS_LIST` | CONSLIST_T | YES |  |  |
| `LECT_LIST` | LECTLIST_T | YES |  |  |
| `DESC_SUBS_LIST` | DESSUBSLIST_T | YES |  |  |
| `MSJ_LIST` | MSJLIST_T | YES |  |  |

## FK inferidas (alta confianza)

- `MPA_TIPO_MEDIO_PAGO` → [[MEDIOS_PAGO]] _MPA_TIPO_MEDIO_PAGO es PK de MEDIOS_PAGO_
