---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 83414
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_PERSONAS_ACTIVIDADES_DGR"
---

# 🔧 XXCO_PERSONAS_ACTIVIDADES_DGR

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 83,414

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `ADR_CODIGO` | NUMBER | NO |  |  |

## FK inferidas (alta confianza)

- `ADR_CODIGO` → [[XXCO_ACTIVIDADES_DGR]] _ADR_CODIGO es PK de XXCO_ACTIVIDADES_DGR_
