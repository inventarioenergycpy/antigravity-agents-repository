---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 3379713
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_SERVICIOS_LOCALIZACIONES"
---

# 🔧 XXCO_SERVICIOS_LOCALIZACIONES

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 3,379,713

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `SLO_ORIGEN` | VARCHAR2 | NO | 🔑 PK |  |
| `SLO_FECHA` | DATE | YES |  |  |
| `SLO_LAT_DEC` | NUMBER | YES |  |  |
| `SLO_LON_DEC` | NUMBER | YES |  |  |
| `SLO_FECHA_CARGA` | DATE | YES |  |  |
