---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 412
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ASIGNACIONES"
---

# 📋 ASIGNACIONES

**Filas estimadas:** 412

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CER_NUMERO` | NUMBER | NO |  |
| `PRO_ID` | NUMBER | NO | 🔗 → [[PROCURADORES]] |
| `ASI_FECHA_ASIGNADO` | DATE | NO |  |
| `ASI_FECHA_BAJA` | DATE | YES |  |
| `ASI_OBSERVACIONES` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **ASI_PRO_FK**: `PRO_ID` → [[PROCURADORES]] (`PRO_ID`)

## FK inferidas (alta confianza)

- `PRO_ID` → [[PROCURADORES]] _PRO_ID es PK de PROCURADORES_
