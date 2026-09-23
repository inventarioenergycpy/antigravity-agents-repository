---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 72737933
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "MIRA_DOC"
---

# 📋 MIRA_DOC

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 72,737,933

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_IMPORTE_BASICO` | NUMBER | YES |  | NO USAR como neto de la factura: coincide con DOC_IMPORTE_GRAVADO en solo el 70,6% y es MENOR en el 28,2% (muestra 322.120 docs de 2025). Poblada al 100% pero con semántica distinta al neto gravado. Para el neto usar DOC_IMPORTE_GRAVADO. |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `DOC_FECHA_EMISION` | DATE | YES |  |  |
| `DOC_TIPO_N` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_N` | NUMBER | YES |  |  |
| `SRV_CODIGO_N` | NUMBER | YES |  |  |
| `CNT_NUMERO_N` | NUMBER | YES |  |  |
| `DOC_IMPORTE_BASICO_N` | NUMBER | YES |  |  |
| `DOC_IMPORTE_ORIGINAL_N` | NUMBER | YES |  |  |
| `DOC_FECHA_EMISION_N` | DATE | YES |  |  |
| `NRO_SESSION` | NUMBER | YES |  |  |
| `USR_UNIX` | VARCHAR2 | YES |  |  |
| `NRO_ORACLE` | NUMBER | YES |  |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |  |
| `SERVIDOR` | VARCHAR2 | YES |  |  |
| `TERMINAL` | VARCHAR2 | YES |  |  |
| `PROGRAMA` | VARCHAR2 | YES |  |  |
| `OPERACION` | VARCHAR2 | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `DOC_RECARGO_VENC_2` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_3` | NUMBER | YES |  |  |
| `OBSERVA` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `USR_GET` | NUMBER | YES |  |  |
| `DOC_SITUACION` | VARCHAR2 | YES |  | Situacion del documento de deuda en DETALLE_SALDO. El valor 'G' = en Gestion Judicial y tiene correlacion 1:1 con FECHA_PASE_GJ (los 158.883 documentos con pase a GJ tienen DOC_SITUACION='G'): es el indicador equivalente y mas simple de usar. NO existe estado de retorno: 157.751 siguen con saldo pendiente, 1.132 sin SALDO_ACTUAL y CERO saldados. |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `DOC_FECHA_VENC_2` | DATE | YES |  |  |
| `DOC_FECHA_VENC_3` | DATE | YES |  |  |
| `DATOS_PROCESOS` | VARCHAR2 | YES |  |  |
| `DOC_GRUPO` | VARCHAR2 | YES |  | Circuito al que pertenece el documento en DOCUMENTOS. 'N' = normal, el de facturación de energía (14,09M de 14,10M docs en 2025). Los demás son circuitos aparte y no deben mezclarse: T (Factura Telec./comp. interno), O, L, C, G, A. Filtrar DOC_GRUPO='N' junto con DOC_TIPO='F'. |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
