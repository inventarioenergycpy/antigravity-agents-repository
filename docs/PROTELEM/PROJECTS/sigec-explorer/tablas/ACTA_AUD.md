---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 210697
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "ACTA_AUD"
---

# 📋 ACTA_AUD

**Filas estimadas:** 210,697

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DRE_CONSUMO_ESTIMADO` | NUMBER | YES |  |  |
| `DRE_ENERGIA_NO_REG` | NUMBER | YES |  |  |
| `DRE_FECHA_DESDE` | DATE | YES |  |  |
| `DRE_FECHA_HASTA` | DATE | YES |  |  |
| `DRE_PERIODO` | NUMBER | YES |  |  |
| `DRE_PROM_ESTIMADO` | NUMBER | YES |  |  |
| `DRE_PROM_REGISTRADO` | NUMBER | YES |  |  |
| `RCL_NUMERO` | NUMBER | YES |  |  |
| `DRE_NRO_ACTA_INSPECCION` | VARCHAR2 | YES |  |  |
| `AUD_FECHA` | DATE | YES |  |  |
| `AUD_USUARIO` | NUMBER | YES |  |  |
| `AUD_OBSERVACION` | VARCHAR2 | YES |  |  |
| `DRE_ESTADO` | VARCHAR2 | YES |  |  |
| `TRT_NUMERO` | NUMBER | YES |  |  |
| `DRE_FECHA_TRANSMISION` | DATE | YES |  |  |
| `DRE_NOMBRE_DUENIO` | VARCHAR2 | YES |  |  |
| `DRE_OBSERVACION_ACTA` | VARCHAR2 | YES |  |  |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `DRE_FASE_R` | NUMBER | YES |  |  |
| `DRE_FASE_S` | NUMBER | YES |  |  |
| `DRE_FASE_T` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `DRE_FORMULA_ESTIMACION` | VARCHAR2 | YES |  |  |
