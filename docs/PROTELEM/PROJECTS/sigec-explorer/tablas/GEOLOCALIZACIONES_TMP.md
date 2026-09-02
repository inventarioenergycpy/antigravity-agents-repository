---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: servicios
num_rows: 2493
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/servicios
  - documentada/negocio
aliases:
  - "GEOLOCALIZACIONES_TMP"
---

# ⏱️ GEOLOCALIZACIONES_TMP

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 2,493

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `DIRECCION` | VARCHAR2 | YES |  |  |
| `LATITUD` | VARCHAR2 | YES |  |  |
| `LONGITUD` | VARCHAR2 | YES |  |  |
| `POL_CODIGO` | VARCHAR2 | YES |  |  |
| `GRL_CODIGO` | NUMBER | YES |  |  |
| `CORREGIDO` | CHAR | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `SRV_ORDEN_LECTURA` | NUMBER | YES |  |  |
| `SRV_CODIGO_ANT` | NUMBER | YES |  |  |
| `SRV_ORDEN_LECTURA_ANT` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `POL_CODIGO` → [[XXAG_POLIGONOS]] _POL_CODIGO es PK de XXAG_POLIGONOS_
