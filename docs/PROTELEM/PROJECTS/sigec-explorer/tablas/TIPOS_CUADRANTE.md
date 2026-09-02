---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 184
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "TIPOS_CUADRANTE"
---

# 📋 TIPOS_CUADRANTE

**Filas estimadas:** 184

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CDR_UNIDAD` | VARCHAR2 | NO | 🔑 PK |
| `TCU_DESCRIPCION` | VARCHAR2 | NO |  |
| `TCU_GRUPO` | VARCHAR2 | NO |  |
| `TCU_ACUMULATIVO` | VARCHAR2 | NO |  |
| `TCU_ORDEN` | NUMBER | YES |  |
| `TCU_UNIDAD_MEDIDA` | VARCHAR2 | YES |  |
| `TCU_CANT_HORAS` | NUMBER | YES |  |
| `TCU_NUMERO` | NUMBER | YES |  |
| `TCU_ESTADO` | VARCHAR2 | YES |  |
| `TCU_CDR_ACUMULATIVO` | VARCHAR2 | YES |  |
| `TCU_BANDA_HORARIA` | VARCHAR2 | YES |  |
| `TCU_CDR_LEIBLE` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[CONCEPTOS_TARIFAS]] via `CDR_UNIDAD`
- [[CUADRANTES_TARIFA]] via `CDR_UNIDAD`
- [[CUADRANTES_TARIFA_DET]] via `CDR_UNIDAD`
- [[DETALLES_PENALIZACION]] via `CDR_UNIDAD`
- [[RANGO_POTENCIAS]] via `CDR_CODIGO`
