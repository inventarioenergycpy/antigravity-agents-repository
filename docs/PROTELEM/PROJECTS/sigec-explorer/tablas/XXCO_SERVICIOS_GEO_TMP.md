---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: servicios
num_rows: 1
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_SERVICIOS_GEO_TMP"
---

# ⏱️ XXCO_SERVICIOS_GEO_TMP

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 1

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `SRV_CALLE` | VARCHAR2 | YES |  |  |
| `SRV_NRO` | NUMBER | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `SRV_GPS_LATITUD` | NUMBER | YES |  |  |
| `SRV_GPS_LONGITUD` | NUMBER | YES |  |  |
| `SRV_FECHA` | DATE | YES |  |  |
| `USR_ID` | NUMBER | YES |  |  |
| `SRV_FECHA_REGISTRO` | DATE | YES |  |  |
