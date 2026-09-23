---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 9874
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "VARIABLES_NOTIFICACION"
---

# 📋 VARIABLES_NOTIFICACION

**Filas estimadas:** 9,874

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `NOT_CODIGO` | VARCHAR2 | NO |  |
| `ENO_ORDEN` | NUMBER | NO |  |
| `VNO_SESSION` | NUMBER | NO |  |
| `ENO_SUB_ORDEN` | NUMBER | YES |  |
| `VNO_ID` | NUMBER | NO |  |
| `VNO_CONTENIDO` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `ENO_ORDEN` → [[ESTRUCTURA_NOTIFICACION]] _ENO_ORDEN es PK de ESTRUCTURA_NOTIFICACION_
