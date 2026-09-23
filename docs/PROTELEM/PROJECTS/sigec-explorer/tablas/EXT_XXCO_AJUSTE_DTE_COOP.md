---
tipo: tabla
categoria: base
owner: XXSIGEC
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "EXT_XXCO_AJUSTE_DTE_COOP"
---

# 📋 EXT_XXCO_AJUSTE_DTE_COOP

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ADC_NEMO` | VARCHAR2 | YES |  |  |
| `ADC_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `ADC_MUNICIPIO` | VARCHAR2 | YES |  |  |
| `ADC_IMPORTE` | NUMBER | YES |  |  |
| `ADC_ANIO` | NUMBER | YES |  |  |
| `ADC_PERIODO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
