---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1136
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "CLASES"
---

# 📋 CLASES

**Filas estimadas:** 1,136

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TARIFAS]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `CLA_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `CLA_GRUPO` | VARCHAR2 | NO |  |  |
| `CLA_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |  |
| `CLA_CALCULA_COS_FI` | VARCHAR2 | YES |  |  |
| `CLA_EVENTO_COS_FI` | VARCHAR2 | YES |  |  |
| `CLA_PRORRATEA` | VARCHAR2 | YES |  |  |
| `CLA_SOCIAL_TIPO` | VARCHAR2 | YES |  |  |
| `CLA_ENERGIA_DIST` | VARCHAR2 | YES |  |  |
| `CLA_PREPAGO` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **CLA_FK_TCL**: `TCL_CODIGO` → [[TARIFAS]] (`TCL_CODIGO`)

## Tablas que referencian esta tabla

- [[COMBINACIONES_HABILITADAS]] via `CLA_CODIGO`, `TCL_CODIGO`
- [[PENALIZACIONES]] via `CLA_CODIGO`, `TCL_CODIGO`
- [[PRECIOS_CONTRIB_REEMBOL]] via `CLA_CODIGO`, `TCL_CODIGO`
- [[PRECIOS_TARIFA]] via `CLA_CODIGO`, `TCL_CODIGO`
- [[RANGO_POTENCIAS]] via `CLA_CODIGO`, `TCL_CODIGO`
- [[XX_TARIFAS_GRUPOS]] via `CLA_CODIGO`, `TCL_CODIGO`
