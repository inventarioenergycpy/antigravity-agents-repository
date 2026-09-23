---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 40777
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_CASOS_MOVIDOS_FECHA_VENC"
---

# 🔧 XXCO_CASOS_MOVIDOS_FECHA_VENC

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 40,777

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `MPA_TIPO` | VARCHAR2 | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `DOC_FECHA_VENC_1_GRF` | DATE | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `CRF_ANIO` | NUMBER | YES |  |  |
| `CRF_PERIODO` | NUMBER | YES |  |  |
| `FRENADO` | VARCHAR2 | YES |  |  |
