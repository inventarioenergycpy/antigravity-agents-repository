---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 4759
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_XML_INTERBANKING"
---

# 🔧 XXCO_XML_INTERBANKING

**Filas estimadas:** 4,759

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `XIN_NOMBRE_ARCHIVO` | VARCHAR2 | NO | 🔑 PK |
| `XIN_FECHA` | DATE | YES |  |
| `XIN_ESTADO` | VARCHAR2 | YES |  |
| `XIN_ARCHIVO` | CLOB | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |

## Tablas que referencian esta tabla

- [[XXCO_XML_DETALLE]] via `XIN_NOMBRE_ARCHIVO`
