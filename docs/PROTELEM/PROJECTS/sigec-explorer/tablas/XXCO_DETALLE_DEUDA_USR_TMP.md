---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: documentos
num_rows: 41987
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_DETALLE_DEUDA_USR_TMP"
---

# ⏱️ XXCO_DETALLE_DEUDA_USR_TMP

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 41,987

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRS_RAZON_SOCIAL` | VARCHAR2 | NO |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_ESTADO` | VARCHAR2 | NO |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `TMI_CODIGO` | VARCHAR2 | YES |  | Tipo de ente (PK de TIPOS_ENTE, en ENTES): 1 Nacional, 2 Provincial, 3 Municipal, 4 Cooperativas, 5 Particulares, 6 Prov. No Autárq., 7 EPEC, 8 Barrios. Se guarda como VARCHAR ('1'...'8'). |
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `MIN_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `ZON_CODIGO` | VARCHAR2 | NO |  |  |
| `SCF_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_SITUACION` | VARCHAR2 | YES |  | Situacion del documento de deuda en DETALLE_SALDO. El valor 'G' = en Gestion Judicial y tiene correlacion 1:1 con FECHA_PASE_GJ (los 158.883 documentos con pase a GJ tienen DOC_SITUACION='G'): es el indicador equivalente y mas simple de usar. NO existe estado de retorno: 157.751 siguen con saldo pendiente, 1.132 sin SALDO_ACTUAL y CERO saldados. |
| `IMPORTE_CONCURSO_QUIEBRA` | NUMBER | YES |  |  |
| `DOC_FECHA_VENC` | DATE | YES |  |  |
| `DOC_CONSUMO` | NUMBER | YES |  | Consumo facturado (kWh) en la cabecera de DOCUMENTOS: LA columna de kWh de una factura. Cubre la banda horaria completa — coincide con CONS_ENERGIA+PICO+VALLE+RESTO de la VM en 99,65% de las filas (revalidado 2026-08: 99,92% en el período 2025/6, y solo 0,56% de las facturas tiene banda horaria). En notas de crédito (DOC_TIPO='C') viene POSITIVO: negar para restar. Es la forma de obtener kWh cuando se usa DOCUMENTOS (la VM AUDITORIA_CAMMESA solo tiene 2022 desde dic-2022). Para kWh preferirla SIEMPRE sobre sumar ITEMS (que solo la reproduce en 81,5%). |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | NO |  |  |
| `DOC_SALDO` | NUMBER | NO |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `DOC_SALDO_ACTUALIZADO` | NUMBER | YES |  |  |
| `DOC_SALDO_ACTUALIZADO_S_I` | NUMBER | YES |  |  |
| `DOC_INTERESES` | NUMBER | YES |  |  |
| `DOC_PUNIT_INTERESES` | NUMBER | YES |  |  |
| `DOC_FECHA_EMISION` | DATE | NO |  |  |
| `VENCIDO_NO_VENCIDO` | VARCHAR2 | YES |  |  |
| `ESCALON_DEUDA` | VARCHAR2 | YES |  |  |
| `FECHA_INTIMACION` | DATE | YES |  |  |
| `ULTIMO_INCORE_EJECUTADO` | VARCHAR2 | YES |  |  |
| `FECHA_EJEC_ULTIMO_INCORE` | DATE | YES |  |  |
| `ULTIMO_INCORE_GENERADO` | VARCHAR2 | YES |  | Ultimo paso INCORE generado para el contrato (XXCO_DETALLE_DEUDA_USR_TMP). Valores = TOR_CODIGO: IN intimacion, CO corte, RE retiro, IA intimacion a servicio activo, NE notificacion de deuda grandes clientes. Su par es ULTIMO_INCORE_EJECUTADO (+ FECHA_ULTIMO_INCORE_GENERADO / FECHA_EJEC_ULTIMO_INCORE). |
| `FECHA_ULTIMO_INCORE_GENERADO` | DATE | YES |  |  |
| `TRT_NUMERO` | NUMBER | YES |  |  |
| `TIENE_GARANTE` | CHAR | YES |  |  |
| `CNT_COND_INTIMACION` | VARCHAR2 | NO |  | Flag S/N en CONTRATOS: si el contrato es intimable. S=3.705.652, N=53.615. CNT_FECHA_TOPE_INTIMAC casi no se usa (20 filas). |
| `CNT_COND_CORTE` | VARCHAR2 | NO |  |  |
| `CNT_COND_RETIRO` | VARCHAR2 | NO |  |  |
| `CNT_FECHA_TOPE_CORTE` | DATE | YES |  |  |
| `DOC_GRUPO` | VARCHAR2 | NO |  | Circuito al que pertenece el documento en DOCUMENTOS. 'N' = normal, el de facturación de energía (14,09M de 14,10M docs en 2025). Los demás son circuitos aparte y no deben mezclarse: T (Factura Telec./comp. interno), O, L, C, G, A. Filtrar DOC_GRUPO='N' junto con DOC_TIPO='F'. |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |  |
| `OFICIO_ERSEP` | VARCHAR2 | YES |  |  |
| `DG_FECHA_ACTUALIZACION` | DATE | YES |  |  |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
