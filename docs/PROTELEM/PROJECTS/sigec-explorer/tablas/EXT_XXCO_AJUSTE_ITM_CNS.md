---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "EXT_XXCO_AJUSTE_ITM_CNS"
---

# 📋 EXT_XXCO_AJUSTE_ITM_CNS

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `AIC_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `AIC_ANIO` | NUMBER | YES |  |  |
| `AIC_PERIODO` | NUMBER | YES |  |  |
| `AIC_IMPORTE` | NUMBER | YES |  |  |
