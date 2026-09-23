---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: cobranza
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/cobranza
aliases:
  - "MOVIMIENTOS_MONETARIOS"
---

# 📋 MOVIMIENTOS_MONETARIOS

**Prefijo `MOV_`:** Movimientos de cobranza (MOVIMIENTOS_COBRANZA)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `MOV_NUMERO` | NUMBER | NO |  |
| `CER_NUMERO` | NUMBER | NO |  |
| `PRO_ID` | NUMBER | NO | 🔗 → [[PROCURADORES]] |
| `MOV_TIPO` | VARCHAR2 | NO |  |
| `MOV_IMPORTE` | NUMBER | NO |  |
| `MOV_FECHA_IMPUTACION` | DATE | NO |  |
| `MOV_FECHA_GENERACION` | DATE | NO |  |
| `MOV_ESTADO` | VARCHAR2 | NO |  |
| `MOV_DEB_CRED` | VARCHAR2 | NO |  |
| `ACC_NUMERO` | NUMBER | YES | 🔗 → [[ACCIONES]] |

## FK declaradas → otras tablas

- **MOV_ACC_FK**: `ACC_NUMERO` → [[ACCIONES]] (`ACC_NUMERO`)
- **MOV_PRO_FK**: `PRO_ID` → [[PROCURADORES]] (`PRO_ID`)

## FK inferidas (alta confianza)

- `PRO_ID` → [[PROCURADORES]] _PRO_ID es PK de PROCURADORES_
