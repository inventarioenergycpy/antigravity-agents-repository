---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 59
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
aliases:
  - "XXCO_VERAZ"
---

# 🔧 XXCO_VERAZ

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 59

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ITM_NUMERO` | NUMBER | YES |  |
| `TIT_CLAVE` | VARCHAR2 | YES |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |
| `DOC_NUMERO` | NUMBER | YES |  |
| `DOC_TIPO_CANCELA` | VARCHAR2 | YES |  |
| `DOC_NUMERO_CANCELA` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `ITM_NUMERO` → [[XX_INFORMES_PROCESOS_ITEMS]] _ITM_NUMERO es PK de XX_INFORMES_PROCESOS_ITEMS_
