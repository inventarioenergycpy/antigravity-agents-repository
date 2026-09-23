---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1943
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "OPERATIVOS_SUBESTACIONES"
---

# 📋 OPERATIVOS_SUBESTACIONES

**Filas estimadas:** 1,943

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `OPE_NUMERO` | NUMBER | YES | 🔗 → [[OPERATIVOS]] |
| `SUB_CODIGO` | VARCHAR2 | YES |  |
| `OSU_OBSERVACIONES` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **OSU_OPE_FK**: `OPE_NUMERO` → [[OPERATIVOS]] (`OPE_NUMERO`)

## FK inferidas (alta confianza)

- `OPE_NUMERO` → [[OPERATIVOS]] _OPE_NUMERO es PK de OPERATIVOS_
- `SUB_CODIGO` → [[XXCO_ARTEFACTOS_SUBCATEGORIAS]] _SUB_CODIGO es PK de XXCO_ARTEFACTOS_SUBCATEGORIAS_
