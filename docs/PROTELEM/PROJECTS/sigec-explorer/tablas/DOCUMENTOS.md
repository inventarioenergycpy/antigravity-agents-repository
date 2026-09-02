---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 468200117
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "DOCUMENTOS"
---

# 📋 DOCUMENTOS

> [!info] Significado de negocio
> FUENTE PRIMARIA de facturación (~468M filas, historia completa) y FUENTE ÚNICA para 'cuánto se le facturó a un cliente en un período': una fila = una factura, con importe, kWh y días del período TODOS en la cabecera. PK (DOC_TIPO, DOC_NUMERO). AUDITORIA_CAMMESA (la VM) es un SUBCONJUNTO de esta tabla (la declaración a CAMMESA). Importe = DOC_IMPORTE (total con impuestos) = DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO. kWh = DOC_CONSUMO. Días del período = DOC_FECHA_HASTA - DOC_FECHA_DESDE. OJO: DOC_ANIO/DOC_PERIODO es la ETIQUETA DEL CICLO, no el mes consumido (ver DOC_PERIODO). OJO: PRS_NUMERO EXISTE PERO ESTÁ VACÍA (2 filas pobladas de 14,09M facturas 2025) — al cliente se llega por CONTRATOS(SRV_CODIGO,CNT_NUMERO)→PERSONAS. Grano: 1 factura F por contrato-período en el 99,8% (30.285 contratos tuvieron 2 en 2025 por refacturación). NO tiene tarifa (usar CONTRATOS.TCL_CODIGO, actual). 468M filas → SIEMPRE filtrar (DOC_ANIO + DOC_TIPO). Para energía facturada DEFINITIVA: DOC_TIPO IN ('F','C','D') — C es nota de crédito (DOC_CONSUMO e importe POSITIVOS → NEGAR). NO incluir FP=FACTURA PROVISORIA (estimada, sin lectura): incluirla infla alumbrado ~+50% y comercial ~+5%. Tipos en TIPOS_COMPROBANTE.

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 468,200,117

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔗 → [[CONTRATOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔗 → [[CONTRATOS]] | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_GRUPO` | VARCHAR2 | NO |  | Circuito al que pertenece el documento en DOCUMENTOS. 'N' = normal, el de facturación de energía (14,09M de 14,10M docs en 2025). Los demás son circuitos aparte y no deben mezclarse: T (Factura Telec./comp. interno), O, L, C, G, A. Filtrar DOC_GRUPO='N' junto con DOC_TIPO='F'. |
| `DOC_TIPO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[PAGOS_TEMPRANOS]] |  |
| `DOC_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[PAGOS_TEMPRANOS]] |  |
| `DOC_FECHA_EMISION` | DATE | NO |  |  |
| `DOC_VENC_NRO` | VARCHAR2 | YES |  | Numero de vencimiento aplicado al documento, NO una fecha. Poblado en 13,6M de 14,09M facturas 2025. Correlaciona con cobranza: saldo promedio $150 cuando vale 1, contra $82.112 cuando viene NULL (468.868 docs) — el NULL marca al impago. Para mostrar la fecha usar DOC_FECHA_VENC_1. |
| `DOC_FECHA_VENC` | DATE | YES |  |  |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `DOC_FECHA_VENC_2` | DATE | YES |  |  |
| `DOC_FECHA_VENC_3` | DATE | YES |  |  |
| `DOC_FECHA_INTERESES` | DATE | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_FRECUENCIA` | NUMBER | YES |  | INSERVIBLE: 100% NULL en las 14,09M facturas de 2025. No sirve para distinguir facturación mensual de bimestral — deducirlo de DOC_FECHA_HASTA - DOC_FECHA_DESDE (mediana 30-31 días). |
| `DOC_CUOTA` | NUMBER | YES |  |  |
| `DOC_TIPO_ORIGEN` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_ORIGEN` | NUMBER | YES |  |  |
| `DOC_POTENCIA` | NUMBER | YES |  |  |
| `DOC_CONSUMO` | NUMBER | YES |  | Consumo facturado (kWh) en la cabecera de DOCUMENTOS: LA columna de kWh de una factura. Cubre la banda horaria completa — coincide con CONS_ENERGIA+PICO+VALLE+RESTO de la VM en 99,65% de las filas (revalidado 2026-08: 99,92% en el período 2025/6, y solo 0,56% de las facturas tiene banda horaria). En notas de crédito (DOC_TIPO='C') viene POSITIVO: negar para restar. Es la forma de obtener kWh cuando se usa DOCUMENTOS (la VM AUDITORIA_CAMMESA solo tiene 2022 desde dic-2022). Para kWh preferirla SIEMPRE sobre sumar ITEMS (que solo la reproduce en 81,5%). |
| `DOC_COS_FI` | NUMBER | YES |  |  |
| `DOC_IMPORTE` | NUMBER | NO |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `DOC_IMPORTE_BASICO` | NUMBER | YES |  | NO USAR como neto de la factura: coincide con DOC_IMPORTE_GRAVADO en solo el 70,6% y es MENOR en el 28,2% (muestra 322.120 docs de 2025). Poblada al 100% pero con semántica distinta al neto gravado. Para el neto usar DOC_IMPORTE_GRAVADO. |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | NO |  |  |
| `DOC_IMPORTE_PAGARE` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_2` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_3` | NUMBER | YES |  |  |
| `DOC_SALDO` | NUMBER | NO |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `TIN_CODIGO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_FINAN` | NUMBER | YES |  |  |
| `DOC_CON_CONTRATO` | VARCHAR2 | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES | 🔗 → [[PERSONAS]] | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `URC_CODIGO` | NUMBER | YES | 🔗 → [[UNIDADES_RECAUDADORAS]] |  |
| `ASI_NUMERO` | NUMBER | YES |  |  |
| `ORD_NUMERO` | NUMBER | YES |  |  |
| `TAB_NUMERO` | NUMBER | YES |  |  |
| `USR_NUMERO` | NUMBER | YES | 🔗 → [[USUARIOS]] |  |
| `DOC_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `DOC_SITUACION` | VARCHAR2 | YES |  | Situacion del documento de deuda en DETALLE_SALDO. El valor 'G' = en Gestion Judicial y tiene correlacion 1:1 con FECHA_PASE_GJ (los 158.883 documentos con pase a GJ tienen DOC_SITUACION='G'): es el indicador equivalente y mas simple de usar. NO existe estado de retorno: 157.751 siguen con saldo pendiente, 1.132 sin SALDO_ACTUAL y CERO saldados. |
| `DOC_ESTADO` | VARCHAR2 | NO |  | Estado del documento: 'D' = definitivo, el 100% de las facturas 2025. Su par DOC_SITUACION viene NULL salvo excepciones: 'G' gestión judicial (7.502 facturas 2025, $2.195M), 'M' (1.230), 'X' (98), 'I' (1). Ver también DOC_SITUACION en DETALLE_SALDO. |
| `DOC_IVV_CODIGO` | NUMBER | YES |  |  |
| `USR_NUMERO_AUTORIZADOR` | NUMBER | YES | 🔗 → [[USUARIOS]] |  |
| `DOC_CANT_CUOTAS` | NUMBER | YES |  |  |
| `DOC_SUB_TYPE` | VARCHAR2 | YES |  |  |
| `GDO_CODIGO` | VARCHAR2 | YES |  |  |
| `FPG_TRANSACCION` | NUMBER | YES |  |  |
| `DOC_PAGO_A_CUENTA` | VARCHAR2 | YES |  |  |
| `DOC_DIAS_VENC_1` | NUMBER | YES |  |  |
| `DOC_DIAS_VENC_2` | NUMBER | YES |  |  |
| `DOC_DIAS_VENC_3` | NUMBER | YES |  |  |
| `CTA_CODIGO` | VARCHAR2 | YES |  |  |
| `ASI_NUMERO_PERCEPCION` | NUMBER | YES |  |  |
| `DOC_PERCEPCION` | VARCHAR2 | YES |  | ES UN FLAG 'S'/NULL, NO UN IMPORTE, pese al nombre. 'S' en 13.657.099 de 14,09M facturas 2025. Sumarlo o compararlo como número tira ORA-01722 (invalid number). |
| `TRT_CODIGO` | NUMBER | YES |  |  |
| `TRT_NUMERO` | NUMBER | YES |  |  |
| `CPR_NUMERO_CL` | NUMBER | YES |  |  |
| `DOC_VUELTA_COBRANZA` | VARCHAR2 | YES |  |  |
| `DIF_NUMERO` | NUMBER | YES |  |  |
| `DOC_IMPORTE_EXENTO` | NUMBER | YES |  | OJO CON EL NOMBRE: no es 'exento de IVA', es el BLOQUE DE IMPUESTOS Y CARGOS de la factura. Verificado ítem por ítem: IVA Cons.Final (21%) + Ord.imp. municipal (9,90%) + Dto. 2298 (0,40%) + ERSeP Ley 10281 R.27 (0,10%) + Fdo.Des.Ene.Prov (10%) + redondeo. Con DOC_IMPORTE_GRAVADO suma DOC_IMPORTE. |
| `DOC_IMPORTE_GRAVADO` | NUMBER | YES |  | Neto de la factura ANTES de impuestos: energía (ítems EE1..EE4) + cargo fijo (CFI). Su par DOC_IMPORTE_EXENTO son los impuestos. GRAVADO + EXENTO = DOC_IMPORTE en el 99,27% de las facturas 2025. Es el neto correcto a usar; DOC_IMPORTE_BASICO NO lo es. |
| `DOC_LIBRO` | VARCHAR2 | YES |  |  |
| `DOC_LIBRO_IVA` | VARCHAR2 | YES |  |  |
| `DOC_CONDICION` | VARCHAR2 | YES |  |  |
| `DOC_POTENCIA_FACTURADA` | NUMBER | YES |  |  |
| `DOC_POTENCIA_AUTORIZADA` | NUMBER | YES |  |  |
| `DOC_FECHA_DESDE` | DATE | YES |  | Primer día del período facturado en DOCUMENTOS. Su par es DOC_FECHA_HASTA. Los períodos ENCADENAN: DOC_FECHA_DESDE = DOC_FECHA_HASTA de la factura anterior del mismo contrato en el 99,4% (89.267 de 89.819 comparables) — el día frontera se comparte, así que los días facturados son HASTA - DESDE, SIN +1. Poblada en el 99,94% de las facturas 2025. |
| `DOC_FECHA_HASTA` | DATE | YES |  | Último día del período facturado en DOCUMENTOS (día de la lectura de cierre). Días del período = DOC_FECHA_HASTA - DOC_FECHA_DESDE. Distribución 2025: 31 días 4,25M docs, 30 d 3,62M, 29 d 2,86M, 32 d 1,54M, 28 d 0,99M → ciclo mensual. Ninguna factura calza con el mes calendario: los cortes caen a mitad de mes. OJO AL MOSTRARLO AL CLIENTE: la boleta oficial de EPEC presenta el rango como DOC_FECHA_DESDE+1 .. DOC_FECHA_HASTA (corre el desde un día para no solapar con la factura anterior, que comparte ese día frontera). Verificado contra la API publica /api/documentos/a-pagar: su campo 'hasta' = DOC_FECHA_HASTA exacto y su 'desde' = DOC_FECHA_DESDE+1. La cantidad de días no cambia: sigue siendo HASTA-DESDE. |
| `MPA_TIPO` | VARCHAR2 | YES |  |  |
| `CNT_NUMERO_CUENTA` | VARCHAR2 | YES |  | NO es el número de contrato/cuenta comercial. Es el número de CUENTA BANCARIA o TARJETA para débito automático (VARCHAR2: 16 dígitos = tarjeta, 22 = CBU). Solo 122.016 de 3,74M filas de CONTRATOS lo tienen poblado (3,2%) y viene NULL en la mayoría de los suministros. En DOCUMENTOS también viene NULL. El identificador comercial es la PK (SRV_CODIGO, CNT_NUMERO). |
| `DOC_FECHA_CALCULO` | DATE | YES |  |  |
| `URC_CODIGO_DEPOSITO` | NUMBER | YES |  |  |
| `CPR_NUMERO_DEBITO` | NUMBER | YES |  |  |
| `DOC_COD_COMENTARIO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `AGE_CODIGO` | VARCHAR2 | YES |  |  |
| `DOC_MENSAJE` | VARCHAR2 | YES |  |  |
| `DOC_COBRO_INCOBRABLE` | VARCHAR2 | YES |  |  |
| `DOC_FECHA_PAGO` | DATE | YES |  |  |
| `DOC_EXPEDIENTE` | VARCHAR2 | YES |  |  |
| `CODE_COMBINATION_ID` | NUMBER | YES |  |  |
| `ASI_NUMERO_PRESUPUESTARIO` | NUMBER | YES |  |  |
| `CPR_NUMERO_INTERFASE_CE` | NUMBER | YES |  |  |
| `PROJECT_NUMBER` | NUMBER | YES |  |  |
| `DOC_ENVIADO_CORREO` | DATE | YES |  |  |
| `DOC_BASE_IB` | NUMBER | YES |  |  |
| `CIB_CODIGO` | NUMBER | YES |  |  |
| `DOC_TIPO_INT` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_INT` | NUMBER | YES |  |  |
| `DOC_DEMANDA_PICO_FACTURADA` | NUMBER | YES |  |  |
| `DOC_DEMANDA_PICO_CONTRATADA` | NUMBER | YES |  |  |
| `DOC_DEMANDA_FUERA_FACTURADA` | NUMBER | YES |  |  |
| `DOC_DEMANDA_FUERA_CONTRATADA` | NUMBER | YES |  |  |
| `DOC_BASE_OIM` | NUMBER | YES |  |  |
| `DOC_COSTO_COMPRA_MEM` | NUMBER | YES |  |  |
| `DOC_VAD` | NUMBER | YES |  |  |
| `DOC_FECHA_EMISION_COMPLETA` | DATE | YES |  |  |
| `TCE_CODIGO` | VARCHAR2 | YES |  |  |
| `IVV_TIPO_FORMULARIO` | VARCHAR2 | YES |  |  |
| `TCE_PUNTO_VENTA` | NUMBER | YES |  |  |
| `TCE_NUMERO` | NUMBER | YES |  |  |
| `TCE_NUMERO_CAE` | VARCHAR2 | YES |  |  |
| `TCE_FECHA_VENC_CAE` | DATE | YES |  |  |
| `DOC_ENVIADO_ENTE` | DATE | YES |  |  |
| `DOC_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
| `DOC_NUMERO_BIMESTRE` | NUMBER | YES |  |  |
| `DOC_ANIO_BIMESTRE` | NUMBER | YES |  |  |
| `DOC_NRO_LIQUIDACION` | NUMBER | YES |  |  |
| `CODIGO_MODELO_IMPRESION_XML` | VARCHAR2 | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **DOC_ABONADO_EN**: `URC_CODIGO` → [[UNIDADES_RECAUDADORAS]] (`URC_CODIGO`)
- **DOC_AUTORIZADO_POR**: `USR_NUMERO_AUTORIZADOR` → [[USUARIOS]] (`USR_NUMERO`)
- **DOC_FK_CNT**: `SRV_CODIGO`, `CNT_NUMERO` → [[CONTRATOS]] (`SRV_CODIGO`, `CNT_NUMERO`)
- **DOC_FK_PRS**: `PRS_NUMERO` → [[PERSONAS]] (`PRS_NUMERO`)
- **DOC_GENERADO_POR**: `USR_NUMERO` → [[USUARIOS]] (`USR_NUMERO`)
- **DOC_REGISTRADO_EN**: `DOC_TIPO`, `DOC_NUMERO` → [[PAGOS_TEMPRANOS]] (`DOC_TIPO`, `DOC_NUMERO`)

## FK inferidas (alta confianza)

- `TCE_PUNTO_VENTA` → [[XXCO_TIPOS_COMP_ELECTRONICO]] _TCE_PUNTO_VENTA es PK de XXCO_TIPOS_COMP_ELECTRONICO_
- `AGE_CODIGO` → [[AGENCIAS]] _AGE_CODIGO es PK de AGENCIAS_
- `DIF_NUMERO` → [[DIFERENCIAS]] _DIF_NUMERO es PK de DIFERENCIAS_
- `GDO_CODIGO` → [[GRUPOS_DOCUMENTO]] _GDO_CODIGO es PK de GRUPOS_DOCUMENTO_
- `TCE_CODIGO` → [[XXCO_TIPOS_COMP_ELECTRONICO]] _TCE_CODIGO es PK de XXCO_TIPOS_COMP_ELECTRONICO_
