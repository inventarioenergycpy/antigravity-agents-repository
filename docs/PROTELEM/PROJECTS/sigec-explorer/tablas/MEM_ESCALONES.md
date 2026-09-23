---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 15
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "MEM_ESCALONES"
---

# 📋 MEM_ESCALONES

**Filas estimadas:** 15

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CON_FECHA_VIGENCIA` | DATE | NO |  |  |
| `MES_NUMERO` | NUMBER | NO |  |  |
| `MES_CANTIDAD_DESDE` | NUMBER | NO |  |  |
| `MES_CANTIDAD_HASTA` | NUMBER | NO |  |  |
