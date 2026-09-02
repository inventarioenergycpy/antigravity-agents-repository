---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "VKO_PLANES_CAIDOS"
---

# 📋 VKO_PLANES_CAIDOS

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CAP_NRO_PLAN` | VARCHAR2 | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PLC_CUOTA_NUMERO` | NUMBER | YES |  |  |
| `PLC_CUOTA_VTO` | DATE | YES |  |  |
