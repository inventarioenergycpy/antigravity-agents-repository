---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 99
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "GRUPOS_LECTURA"
---

# 📋 GRUPOS_LECTURA

**Filas estimadas:** 99

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRL_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `GRL_DESCRIPCION` | VARCHAR2 | YES |  |
| `GRL_FRECUENCIA` | NUMBER | NO |  |
| `SEC_CODIGO` | VARCHAR2 | YES |  |
| `AGE_CODIGO` | VARCHAR2 | YES |  |
| `TFR_CODIGO` | VARCHAR2 | NO |  |

## Tablas que referencian esta tabla

- [[RUTAS_LECTURAS]] via `GRL_CODIGO`
- [[XXCO_GRL_GRF]] via `GRL_CODIGO`

## FK inferidas (alta confianza)

- `AGE_CODIGO` → [[AGENCIAS]] _AGE_CODIGO es PK de AGENCIAS_
- `TFR_CODIGO` → [[XXCO_TIPOS_FRECUENCIA]] _TFR_CODIGO es PK de XXCO_TIPOS_FRECUENCIA_
