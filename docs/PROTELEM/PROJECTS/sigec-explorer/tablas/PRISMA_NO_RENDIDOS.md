---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1266
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PRISMA_NO_RENDIDOS"
---

# 📋 PRISMA_NO_RENDIDOS

**Filas estimadas:** 1,266

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `FECHA` | DATE | YES |  |
| `SERV` | VARCHAR2 | YES |  |
| `CNT` | VARCHAR2 | YES |  |
| `TIPO_DOC` | VARCHAR2 | YES |  |
| `NUMERO_DOC` | NUMBER | YES |  |
| `IMPORTE` | NUMBER | YES |  |
| `PROCESA_ORDENATIVO` | VARCHAR2 | YES |  |
| `ID_TRANSACCION` | VARCHAR2 | YES |  |
| `SITE_TRANSACTION_ID` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
