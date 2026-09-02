---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 3554
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "OPERATIVOS"
---

# 📋 OPERATIVOS

**Filas estimadas:** 3,554

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `OPE_NUMERO` | NUMBER | NO | 🔑 PK |
| `OPE_DESCRIPCION` | VARCHAR2 | YES |  |
| `OPE_FECHA_DESDE` | DATE | YES |  |
| `OPE_FECHA_HASTA` | DATE | YES |  |
| `OPE_ESTADO` | VARCHAR2 | YES |  |
| `OPE_ORIGEN` | VARCHAR2 | YES |  |
| `OPE_NUMERO_PADRE` | NUMBER | YES | 🔗 → [[OPERATIVOS]] |
| `USR_NUMERO` | NUMBER | YES |  |
| `OPE_FECHA_CARGA` | DATE | YES |  |
| `OPE_INSPECTOR` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **OPE_OPE_FK**: `OPE_NUMERO_PADRE` → [[OPERATIVOS]] (`OPE_NUMERO`)

## Tablas que referencian esta tabla

- [[OPERATIVOS]] via `OPE_NUMERO_PADRE`
- [[OPERATIVOS_ACTIVIDADES]] via `OPE_NUMERO`
- [[OPERATIVOS_BARRIOS]] via `OPE_NUMERO`
- [[OPERATIVOS_CALLES]] via `OPE_NUMERO`
- [[OPERATIVOS_LINEAS]] via `OPE_NUMERO`
- [[OPERATIVOS_SUBESTACIONES]] via `OPE_NUMERO`
- [[RECLAMOS]] via `OPE_NUMERO`
