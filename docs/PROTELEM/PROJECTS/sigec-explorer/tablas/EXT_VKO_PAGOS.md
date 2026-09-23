---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "EXT_VKO_PAGOS"
---

# 📋 EXT_VKO_PAGOS

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TIPO_REGISTRO` | VARCHAR2 | YES |  |  |
| `NRO_CLIENTE` | NUMBER | YES |  | Número de cliente en tablas EXT_VKO_* (integración externa). |
| `NRO_PLAN` | VARCHAR2 | YES |  |  |
| `NRO_CUOTA` | NUMBER | YES |  |  |
| `FECHA_PAGO` | DATE | YES |  |  |
| `IMPORTE` | NUMBER | YES |  |  |
