---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 5962
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_TARIFAS_BASE_CONFECCIONES"
---

# 🔧 XXCO_TARIFAS_BASE_CONFECCIONES

**Filas estimadas:** 5,962

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PCC_NUMERO` | NUMBER | NO | 🔑 PK |
| `TCL_CODIGO_BASE` | VARCHAR2 | NO | 🔑 PK |
| `CLA_CODIGOS` | VARCHAR2 | NO | 🔑 PK |
| `TEN_CODIGOS` | VARCHAR2 | NO | 🔑 PK |

## Tablas que referencian esta tabla

- [[XXCO_CONCEPTOS_CONFECCIONES]] via `CCR_CLASES`, `CCR_TENSIONES`, `PCC_NUMERO`, `TCL_CODIGO_BASE`
- [[XXCO_REPLICAS_TARIFAS_CONFEC]] via `CLA_CODIGOS`, `PCC_NUMERO`, `TCL_CODIGO_BASE`, `TEN_CODIGOS`
