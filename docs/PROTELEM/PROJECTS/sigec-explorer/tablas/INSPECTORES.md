---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 398
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "INSPECTORES"
---

# 📋 INSPECTORES

**Filas estimadas:** 398

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `INP_CODIGO` | NUMBER | NO | 🔑 PK |
| `INP_NOMBRE` | VARCHAR2 | YES |  |
| `ZON_CODIGO` | VARCHAR2 | YES |  |
| `INP_HABILITADO` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
