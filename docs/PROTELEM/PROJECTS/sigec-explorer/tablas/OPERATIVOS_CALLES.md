---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 956
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "OPERATIVOS_CALLES"
---

# 📋 OPERATIVOS_CALLES

**Filas estimadas:** 956

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `OPE_NUMERO` | NUMBER | YES | 🔗 → [[OPERATIVOS]] |
| `OPE_CALLE` | VARCHAR2 | YES |  |
| `OPE_ALTURA_DESDE` | NUMBER | YES |  |
| `OPE_ALTURA_HASTA` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **OCA_OPE_FK**: `OPE_NUMERO` → [[OPERATIVOS]] (`OPE_NUMERO`)

## FK inferidas (alta confianza)

- `OPE_NUMERO` → [[OPERATIVOS]] _OPE_NUMERO es PK de OPERATIVOS_
