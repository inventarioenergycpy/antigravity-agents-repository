---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_TRANSACCIONES_COBRANZA"
---

# 📋 XX_TRANSACCIONES_COBRANZA

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TXR_TRANSACCION` | NUMBER | NO |  |
| `TXR_ESTADO` | VARCHAR2 | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `TAN_CODIGO` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `TAN_CODIGO` → [[TIPOS_ANORMALIDAD]] _TAN_CODIGO es PK de TIPOS_ANORMALIDAD_
