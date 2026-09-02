---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 209
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_SOLUCIONES_ERRORES_LCT"
---

# 🔧 XXCO_SOLUCIONES_ERRORES_LCT

**Filas estimadas:** 209

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `VAL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[VALIDACION_LECTURA]] |
| `SEL_SECUENCIA` | NUMBER | NO | 🔑 PK |
| `SEL_DESCRIPCION` | VARCHAR2 | YES |  |
| `SEL_TEXTO_MOSTRAR` | VARCHAR2 | NO |  |

## FK declaradas → otras tablas

- **SEL_VAL_FK**: `VAL_CODIGO` → [[VALIDACION_LECTURA]] (`VAL_CODIGO`)

## Tablas que referencian esta tabla

- [[XXCO_EJEC_SOLUCION_LCT]] via `SEL_SECUENCIA`, `VAL_CODIGO`
