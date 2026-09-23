---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 4181
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "RECARGOS"
---

# 📋 RECARGOS

**Filas estimadas:** 4,181

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `RCG_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `RCG_DIAS_DESDE` | NUMBER | NO |  |  |
| `RCG_DIAS_HASTA` | NUMBER | NO |  |  |
| `RCG_APLICACION` | VARCHAR2 | NO |  |  |
| `RCG_TIPO` | VARCHAR2 | NO |  |  |
| `RCG_TASA` | NUMBER | YES |  |  |
| `TIN_CODIGO` | VARCHAR2 | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | YES |  |  |
| `TFA_CODIGO` | VARCHAR2 | YES |  |  |
