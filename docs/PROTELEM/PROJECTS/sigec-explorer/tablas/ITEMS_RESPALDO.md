---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 230
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "ITEMS_RESPALDO"
---

# 📋 ITEMS_RESPALDO

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 230

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ITM_NUMERO` | NUMBER | NO |  |
| `DOC_TIPO` | VARCHAR2 | NO |  |
| `DOC_NUMERO` | NUMBER | NO |  |
| `DOC_TIPO_ORIGEN_1` | VARCHAR2 | YES |  |
| `DOC_NUMERO_ORIGEN_1` | NUMBER | YES |  |
| `TIT_CLAVE` | VARCHAR2 | NO |  |
| `ITM_DETALLE` | VARCHAR2 | YES |  |
| `ITM_CANTIDAD` | NUMBER | YES |  |
| `ITM_PRECIO_UNIT` | NUMBER | YES |  |
| `ITM_IMPORTE` | NUMBER | NO |  |
| `ITM_SALDO` | NUMBER | YES |  |
| `ITM_MES_CONTABLE` | NUMBER | YES |  |
| `ITM_ESTADO` | VARCHAR2 | YES |  |
| `DOC_NUMERO_ORIGEN` | NUMBER | YES |  |
| `DOC_TIPO_ORIGEN` | VARCHAR2 | YES |  |
| `ITM_VENC_NRO` | VARCHAR2 | YES |  |
| `ITM_SALDO_CANTIDAD` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `ITM_NUMERO` → [[XX_INFORMES_PROCESOS_ITEMS]] _ITM_NUMERO es PK de XX_INFORMES_PROCESOS_ITEMS_
