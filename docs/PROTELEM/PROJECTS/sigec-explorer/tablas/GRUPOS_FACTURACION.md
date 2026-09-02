---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1128
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "GRUPOS_FACTURACION"
---

# 📋 GRUPOS_FACTURACION

**Filas estimadas:** 1,128

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRF_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `GRF_DESCRIPCION` | VARCHAR2 | NO |  |
| `GRF_CODIGO_ANTERIOR` | VARCHAR2 | YES |  |
| `GRF_FECHA_ESTAD_INTIM` | DATE | YES |  |
| `GRF_FECHA_INTIMACION` | DATE | YES |  |
| `GRF_CONFIRMA` | VARCHAR2 | YES |  |
| `TFA_CODIGO` | VARCHAR2 | NO |  |
| `GCO_GRUPO` | VARCHAR2 | NO |  |
| `GRF_AUXILIAR` | VARCHAR2 | YES |  |
| `GRF_PAR_IMPAR` | VARCHAR2 | YES |  |
| `GRF_MESES_LECTURA` | VARCHAR2 | YES |  |
| `GRF_TIPO_GRUPO` | VARCHAR2 | YES |  |
| `GRF_ESTADO` | VARCHAR2 | NO |  |
| `GRF_VARIABLE` | VARCHAR2 | NO |  |
| `GRF_FACTURABLE` | VARCHAR2 | NO |  |

## Tablas que referencian esta tabla

- [[XXCO_GRL_GRF]] via `GRF_CODIGO`
