---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: servicios
num_rows: 139303
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_MAPA_ORD_3160_TMP"
---

# ⏱️ XXCO_MAPA_ORD_3160_TMP

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 139,303

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SESSIONID` | NUMBER | NO |  |  |
| `MAPA_TMP_ID` | NUMBER | NO |  |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `ORD_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SRV_GPS_LATITUD` | NUMBER | YES |  |  |
| `SRV_GPS_LONGITUD` | NUMBER | YES |  |  |
| `SLO_ORIGEN` | VARCHAR2 | YES |  |  |
| `SRV_CALLE` | VARCHAR2 | YES |  |  |
| `SRV_NRO` | NUMBER | YES |  |  |
| `USR_CODIGO` | VARCHAR2 | YES |  |  |
| `ORIGEN_MAPA` | NUMBER | YES |  |  |
| `LOR_NUMERO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `LOR_NUMERO` → [[XXCO_LOTE_ORDENATIVOS_MOV]] _LOR_NUMERO es PK de XXCO_LOTE_ORDENATIVOS_MOV_
- `SLO_ORIGEN` → [[XXCO_SERVICIOS_LOCALIZACIONES]] _SLO_ORIGEN es PK de XXCO_SERVICIOS_LOCALIZACIONES_
