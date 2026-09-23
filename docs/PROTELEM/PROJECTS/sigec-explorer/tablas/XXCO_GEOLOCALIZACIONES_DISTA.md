---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 1030
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_GEOLOCALIZACIONES_DISTA"
---

# 🔧 XXCO_GEOLOCALIZACIONES_DISTA

**Filas estimadas:** 1,030

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `LAT_GPS` | NUMBER | YES |  |  |
| `LON_GPS` | NUMBER | YES |  |  |
| `LAT_3G` | NUMBER | YES |  |  |
| `LON_3G` | NUMBER | YES |  |  |
| `DISTANCIA` | NUMBER | YES |  |  |
