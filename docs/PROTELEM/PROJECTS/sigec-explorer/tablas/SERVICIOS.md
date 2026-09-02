---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 1554360
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "SERVICIOS"
---

# 📋 SERVICIOS

> [!info] Significado de negocio
> Puntos de suministro (conexiones de servicio eléctrico).

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 1,554,360

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `AGE_CODIGO` | VARCHAR2 | NO |  |  |
| `RTA_CODIGO` | NUMBER | NO |  |  |
| `SRV_ORDEN_LECTURA` | NUMBER | YES |  |  |
| `SRV_DIRECCION` | VARCHAR2 | YES |  |  |
| `SRV_CALLE` | VARCHAR2 | YES |  |  |
| `SRV_NRO` | NUMBER | YES |  |  |
| `SRV_PISO` | VARCHAR2 | YES |  |  |
| `SRV_DEPTO` | VARCHAR2 | YES |  |  |
| `SRV_C_POSTAL` | NUMBER | YES |  |  |
| `AGF_CODIGO` | NUMBER | NO |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `SRV_FECHA_INSTAL` | DATE | YES |  |  |
| `SRV_FECHA_BAJA` | DATE | YES |  |  |
| `SRV_MOTIVO_BAJA` | VARCHAR2 | YES |  |  |
| `SRV_PLAN_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_ZONA_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_LOCALIDAD_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_RUTA_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_SUMINISTRO_ORIGINAL` | NUMBER | YES |  | Clave del suministro propagada a tablas de lectura/facturación. |
| `SRV_PROMEDIO_VERANO` | NUMBER | YES |  |  |
| `SRV_PROMEDIO_INVIERNO` | NUMBER | YES |  |  |
| `SRV_PROMEDIO_ANUAL` | NUMBER | YES |  |  |
| `SRV_TIPO_SUMINISTRO` | VARCHAR2 | YES |  |  |
| `EDI_NUMERO` | NUMBER | YES |  |  |
| `ERD_CODIGO` | NUMBER | YES |  |  |
| `SRV_DISTRITO_CAT` | VARCHAR2 | YES |  |  |
| `SRV_ZONA_CAT` | VARCHAR2 | YES |  |  |
| `SRV_MANZANA_CAT` | VARCHAR2 | YES |  |  |
| `SRV_LOTE_CAT` | VARCHAR2 | YES |  |  |
| `SRV_ESTADO` | VARCHAR2 | NO |  |  |
| `SRV_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `SRV_TORRE` | VARCHAR2 | YES |  |  |
| `SRV_ORDEN_LECTURA_ANTERIOR` | NUMBER | YES |  |  |
| `SRV_CALIBRACION_FUSIBLE` | NUMBER | YES |  |  |
| `SRV_DISTRIBUIDOR_TEC` | VARCHAR2 | YES |  |  |
| `SRV_SALIDA_TEC` | VARCHAR2 | YES |  |  |
| `SRV_SEA_TEC` | VARCHAR2 | YES |  |  |
| `SRV_SUBESTACION_TEC` | VARCHAR2 | YES |  |  |
| `SRV_TIPO_DISTRIB_TEC` | VARCHAR2 | YES |  |  |
| `GSE_GRUPO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO_2` | NUMBER | YES |  |  |
| `RTC_CODIGO` | NUMBER | YES |  |  |
| `SRV_CONTROLADO_EN_RTC_SCF_CODI` | NUMBER | YES |  |  |
| `SRV_ORDEN_LECTURA_CONTROL` | NUMBER | YES |  |  |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `SRV_LOCAL` | VARCHAR2 | YES |  |  |
| `SRV_OFICINA` | VARCHAR2 | YES |  |  |
| `EID_NUMERO` | NUMBER | YES |  |  |
| `SRV_DISTRITO_CATA` | NUMBER | YES |  |  |
| `SRV_ZONA_CATA` | NUMBER | YES |  |  |
| `SRV_MANZANA_CATA` | NUMBER | YES |  |  |
| `SRV_LOTE_CATA` | NUMBER | YES |  |  |
| `SRV_PH_CATA` | NUMBER | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `SRV_ACCESO_MEDIDOR` | VARCHAR2 | YES |  |  |
| `SRV_GPS_LATITUD` | NUMBER | YES |  |  |
| `SRV_GPS_LONGITUD` | NUMBER | YES |  |  |
| `BAR_CODIGO` | VARCHAR2 | YES |  |  |
| `SLO_ORIGEN` | VARCHAR2 | YES |  |  |
| `AGE_CODIGO_PROX` | VARCHAR2 | YES |  |  |
| `C_REPAR_GUARDIA` | NUMBER | YES |  |  |
| `NRO_CERT_LEY_10281` | VARCHAR2 | YES |  |  |
| `VIGENCIA_CERT_LEY_10281` | DATE | YES |  |  |
| `PRESENTA_CERT_LEY_10281` | VARCHAR2 | YES |  |  |
| `SRV_CALLE_GEO` | VARCHAR2 | YES |  |  |
| `SRV_LOTE` | NUMBER | YES |  |  |
| `SRV_MANZANA` | NUMBER | YES |  |  |
| `SRV_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
| `SRV_TELEMEDIBLE` | VARCHAR2 | YES |  |  |
| `SRV_TELEMEDIBLE_DESDE` | DATE | YES |  |  |
| `SRV_ULTIMA_ACTUALIZACION_MDM` | DATE | YES |  |  |
| `SRV_DENOM_CATASTRAL` | VARCHAR2 | YES |  |  |
| `EDI_PARTICIPACION` | NUMBER | YES |  |  |
| `EDI_UNIDAD_TIPO` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `AGE_CODIGO` → [[AGENCIAS]] _AGE_CODIGO es PK de AGENCIAS_
- `ERD_CODIGO` → [[ELEMENTOS]] _ERD_CODIGO es PK de ELEMENTOS_
- `BAR_CODIGO` → [[XXCO_BARRIOS]] _BAR_CODIGO es PK de XXCO_BARRIOS_
- `GSE_GRUPO` → [[GRUPOS_SERVICIO]] _GSE_GRUPO es PK de GRUPOS_SERVICIO_
- `RTC_CODIGO` → [[RUTAS_CONTROL]] _RTC_CODIGO es PK de RUTAS_CONTROL_
- `SLO_ORIGEN` → [[XXCO_SERVICIOS_LOCALIZACIONES]] _SLO_ORIGEN es PK de XXCO_SERVICIOS_LOCALIZACIONES_
