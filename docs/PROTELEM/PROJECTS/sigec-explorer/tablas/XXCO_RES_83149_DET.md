---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 146193
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_RES_83149_DET"
---

# 🔧 XXCO_RES_83149_DET

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 146,193

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ID_REPORTE` | NUMBER | NO | 🔑 PK |  |
| `ANIO` | NUMBER | NO |  |  |
| `PERIODO` | NUMBER | NO |  |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_ESTADO` | VARCHAR2 | YES |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `CIB_CODIGO` | NUMBER | YES |  |  |
| `IVV_CODIGO` | NUMBER | YES |  |  |
| `OIM_TIPO` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO_OIM` | NUMBER | YES |  |  |
| `E_PICO_PERIODO` | NUMBER | YES |  |  |
| `E_VALLE_PERIODO` | NUMBER | YES |  |  |
| `E_RESTO_PERIODO` | NUMBER | YES |  |  |
| `E_REACTIVA_PERIODO` | NUMBER | YES |  |  |
| `E_PICO_PER_2019` | NUMBER | YES |  |  |
| `E_VALLE_PER_2019` | NUMBER | YES |  |  |
| `E_RESTO_PER_2019` | NUMBER | YES |  |  |
| `E_REACTIVA_PER_2019` | NUMBER | YES |  |  |
| `E_PICO_PER_032020` | NUMBER | YES |  |  |
| `E_VALLE_PER_032020` | NUMBER | YES |  |  |
| `E_RESTO_PER_032020` | NUMBER | YES |  |  |
| `E_REACTIVA_PER_032020` | NUMBER | YES |  |  |
| `APLICA` | VARCHAR2 | YES |  |  |
| `POTENCIA_CONT_DP` | NUMBER | YES |  |  |
| `POTENCIA_CONT_DF` | NUMBER | YES |  |  |
| `POTENCIA_PEN_DP` | NUMBER | YES |  |  |
| `POTENCIA_PEN_DF` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `POSEE_IAF` | VARCHAR2 | YES |  |  |
| `ES_PADRE` | VARCHAR2 | YES |  |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `CNT_CIIU` | NUMBER | YES |  |  |
| `RELACION` | NUMBER | YES |  |  |
| `SIMULADO_CON_MULTA` | NUMBER | YES |  |  |
| `SIMULADO_SIN_MULTA` | NUMBER | YES |  |  |
| `SIMULADO_LEIDA` | NUMBER | YES |  |  |
| `DOC_FECHA_EMISION` | DATE | YES |  |  |
| `POTENCIA_LEIDA_DP` | NUMBER | YES |  |  |
| `POTENCIA_LEIDA_DF` | NUMBER | YES |  |  |
| `POTENCIA_CONT_DP_032020` | NUMBER | YES |  |  |
| `POTENCIA_PEN_DP_032020` | NUMBER | YES |  |  |
| `POTENCIA_PEN_DF_032020` | NUMBER | YES |  |  |
| `POTENCIA_LEIDA_DP_032020` | NUMBER | YES |  |  |
| `POTENCIA_LEIDA_DF_032020` | NUMBER | YES |  |  |
| `POTENCIA_CONT_DP_2019` | NUMBER | YES |  |  |
| `POTENCIA_CONT_DF_2019` | NUMBER | YES |  |  |
| `POTENCIA_PEN_DP_2019` | NUMBER | YES |  |  |
| `POTENCIA_PEN_DF_2019` | NUMBER | YES |  |  |
| `POTENCIA_LEIDA_DP_2019` | NUMBER | YES |  |  |
| `POTENCIA_LEIDA_DF_2019` | NUMBER | YES |  |  |
| `POTENCIA_CONT_DF_032020` | NUMBER | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `FLEXIBILIZADA` | VARCHAR2 | YES |  |  |
| `NRO_SOLICITUD` | NUMBER | YES |  |  |
| `AJUSTE_83531` | VARCHAR2 | YES |  |  |
| `TIPO_AJUSTE_83531` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `CNT_CIIU` → [[CODIGOS_CIIU]] _CNT_CIIU es PK de CODIGOS_CIIU_
- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
