---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "SUB_RUTAS"
---

# 📋 SUB_RUTAS

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `RTA_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `SBR_FECHA_LECTURA` | DATE | YES |  |  |
| `SBR_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
