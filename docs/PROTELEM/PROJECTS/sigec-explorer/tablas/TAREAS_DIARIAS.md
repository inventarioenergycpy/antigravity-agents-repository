---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 82
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "TAREAS_DIARIAS"
---

# 📋 TAREAS_DIARIAS

**Filas estimadas:** 82

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TDI_ID` | NUMBER | NO | 🔑 PK |
| `FECHA_HORA` | DATE | YES |  |
| `TPR_ID` | VARCHAR2 | YES | 🔗 → [[TIPOS_PROBLEMA]] |
| `USUARIO_PEDIDO` | VARCHAR2 | YES |  |
| `TSO_ID` | VARCHAR2 | YES | 🔗 → [[TIPOS_SOLUCION]] |
| `DESC_PROBLEMA` | VARCHAR2 | YES |  |
| `USUARIO_SOLUCION` | VARCHAR2 | YES |  |
| `ESTADO` | VARCHAR2 | YES |  |
| `TIEMPO_INSUMO` | VARCHAR2 | YES |  |
| `GRUPO_MOD` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **TPR_FK**: `TPR_ID` → [[TIPOS_PROBLEMA]] (`TPR_ID`)
- **TSO_FK**: `TSO_ID` → [[TIPOS_SOLUCION]] (`TSO_ID`)

## FK inferidas (alta confianza)

- `TPR_ID` → [[TIPOS_PROBLEMA]] _TPR_ID es PK de TIPOS_PROBLEMA_
- `TSO_ID` → [[TIPOS_SOLUCION]] _TSO_ID es PK de TIPOS_SOLUCION_
