---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: cobranza
num_rows: 415643
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/cobranza
aliases:
  - "XXCO_DIFERENCIAS_FIANNCIACION"
---

# 🔧 XXCO_DIFERENCIAS_FIANNCIACION

**Prefijo `APL_`:** Aplicaciones / imputación de pagos (APLICACIONES)

**Filas estimadas:** 415,643

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `DOC_NUMERO_FINAN` | NUMBER | YES |  |
| `IMPORTE_APL` | NUMBER | YES |  |
| `IMPORTE_CF` | NUMBER | YES |  |
| `IMPORTE_CC` | NUMBER | YES |  |
| `APL_CF` | NUMBER | YES |  |
| `APL_CC_PG` | NUMBER | YES |  |
| `FECHA` | DATE | YES |  |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
