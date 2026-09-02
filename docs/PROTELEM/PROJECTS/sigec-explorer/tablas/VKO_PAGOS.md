---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 92657
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "VKO_PAGOS"
---

# 📋 VKO_PAGOS

**Filas estimadas:** 92,657

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CAP_NRO_PLAN` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[VKO_CABECERA_PLAN]] |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `CAP_CUOTA_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `PAG_FECHA_PAGO` | DATE | YES |  |  |
| `PAG_ESTADO` | VARCHAR2 | YES |  |  |
| `PAG_FECHA_PROCESO` | DATE | YES |  |  |
| `PAG_IMPORTE` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **PAG_CAP_FK**: `CAP_NRO_PLAN` → [[VKO_CABECERA_PLAN]] (`CAP_NRO_PLAN`)
