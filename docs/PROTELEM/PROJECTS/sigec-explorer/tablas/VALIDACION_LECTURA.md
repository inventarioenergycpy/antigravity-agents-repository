---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 69
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "VALIDACION_LECTURA"
---

# 📋 VALIDACION_LECTURA

**Filas estimadas:** 69

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `VAL_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `VAL_MENSAJE` | VARCHAR2 | YES |  |
| `VAL_CANTIDAD` | NUMBER | NO |  |
| `VAL_TIPO` | VARCHAR2 | YES |  |
| `VAL_ORDEN` | NUMBER | YES |  |
| `VAL_SQL_TEXTO_MOSTRAR` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[XXCO_SOLUCIONES_ERRORES_LCT]] via `VAL_CODIGO`
