---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 5667
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "ANALIZAR_GC_AL_CORREO"
---

# 📋 ANALIZAR_GC_AL_CORREO

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 5,667

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PER` | NUMBER | YES |  |  |
| `GRF` | VARCHAR2 | YES |  |  |
| `FEC_ENVIO` | DATE | YES |  |  |
| `CANT` | NUMBER | YES |  |  |
| `SIF_ULTIMO_VTO` | DATE | YES |  |  |
| `SIF_DOC_NRO_DESDE` | VARCHAR2 | YES |  |  |
| `SIF_DOC_NRO_HASTA` | VARCHAR2 | YES |  |  |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | NO |  |  |
| `DOC_SALDO` | NUMBER | NO |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `PRS_E_MAIL` | VARCHAR2 | YES |  |  |
| `PRS_TEL_CELULAR` | VARCHAR2 | YES |  |  |
