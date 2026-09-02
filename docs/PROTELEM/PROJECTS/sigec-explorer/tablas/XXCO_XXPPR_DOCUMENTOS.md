---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 9856273
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
aliases:
  - "XXCO_XXPPR_DOCUMENTOS"
---

# 🔧 XXCO_XXPPR_DOCUMENTOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 9,856,273

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `DOC_NUMERO` | NUMBER | NO | 🔑 PK |
| `C_CLOB` | CLOB | YES |  |
| `FECHA` | DATE | YES |  |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
