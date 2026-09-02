---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 246380
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "VKO_CUOTAS_MORA_PLAN"
---

# 📋 VKO_CUOTAS_MORA_PLAN

**Filas estimadas:** 246,380

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CAP_NRO_PLAN` | VARCHAR2 | NO | 🔑 PK |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `CMP_CUOTA_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `CMP_CUOTA_VTO` | DATE | NO | 🔑 PK |  |
| `CMP_CONCEPTO` | VARCHAR2 | NO | 🔑 PK |  |
| `CMP_IMPORTE` | NUMBER | YES |  |  |
| `CMP_FECHA_CALCULO` | DATE | NO | 🔑 PK |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
