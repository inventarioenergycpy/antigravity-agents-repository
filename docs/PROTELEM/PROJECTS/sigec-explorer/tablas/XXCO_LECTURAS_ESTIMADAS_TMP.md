---
tipo: tabla
categoria: temp
owner: XXSIGEC
num_rows: 287957
tags:
  - sigec-explorer
  - tabla
  - temp
  - documentada/negocio
aliases:
  - "XXCO_LECTURAS_ESTIMADAS_TMP"
---

# ⏱️ XXCO_LECTURAS_ESTIMADAS_TMP

**Filas estimadas:** 287,957

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CONSUMO_ESTIMADO_P` | NUMBER | YES |  |  |
| `ANIO` | NUMBER | YES |  |  |
| `PERIODO` | NUMBER | YES |  |  |
| `CONSUMO_ESTIMADO_T` | NUMBER | YES |  |  |
