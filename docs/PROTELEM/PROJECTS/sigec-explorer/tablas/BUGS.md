---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1434
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "BUGS"
---

# 📋 BUGS

**Filas estimadas:** 1,434

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TIPO_MOD` | VARCHAR2 | YES |  |
| `NOMBRE_MOD` | VARCHAR2 | YES |  |
| `SEC` | NUMBER | YES |  |
| `FECHA` | DATE | YES |  |
| `PROBLEMA` | VARCHAR2 | YES |  |
| `FECHA_RES` | DATE | YES |  |
| `RESUELTO_POR` | VARCHAR2 | YES |  |
| `COMENT_RESOLUCION` | VARCHAR2 | YES |  |
| `ESTADO` | VARCHAR2 | YES |  |
| `PRIORIDAD` | NUMBER | YES |  |
| `FECHA_ESTIMADA` | DATE | YES |  |
| `USR_CARGA` | NUMBER | YES |  |
| `USR_SOLICITA` | VARCHAR2 | YES |  |
| `FECHA_ASIGNACION` | DATE | YES |  |
| `GRUPO_MOD` | VARCHAR2 | YES |  |
| `BUG_ID` | NUMBER | NO | 🔑 PK |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
