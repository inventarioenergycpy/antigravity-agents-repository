---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "CONTROL_REPORTES"
---

# 📋 CONTROL_REPORTES

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CNR_NUMERO` | NUMBER | NO |  |
| `CNR_COMANDO` | VARCHAR2 | NO |  |
| `CNR_ARCHIVO` | VARCHAR2 | NO |  |
| `CNR_SALIDA` | VARCHAR2 | NO |  |
| `CNR_PRIORIDAD` | NUMBER | YES |  |
| `PRT_CODIGO` | VARCHAR2 | NO | 🔗 → [[IMPRESORAS]] |
| `REP_CODIGO` | VARCHAR2 | NO | 🔗 → [[REPORTES]] |
| `CNR_UNAME` | VARCHAR2 | YES |  |
| `CNR_FECHA_ENTRADA` | DATE | NO |  |
| `CNR_FECHA_INICIO` | DATE | YES |  |
| `CNR_FECHA_FIN` | DATE | YES |  |
| `CNR_PID` | NUMBER | YES |  |
| `USR_NUMERO` | NUMBER | NO | 🔗 → [[USUARIOS]] |
| `CNR_ESTADO` | VARCHAR2 | NO |  |
| `PRT_UNAME` | VARCHAR2 | YES |  |
| `CNR_COPIAS` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **CNR_IMPRESO_EN**: `PRT_CODIGO` → [[IMPRESORAS]] (`PRT_CODIGO`)
- **CNR_INGRESADO_POR**: `USR_NUMERO` → [[USUARIOS]] (`USR_NUMERO`)
- **CNR_PERTENECER**: `REP_CODIGO` → [[REPORTES]] (`REP_CODIGO`)

## FK inferidas (alta confianza)

- `PRT_CODIGO` → [[IMPRESORAS]] _PRT_CODIGO es PK de IMPRESORAS_
- `REP_CODIGO` → [[REPORTES]] _REP_CODIGO es PK de REPORTES_
