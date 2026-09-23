---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 14
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PLSQL_PROFILER_RUNS"
---

# 📋 PLSQL_PROFILER_RUNS

> Run-specific information for the PL/SQL profiler

**Filas estimadas:** 14

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RUNID` | NUMBER | NO | 🔑 PK |
| `RELATED_RUN` | NUMBER | YES |  |
| `RUN_OWNER` | VARCHAR2 | YES |  |
| `RUN_DATE` | DATE | YES |  |
| `RUN_COMMENT` | VARCHAR2 | YES |  |
| `RUN_TOTAL_TIME` | NUMBER | YES |  |
| `RUN_SYSTEM_INFO` | VARCHAR2 | YES |  |
| `RUN_COMMENT1` | VARCHAR2 | YES |  |
| `SPARE1` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[PLSQL_PROFILER_UNITS]] via `RUNID`
