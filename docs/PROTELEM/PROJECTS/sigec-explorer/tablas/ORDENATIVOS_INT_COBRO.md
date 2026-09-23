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
  - "ORDENATIVOS_INT_COBRO"
---

# 📋 ORDENATIVOS_INT_COBRO

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ORD_NUMERO` | NUMBER | NO | 🔑 PK |
| `TRX_TRANSACCION` | NUMBER | NO | 🔑 PK |
| `OIO_DOC_NUMERO_FINAN` | NUMBER | NO |  |
| `TRT_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[TRAMITES]] |
| `ORD_ESTADO_ANT` | VARCHAR2 | YES |  |
| `ORD_ESTADO_POST` | VARCHAR2 | YES |  |
| `OIO_FECHA` | DATE | YES |  |

## FK declaradas → otras tablas

- **OIO_TRE_FK**: `TRT_NUMERO` → [[TRAMITES]] (`TRT_NUMERO`)
