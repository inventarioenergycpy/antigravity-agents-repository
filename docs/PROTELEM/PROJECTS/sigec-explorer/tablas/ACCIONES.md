---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 2
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "ACCIONES"
---

# 📋 ACCIONES

**Filas estimadas:** 2

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ACC_NUMERO` | NUMBER | NO | 🔑 PK |
| `PRO_ID` | NUMBER | NO | 🔗 → [[PROCURADORES]] |
| `CER_NUMERO` | NUMBER | NO |  |
| `ETS_CODIGO` | NUMBER | NO | 🔗 → [[ETAPAS]] |
| `ACC_FECHA_INICIO` | DATE | NO |  |
| `ACC_ESTADO` | VARCHAR2 | NO |  |
| `ACC_DESCRIPCION` | VARCHAR2 | NO |  |
| `ACC_LIQUIDADO` | VARCHAR2 | NO |  |

## FK declaradas → otras tablas

- **ACC_ETS_FK**: `ETS_CODIGO` → [[ETAPAS]] (`ETS_CODIGO`)
- **ACC_PRO_FK**: `PRO_ID` → [[PROCURADORES]] (`PRO_ID`)

## Tablas que referencian esta tabla

- [[ACCIONES_PARAMETROS]] via `ACC_NUMERO`
- [[MOVIMIENTOS_MONETARIOS]] via `ACC_NUMERO`

## FK inferidas (alta confianza)

- `PRO_ID` → [[PROCURADORES]] _PRO_ID es PK de PROCURADORES_
- `ETS_CODIGO` → [[ETAPAS]] _ETS_CODIGO es PK de ETAPAS_
