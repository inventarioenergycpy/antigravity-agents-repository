---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "TMP_INTERBANKING_XML"
---

# 📋 TMP_INTERBANKING_XML

**Filas estimadas:** 1

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `XIN_NOMBRE_ARCHIVO` | VARCHAR2 | NO |  |
| `XIN_FECHA` | DATE | YES |  |
| `XIN_ESTADO` | VARCHAR2 | YES |  |
| `XIN_ARCHIVO` | CLOB | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `XIN_NOMBRE_ARCHIVO` → [[XXCO_XML_INTERBANKING]] _XIN_NOMBRE_ARCHIVO es PK de XXCO_XML_INTERBANKING_
