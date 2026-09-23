---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 3262
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "STOCK_ELEMENTOS"
---

# 📋 STOCK_ELEMENTOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 3,262

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `STO_ID` | NUMBER | NO | 🔑 PK |
| `STO_FECHA` | DATE | YES |  |
| `TIT_CLAVE` | VARCHAR2 | YES | 🔗 → [[TIPOS_ITEM]] |
| `TME_ID` | VARCHAR2 | YES | 🔗 → [[TIPOS_MOV_ELEMENTOS]] |
| `STO_CANTIDAD` | NUMBER | YES |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |
| `DOC_NUMERO` | NUMBER | YES |  |
| `SCF_CODIGO` | NUMBER | YES |  |
| `USR_NUMERO` | NUMBER | YES |  |
| `STO_OBSERVACIONES` | VARCHAR2 | YES |  |
| `AGE_CODIGO` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **TIT_CLAVE_FK**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
- **TME_ID_FK**: `TME_ID` → [[TIPOS_MOV_ELEMENTOS]] (`TME_ID`)

## FK inferidas (alta confianza)

- `AGE_CODIGO` → [[AGENCIAS]] _AGE_CODIGO es PK de AGENCIAS_
- `TME_ID` → [[TIPOS_MOV_ELEMENTOS]] _TME_ID es PK de TIPOS_MOV_ELEMENTOS_
