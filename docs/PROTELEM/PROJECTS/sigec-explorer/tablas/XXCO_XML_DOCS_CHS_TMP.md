---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: documentos
num_rows: 4
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_XML_DOCS_CHS_TMP"
---

# ⏱️ XXCO_XML_DOCS_CHS_TMP

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 4

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `DOC_NRO_GUION` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PRS_CUIT` | NUMBER | YES |  |  |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | NO |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `TEN_CODIGO` | VARCHAR2 | NO |  |  |
| `CNT_CALLE_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_DIRECCION_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_C_POSTAL_PAGO` | NUMBER | YES |  |  |
| `TFA_CODIGO` | VARCHAR2 | NO |  |  |
| `SRV_CALLE_PAGO` | VARCHAR2 | YES |  |  |
| `SRV_DIRECCION` | VARCHAR2 | YES |  |  |
| `SRV_C_POSTAL` | NUMBER | YES |  |  |
| `SCF_CODIGO_SRV` | NUMBER | NO |  |  |
| `SCF_DESCRIPCION_SRV` | VARCHAR2 | NO |  |  |
| `SCF_C_POSTAL_SRV` | NUMBER | YES |  |  |
| `SCF_FAX_SRV` | VARCHAR2 | YES |  |  |
| `SCF_TELEFONO_SRV` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO_DOC` | NUMBER | NO |  |  |
| `SCF_DESCRIPCION_DOC` | VARCHAR2 | NO |  |  |
| `SCF_C_POSTAL_DOC` | NUMBER | YES |  |  |
| `SCF_FAX_DOC` | VARCHAR2 | YES |  |  |
| `SCF_TELEFONO_DOC` | VARCHAR2 | YES |  |  |
| `AGF_NOMBRE` | VARCHAR2 | NO |  |  |
| `TCL_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `IVV_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `CIB_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `PRS_INSCRIPCION_IB` | NUMBER | YES |  |  |
| `DOC_FECHA_EMISION` | DATE | NO |  |  |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `DOC_FECHA_VENC_2` | DATE | YES |  |  |
| `DOC_FECHA_VENC_3` | DATE | YES |  |  |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_PERIODO_DOC_ANIO` | VARCHAR2 | YES |  |  |
| `DOC_IMPORTE` | NUMBER | NO |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `DOC_RECARGO_VENC_2` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_3` | NUMBER | YES |  |  |
| `MPA_TIPO_MEDIO_PAGO` | VARCHAR2 | YES |  |  |
| `DOC_COS_FI` | NUMBER | YES |  |  |
| `DOC_DEMANDA_PICO_FACTURADA` | NUMBER | YES |  |  |
| `DOC_DEMANDA_PICO_CONTRATADA` | NUMBER | YES |  |  |
| `DOC_DEMANDA_FUERA_FACTURADA` | NUMBER | YES |  |  |
| `DOC_DEMANDA_FUERA_CONTRATADA` | NUMBER | YES |  |  |
| `VENCIMIENTO_2` | VARCHAR2 | YES |  |  |
| `VENCIMIENTO_3` | VARCHAR2 | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | NO |  |  |
| `RTA_CODIGO` | NUMBER | NO |  |  |
| `TEN_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `CAT_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `CAT_CODIGO` | VARCHAR2 | NO |  |  |
| `IVV_DISCRIMINA` | VARCHAR2 | NO |  |  |
| `DOC_IVV_CODIGO` | NUMBER | YES |  |  |
| `CNT_IVV_CODIGO` | NUMBER | NO |  |  |
| `FECHA_LECTURA_MIN` | DATE | YES |  |  |
| `FECHA_LECTURA_MAX` | DATE | YES |  |  |
| `PROXIMO_VTO` | VARCHAR2 | YES |  |  |
| `TAB_NUMERO` | NUMBER | YES |  |  |
| `DOC_SALDO` | NUMBER | NO |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `SRV_CODIGO_CHAR` | VARCHAR2 | YES |  |  |
| `CNT_NUMERO_CHAR` | VARCHAR2 | YES |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | NO |  |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `SRV_ORDEN_LECTURA` | NUMBER | YES |  |  |
| `CNT_NUMERO_CUENTA` | VARCHAR2 | YES |  | NO es el número de contrato/cuenta comercial. Es el número de CUENTA BANCARIA o TARJETA para débito automático (VARCHAR2: 16 dígitos = tarjeta, 22 = CBU). Solo 122.016 de 3,74M filas de CONTRATOS lo tienen poblado (3,2%) y viene NULL en la mayoría de los suministros. En DOCUMENTOS también viene NULL. El identificador comercial es la PK (SRV_CODIGO, CNT_NUMERO). |
| `MPA_IMPRIME_CODIGO_BARRA` | VARCHAR2 | YES |  |  |
| `CRF_ANIO` | NUMBER | NO |  |  |
| `CRF_PERIODO` | NUMBER | NO |  |  |

## FK inferidas (alta confianza)

- `MPA_TIPO_MEDIO_PAGO` → [[MEDIOS_PAGO]] _MPA_TIPO_MEDIO_PAGO es PK de MEDIOS_PAGO_
