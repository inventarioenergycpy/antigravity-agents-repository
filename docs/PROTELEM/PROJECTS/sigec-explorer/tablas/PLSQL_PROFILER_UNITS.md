---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 161
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PLSQL_PROFILER_UNITS"
---

# 📋 PLSQL_PROFILER_UNITS

> Information about each library unit in a run

**Filas estimadas:** 161

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RUNID` | NUMBER | NO | 🔑 PK · 🔗 → [[PLSQL_PROFILER_RUNS]] |
| `UNIT_NUMBER` | NUMBER | NO | 🔑 PK |
| `UNIT_TYPE` | VARCHAR2 | YES |  |
| `UNIT_OWNER` | VARCHAR2 | YES |  |
| `UNIT_NAME` | VARCHAR2 | YES |  |
| `UNIT_TIMESTAMP` | DATE | YES |  |
| `TOTAL_TIME` | NUMBER | NO |  |
| `SPARE1` | NUMBER | YES |  |
| `SPARE2` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **SYS_C00156468**: `RUNID` → [[PLSQL_PROFILER_RUNS]] (`RUNID`)

## Tablas que referencian esta tabla

- [[PLSQL_PROFILER_DATA]] via `RUNID`, `UNIT_NUMBER`
