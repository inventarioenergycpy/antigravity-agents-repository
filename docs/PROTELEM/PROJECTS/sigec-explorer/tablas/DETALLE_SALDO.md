---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 5130753
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "DETALLE_SALDO"
---

# 📋 DETALLE_SALDO

> [!info] Significado de negocio
> Detalle de saldo por documento de deuda (5,19M filas). Contiene FECHA_PASE_GJ (pase a gestion judicial), LA frontera de SIGEC con Legales: 158.883 documentos, 1997-10-28 a hoy, todos con DOC_SITUACION='G'. Saldo total en gestion judicial: $7.447M original / $7.267M actual, sin ningun documento saldado (el resultado del juicio no vuelve a SIGEC). Tambien SALDO_ACTUAL, PUNITORIOS, DOC_SITUACION.

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 5,130,753

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_ESTADO` | VARCHAR2 | NO |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `ZON_CODIGO` | VARCHAR2 | NO |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `DOC_GRUPO` | VARCHAR2 | NO |  | Circuito al que pertenece el documento en DOCUMENTOS. 'N' = normal, el de facturación de energía (14,09M de 14,10M docs en 2025). Los demás son circuitos aparte y no deben mezclarse: T (Factura Telec./comp. interno), O, L, C, G, A. Filtrar DOC_GRUPO='N' junto con DOC_TIPO='F'. |
| `DOC_SITUACION` | VARCHAR2 | YES |  | Situacion del documento de deuda en DETALLE_SALDO. El valor 'G' = en Gestion Judicial y tiene correlacion 1:1 con FECHA_PASE_GJ (los 158.883 documentos con pase a GJ tienen DOC_SITUACION='G'): es el indicador equivalente y mas simple de usar. NO existe estado de retorno: 157.751 siguen con saldo pendiente, 1.132 sin SALDO_ACTUAL y CERO saldados. |
| `TAB_NUMERO` | NUMBER | YES |  |  |
| `MPA_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_FECHA_EMISION` | DATE | NO |  |  |
| `DOC_FECHA_VENC` | DATE | YES |  |  |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `DOC_FECHA_VENC_2` | DATE | YES |  |  |
| `DOC_FECHA_VENC_3` | DATE | YES |  |  |
| `DOC_FECHA_CALCULO` | DATE | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_VENC_NRO` | VARCHAR2 | YES |  | Numero de vencimiento aplicado al documento, NO una fecha. Poblado en 13,6M de 14,09M facturas 2025. Correlaciona con cobranza: saldo promedio $150 cuando vale 1, contra $82.112 cuando viene NULL (468.868 docs) — el NULL marca al impago. Para mostrar la fecha usar DOC_FECHA_VENC_1. |
| `DOC_RECARGO_VENC_2` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_3` | NUMBER | YES |  |  |
| `DOC_FECHA_INTERESES` | DATE | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `TFA_CODIGO` | VARCHAR2 | NO |  |  |
| `CTA_CODIGO` | VARCHAR2 | YES |  |  |
| `DOC_IMPORTE` | NUMBER | NO |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `DOC_IMPORTE_BASICO` | NUMBER | YES |  | NO USAR como neto de la factura: coincide con DOC_IMPORTE_GRAVADO en solo el 70,6% y es MENOR en el 28,2% (muestra 322.120 docs de 2025). Poblada al 100% pero con semántica distinta al neto gravado. Para el neto usar DOC_IMPORTE_GRAVADO. |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | NO |  |  |
| `DOC_SALDO` | NUMBER | NO |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `DOC_NUMERO_FINAN` | NUMBER | YES |  |  |
| `CODE_COMBINATION_ID` | NUMBER | YES |  |  |
| `TRT_NUMERO` | NUMBER | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `IVV_CODIGO` | NUMBER | NO |  |  |
| `IMP_CODIGO` | NUMBER | NO |  |  |
| `OIM_TIPO` | VARCHAR2 | NO |  |  |
| `AGF_CODIGO_OIM` | NUMBER | NO |  |  |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `AGF_CODIGO` | NUMBER | NO |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `SRV_ESTADO` | VARCHAR2 | NO |  |  |
| `TCE_PUNTO_VENTA` | NUMBER | YES |  |  |
| `TCE_NUMERO` | NUMBER | YES |  |  |
| `ASI_NUMERO` | NUMBER | YES |  |  |
| `PRS_NUMERO_CNT` | NUMBER | NO |  |  |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
| `TIN_CODIGO` | VARCHAR2 | YES |  |  |
| `DOC_IVV_CODIGO` | NUMBER | YES |  |  |
| `IVV_TIPO_FORMULARIO` | VARCHAR2 | YES |  |  |
| `SALDO_ACTUAL` | NUMBER | YES |  |  |
| `PUNITORIOS` | NUMBER | YES |  |  |
| `IMP_PUNITORIOS` | NUMBER | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `FECHA_PASE_GJ` | DATE | YES |  | GJ = Gestion Judicial. Fecha en que un documento de deuda pasa a cobro judicial (DETALLE_SALDO, col. 57). ES LA FRONTERA de SIGEC con Legales: 158.883 de 5,19M documentos, 1997-10-28 a hoy, vivo y creciente ($4.548M en 2025, 22.497 docs, 1.805 suministros). |

## FK inferidas (alta confianza)

- `TCE_PUNTO_VENTA` → [[XXCO_TIPOS_COMP_ELECTRONICO]] _TCE_PUNTO_VENTA es PK de XXCO_TIPOS_COMP_ELECTRONICO_
- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
