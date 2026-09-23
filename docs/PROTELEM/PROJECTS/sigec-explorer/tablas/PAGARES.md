---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 4382
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "PAGARES"
---

# 📋 PAGARES

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 4,382

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `DOC_TIPO_CANCELA` | VARCHAR2 | YES |  |
| `DOC_NUMERO_CANCELA` | NUMBER | YES |  |
| `DOC_TIPO_CANCELADO` | VARCHAR2 | YES |  |
| `DOC_NUMERO_CANCELADO` | NUMBER | YES |  |
| `PUNITP` | NUMBER | YES |  |
| `PUNITU` | NUMBER | YES |  |
| `DIFERENCIA` | NUMBER | YES |  |
| `FECHA` | DATE | YES |  |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
