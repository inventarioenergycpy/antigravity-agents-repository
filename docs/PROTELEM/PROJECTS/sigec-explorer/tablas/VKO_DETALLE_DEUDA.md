---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 97263
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "VKO_DETALLE_DEUDA"
---

# 📋 VKO_DETALLE_DEUDA

**Filas estimadas:** 97,263

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CAP_NRO_PLAN` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[VKO_CABECERA_PLAN]] |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `DOC_TIPO` | VARCHAR2 | NO | 🔑 PK |  |
| `DOC_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `DOC_SALDO` | NUMBER | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `DOC_TIPO_MORA` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_MORA` | NUMBER | YES |  |  |
| `DOC_TIPO_FINANCIACION` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_FINANCIACION` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **DED_CAP_FK**: `CAP_NRO_PLAN` → [[VKO_CABECERA_PLAN]] (`CAP_NRO_PLAN`)

## Tablas que referencian esta tabla

- [[VKO_DETALLE_MORA]] via `CAP_NRO_PLAN`, `DOC_NUMERO`, `DOC_TIPO`
