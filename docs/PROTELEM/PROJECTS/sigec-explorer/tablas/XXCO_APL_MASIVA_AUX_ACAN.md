---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 878
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_APL_MASIVA_AUX_ACAN"
---

# 🔧 XXCO_APL_MASIVA_AUX_ACAN

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 878

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `APL_IMPORTE` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_3` | NUMBER | YES |  |  |
| `ESTADO` | VARCHAR2 | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
