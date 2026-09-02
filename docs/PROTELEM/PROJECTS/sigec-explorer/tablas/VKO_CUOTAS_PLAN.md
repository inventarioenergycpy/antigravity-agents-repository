---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 366530
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "VKO_CUOTAS_PLAN"
---

# 📋 VKO_CUOTAS_PLAN

**Filas estimadas:** 366,530

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CAP_NRO_PLAN` | VARCHAR2 | NO | 🔑 PK |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `CUP_CUOTA_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `CUP_CUOTA_VTO` | DATE | YES |  |  |
| `CUP_CUOTA_ACT` | DATE | YES |  |  |
| `CUP_CONCEPTO` | VARCHAR2 | NO | 🔑 PK |  |
| `CUP_IMPORTE` | NUMBER | YES |  |  |
