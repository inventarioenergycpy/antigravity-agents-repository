---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 10863
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PLSQL_PROFILER_DATA"
---

# 📋 PLSQL_PROFILER_DATA

> Accumulated data from all profiler runs

**Filas estimadas:** 10,863

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RUNID` | NUMBER | NO | 🔑 PK · 🔗 → [[PLSQL_PROFILER_UNITS]] |
| `UNIT_NUMBER` | NUMBER | NO | 🔑 PK · 🔗 → [[PLSQL_PROFILER_UNITS]] |
| `LINE#` | NUMBER | NO | 🔑 PK |
| `TOTAL_OCCUR` | NUMBER | YES |  |
| `TOTAL_TIME` | NUMBER | YES |  |
| `MIN_TIME` | NUMBER | YES |  |
| `MAX_TIME` | NUMBER | YES |  |
| `SPARE1` | NUMBER | YES |  |
| `SPARE2` | NUMBER | YES |  |
| `SPARE3` | NUMBER | YES |  |
| `SPARE4` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **SYS_C00156469**: `RUNID`, `UNIT_NUMBER` → [[PLSQL_PROFILER_UNITS]] (`RUNID`, `UNIT_NUMBER`)
