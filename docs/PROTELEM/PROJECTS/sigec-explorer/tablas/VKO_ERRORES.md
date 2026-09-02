---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 137
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "VKO_ERRORES"
---

# 📋 VKO_ERRORES

**Filas estimadas:** 137

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CAP_NRO_PLAN` | VARCHAR2 | NO |  |  |
| `TABLA` | VARCHAR2 | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `CAP_CUOTA_NUMERO` | NUMBER | NO |  |  |
| `PAG_FECHA_PAGO` | DATE | YES |  |  |
| `ERR_FECHA_PROCESO` | DATE | YES |  |  |
| `ERR_IMPORTE` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `CONCEPTO` | VARCHAR2 | YES |  |  |
| `ERROR` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `CAP_CUOTA_NUMERO` → [[VKO_PAGOS]] _CAP_CUOTA_NUMERO es PK de VKO_PAGOS_
