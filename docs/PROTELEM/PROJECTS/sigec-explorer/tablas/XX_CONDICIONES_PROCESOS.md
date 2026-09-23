---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 238
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_CONDICIONES_PROCESOS"
---

# 📋 XX_CONDICIONES_PROCESOS

**Filas estimadas:** 238

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PAP_CODIGO` | VARCHAR2 | NO | 🔗 → [[XX_PARAMETR_PROCESOS]] |
| `COP_CODIGO` | NUMBER | NO | 🔑 PK |
| `COP_DESCRIPCION` | VARCHAR2 | YES |  |
| `TPP_CODIGO` | VARCHAR2 | NO | 🔗 → [[XX_TIPOS_PARAMETROS_PROCESOS]] |
| `COP_VALOR` | VARCHAR2 | YES |  |
| `COP_TIPO` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **FK_COP_PAP**: `PAP_CODIGO` → [[XX_PARAMETR_PROCESOS]] (`PAP_CODIGO`)
- **FK_COP_TPP**: `TPP_CODIGO` → [[XX_TIPOS_PARAMETROS_PROCESOS]] (`TPP_CODIGO`)

## Tablas que referencian esta tabla

- [[XX_VALORES_COND_PROC]] via `COP_CODIGO`

## FK inferidas (alta confianza)

- `PAP_CODIGO` → [[XX_PARAMETR_PROCESOS]] _PAP_CODIGO es PK de XX_PARAMETR_PROCESOS_
- `TPP_CODIGO` → [[XX_TIPOS_PARAMETROS_PROCESOS]] _TPP_CODIGO es PK de XX_TIPOS_PARAMETROS_PROCESOS_
