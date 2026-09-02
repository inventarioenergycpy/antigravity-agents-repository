---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 51
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
aliases:
  - "VKO_PAGOS_DOBLES"
---

# 📋 VKO_PAGOS_DOBLES

**Filas estimadas:** 51

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CAP_NRO_PLAN` | VARCHAR2 | NO |  |
| `CAP_CUOTA_NUMERO` | NUMBER | NO |  |
| `PAD_FECHA_PAGO` | DATE | YES |  |
| `PAD_IMPORTE` | NUMBER | YES |  |
| `PAD_FECHA_CARGA` | DATE | YES |  |

## FK inferidas (alta confianza)

- `CAP_CUOTA_NUMERO` → [[VKO_PAGOS]] _CAP_CUOTA_NUMERO es PK de VKO_PAGOS_
