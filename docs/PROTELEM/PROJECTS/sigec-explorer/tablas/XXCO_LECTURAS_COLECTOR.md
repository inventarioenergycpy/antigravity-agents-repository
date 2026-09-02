---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: equipos
num_rows: 87769980
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/equipos
  - documentada/negocio
aliases:
  - "XXCO_LECTURAS_COLECTOR"
---

# 🔧 XXCO_LECTURAS_COLECTOR

**Prefijo `STE_`:** Stock de equipos — atributos del medidor físico (STOCK_EQUIPOS)

> TAbla para descarga y procesamiento de descargas de colectoras

**Filas estimadas:** 87,769,980

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LCR_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | YES | 🔗 → [[CUADRANTES]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | YES | 🔗 → [[CUADRANTES]] |  |
| `EQP_ORDEN` | NUMBER | YES | 🔗 → [[CUADRANTES]] |  |
| `CDR_UNIDAD` | VARCHAR2 | YES | 🔗 → [[CUADRANTES]] |  |
| `LCR_FECHA_LECTURA` | DATE | YES |  |  |
| `LCR_VALOR_LEIDO` | NUMBER | YES |  |  |
| `LCR_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `LCR_VALOR_LEIDO_ANTERIOR` | NUMBER | YES |  |  |
| `LCR_CONSUMO` | NUMBER | YES |  |  |
| `LCR_CONSUMO_INFORMADO` | NUMBER | YES |  |  |
| `LCR_TIPO_CONSUMO` | VARCHAR2 | YES |  |  |
| `LCR_TIPO_LECTURA` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `LCR_ESTADO` | VARCHAR2 | YES |  |  |
| `LCR_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `LCR_FECHA_CARGA` | DATE | YES |  |  |
| `LCR_USR_CARGA_ACTU` | NUMBER | YES |  |  |
| `LCR_FECHA_CARGA_ACTU` | DATE | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `RTL_ANIO` | NUMBER | YES |  |  |
| `RTL_PERIODO` | NUMBER | YES |  |  |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CAT_CODIGO` | VARCHAR2 | YES |  |  |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `LCR_ORDEN_LECTURA` | NUMBER | YES |  |  |
| `LCR_ORDEN_LECTURA_ANTERIOR` | NUMBER | YES |  |  |
| `STE_TIPO` | VARCHAR2 | YES |  | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `USR_NUMERO_TOMA` | NUMBER | YES |  |  |
| `LCR_FECHA_ERROR` | DATE | YES |  |  |
| `LCR_ERROR` | VARCHAR2 | YES |  |  |
| `LCR_DESCRIPCION_ERROR` | VARCHAR2 | YES |  |  |
| `LCR_FECHA_PROCESO` | DATE | YES |  |  |
| `LCR_POSIBLE_SOLUCION` | VARCHAR2 | YES |  |  |
| `CDR_ENTEROS` | NUMBER | YES |  |  |
| `CDR_DECIMALES` | NUMBER | YES |  |  |
| `LCR_TIPO_CARGA` | VARCHAR2 | YES |  |  |
| `LCR_OBSERVACIONES_CIERRE` | VARCHAR2 | YES |  |  |
| `LCT_CODIGO` | NUMBER | YES |  |  |
| `LCR_FECHA_CIERRE` | DATE | YES |  |  |
| `USR_NUMERO_CIERRE` | NUMBER | YES |  |  |
| `LCR_VALOR_LEIDO_ORIGINAL` | NUMBER | YES |  |  |
| `USR_NUMERO_MODIFICA` | NUMBER | YES |  |  |
| `LCR_FECHA_MODIFICA` | DATE | YES |  |  |
| `LCR_FECHA_LECTURA_ORIGINAL` | DATE | YES |  |  |
| `LCR_ID_FOTO` | VARCHAR2 | YES |  |  |
| `LCR_GPS_LATITUD` | NUMBER | YES |  |  |
| `LCR_GPS_LONGITUD` | NUMBER | YES |  |  |
| `SLO_ORIGEN` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **LCR_FK_CDR**: `SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`, `CDR_UNIDAD` → [[CUADRANTES]] (`SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`, `CDR_UNIDAD`)

## FK inferidas (alta confianza)

- `USR_NUMERO_TOMA` → [[XXCO_ALTAS_COLECTOR]] _USR_NUMERO_TOMA es PK de XXCO_ALTAS_COLECTOR_
- `SLO_ORIGEN` → [[XXCO_SERVICIOS_LOCALIZACIONES]] _SLO_ORIGEN es PK de XXCO_SERVICIOS_LOCALIZACIONES_
- `RTL_ANIO` → [[XXCO_ALTAS_COLECTOR]] _RTL_ANIO es PK de XXCO_ALTAS_COLECTOR_
- `RTL_PERIODO` → [[XXCO_ALTAS_COLECTOR]] _RTL_PERIODO es PK de XXCO_ALTAS_COLECTOR_
- `LCR_FECHA_PROCESO` → [[XXCO_CRONOGRAMAS_LECTURA_TOT]] _LCR_FECHA_PROCESO es PK de XXCO_CRONOGRAMAS_LECTURA_TOT_
