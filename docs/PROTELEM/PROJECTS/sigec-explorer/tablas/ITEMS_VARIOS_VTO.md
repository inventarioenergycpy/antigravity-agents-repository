---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 29753
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "ITEMS_VARIOS_VTO"
---

# 📋 ITEMS_VARIOS_VTO

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 29,753

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `IVT_SECUENCIA` | NUMBER | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `IVT_NUMERO` | NUMBER | YES |  |  |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `ITM_IMPORTE` | NUMBER | YES |  |  |
