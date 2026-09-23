---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 706
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "IMPRESORAS"
---

# 📋 IMPRESORAS

**Filas estimadas:** 706

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PRT_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `PRT_DESCRIPCION` | VARCHAR2 | YES |  |
| `SCF_CODIGO` | NUMBER | NO | 🔗 → [[SUCURSALES]] |
| `PRT_TIM_CODIGO` | VARCHAR2 | YES |  |
| `TIM_CODIGO` | VARCHAR2 | YES |  |
| `PRT_UNAME` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **PRT_UBICADA_EN**: `SCF_CODIGO` → [[SUCURSALES]] (`SCF_CODIGO`)

## Tablas que referencian esta tabla

- [[CONTROL_REPORTES]] via `PRT_CODIGO`
- [[USUARIOS]] via `PRT_CODIGO`
