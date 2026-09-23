---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: documentos
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/documentos
aliases:
  - "DOC_TRT_JN"
---

# 📝 DOC_TRT_JN

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `DTN_NUMERO` | NUMBER | NO | 🔑 PK |
| `DOC_TIPO` | VARCHAR2 | NO |  |
| `DOC_NUMERO` | NUMBER | NO |  |
| `USR_NUMERO` | NUMBER | NO |  |
| `DTN_FECHA` | DATE | NO |  |
| `TRT_NUMERO_IN` | NUMBER | YES | 🔗 → [[TRAMITES]] |
| `TRT_NUMERO_OUT` | NUMBER | YES | 🔗 → [[TRAMITES]] |
| `TRX_TRANSACCION` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **DTN_TRE_FK**: `TRT_NUMERO_IN` → [[TRAMITES]] (`TRT_NUMERO`)
- **DTN_TRE_FK2**: `TRT_NUMERO_OUT` → [[TRAMITES]] (`TRT_NUMERO`)

## FK inferidas (alta confianza)

- `TRX_TRANSACCION` → [[ORDENATIVOS_INT_COBRO]] _TRX_TRANSACCION es PK de ORDENATIVOS_INT_COBRO_
