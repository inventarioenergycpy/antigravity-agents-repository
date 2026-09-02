---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 872
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "STD_POTENCIAS"
---

# 📋 STD_POTENCIAS

**Filas estimadas:** 872

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ZON_CODIGO` | VARCHAR2 | NO |  |  |
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `TCL_CODIGO_AGRUPADO` | VARCHAR2 | YES |  |  |
| `UNIDAD` | VARCHAR2 | YES |  |  |
| `POTENCIA` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
