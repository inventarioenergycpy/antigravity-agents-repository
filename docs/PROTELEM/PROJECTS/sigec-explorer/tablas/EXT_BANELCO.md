---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "EXT_BANELCO"
---

# 📋 EXT_BANELCO

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `RDB_COD_REGISTRO` | VARCHAR2 | YES |  |  |
| `RDB_SRV_CNT` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | VARCHAR2 | YES |  |  |
| `DOC_FECHA_VENC_1` | VARCHAR2 | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `RDB_COD_MONEDA` | VARCHAR2 | YES |  |  |
| `RDB_FECHA_COBRO` | VARCHAR2 | YES |  |  |
| `RDB_IMPORTE_ABONADO` | VARCHAR2 | YES |  |  |
| `RDB_COD_MOVIMIENTO` | VARCHAR2 | YES |  |  |
| `RDB_FECHA_ACREDITACION` | VARCHAR2 | YES |  |  |
| `RDB_ID_CANAL_PAGO` | VARCHAR2 | YES |  |  |
| `RDB_NRO_CONTROL` | VARCHAR2 | YES |  |  |
| `RDB_COD_PROVINCIA` | VARCHAR2 | YES |  |  |
