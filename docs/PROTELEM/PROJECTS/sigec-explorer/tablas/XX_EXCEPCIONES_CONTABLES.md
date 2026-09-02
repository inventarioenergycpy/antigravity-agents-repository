---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 31
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_EXCEPCIONES_CONTABLES"
---

# 📋 XX_EXCEPCIONES_CONTABLES

**Filas estimadas:** 31

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `EXC_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `MCO_CODIGO` | VARCHAR2 | YES |  |
| `EXC_CUENTA_VALOR` | VARCHAR2 | YES |  |
| `CODE_COMBINATION_ID` | NUMBER | YES |  |
| `EXC_OBSERVACION` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `MCO_CODIGO` → [[MODELOS_CONTABLES]] _MCO_CODIGO es PK de MODELOS_CONTABLES_
