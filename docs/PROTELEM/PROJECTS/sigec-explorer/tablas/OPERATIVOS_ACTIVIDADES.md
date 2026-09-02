---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: equipos
num_rows: 443
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/equipos
aliases:
  - "OPERATIVOS_ACTIVIDADES"
---

# 📋 OPERATIVOS_ACTIVIDADES

**Filas estimadas:** 443

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `OPE_NUMERO` | NUMBER | YES | 🔗 → [[OPERATIVOS]] |
| `ACT_CODIGO` | VARCHAR2 | YES |  |
| `OAC_OBSERVACIONES` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **OAC_OPE_FK**: `OPE_NUMERO` → [[OPERATIVOS]] (`OPE_NUMERO`)

## FK inferidas (alta confianza)

- `OPE_NUMERO` → [[OPERATIVOS]] _OPE_NUMERO es PK de OPERATIVOS_
