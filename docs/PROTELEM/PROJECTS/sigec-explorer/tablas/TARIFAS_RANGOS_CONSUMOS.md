---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 399
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "TARIFAS_RANGOS_CONSUMOS"
---

# 📋 TARIFAS_RANGOS_CONSUMOS

**Filas estimadas:** 399

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TAB_NUMERO` | NUMBER | YES |  |  |
| `TCL_CODIGO_GRAL` | VARCHAR2 | YES |  | Código de tarifa 'general' en AUDITORIA_CAMMESA. Se une a TARIFAS.TCL_CODIGO para clasificar el consumo por sector/rubro (vía TARIFAS.TCL_GRUPO). |
| `CLA_CODIGO_GRAL` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO_GRAL` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `TAB_FECHA_VIGENCIA` | DATE | YES |  |  |
| `TAB_CONSUMO_DESDE` | NUMBER | YES |  |  |
| `TAB_CONSUMO_HASTA` | NUMBER | YES |  |  |
| `CRITERIO_ALT` | VARCHAR2 | YES |  |  |
| `PEN_PENALIZA_COS_FI` | VARCHAR2 | YES |  |  |
