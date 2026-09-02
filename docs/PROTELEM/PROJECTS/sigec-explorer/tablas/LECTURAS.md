---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 222965550
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "LECTURAS"
---

# 📋 LECTURAS

> [!info] Significado de negocio
> Lecturas/mediciones de consumo (~223M filas). NO tiene columna de medidor: se une a EQUIPOS por (SRV_CODIGO, GRM_NUMERO, EQP_ORDEN). Filtrar SIEMPRE antes de consultar.

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 222,965,550

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LCT_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | NO | 🔗 → [[CUADRANTES]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO | 🔗 → [[CUADRANTES]] |  |
| `EQP_ORDEN` | NUMBER | NO | 🔗 → [[CUADRANTES]] |  |
| `CDR_UNIDAD` | VARCHAR2 | NO | 🔗 → [[CUADRANTES]] |  |
| `LCT_FECHA_LECTURA` | DATE | NO |  | Fecha en que se tomó la lectura. |
| `LCT_VALOR_LEIDO` | NUMBER | NO |  | Valor leído del medidor en esa lectura (estado del contador). |
| `LCT_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `LCT_VALOR_LEIDO_ANTERIOR` | NUMBER | YES |  |  |
| `LCT_CONSUMO` | NUMBER | YES |  | Consumo calculado del período (diferencia entre lecturas). |
| `LCT_CONSUMO_INFORMADO` | NUMBER | YES |  |  |
| `LCT_TIPO_CONSUMO` | VARCHAR2 | YES |  |  |
| `LCT_TIPO_LECTURA` | VARCHAR2 | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `LCT_ANORMALIDAD` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `LCT_ESTADO` | VARCHAR2 | YES |  |  |
| `LCT_ORIGEN` | VARCHAR2 | YES |  |  |
| `LCT_DIVIDIDA` | VARCHAR2 | YES |  |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `LCT_SALDO_CONSUMO` | NUMBER | YES |  |  |
| `LCT_SALDO_DIAS` | NUMBER | YES |  |  |
| `LCT_CUOTA` | NUMBER | YES |  |  |
| `LCT_ACTUALIZADO` | VARCHAR2 | YES |  |  |
| `LCT_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `LCT_MARCA_RESTAURACION` | NUMBER | YES |  |  |
| `USR_NUMERO_MODIFICA` | NUMBER | YES |  |  |
| `LCT_ENLACE_DET` | NUMBER | YES |  |  |
| `LCT_FECHA_CARGA` | DATE | YES |  |  |
| `LCT_GPS_LATITUD` | NUMBER | YES |  |  |
| `LCT_GPS_LONGITUD` | NUMBER | YES |  |  |
| `LCT_USR_CARGA_ACTU` | NUMBER | YES |  |  |
| `LCT_ANIO` | NUMBER | YES |  |  |
| `LCT_PERIODO` | NUMBER | YES |  |  |
| `USR_NUMERO_TOMA` | NUMBER | YES |  |  |
| `LCR_NUMERO` | NUMBER | YES |  |  |
| `LCT_FECHA_ACTUALIZACION` | DATE | YES |  |  |
| `LCT_CODIGO_ORIGEN` | NUMBER | YES |  |  |
| `LCT_FOTO` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **LCT_FK_CDR**: `SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`, `CDR_UNIDAD` → [[CUADRANTES]] (`SRV_CODIGO`, `GRM_NUMERO`, `EQP_ORDEN`, `CDR_UNIDAD`)

## FK inferidas (alta confianza)

- `USR_NUMERO_TOMA` → [[XXCO_ALTAS_COLECTOR]] _USR_NUMERO_TOMA es PK de XXCO_ALTAS_COLECTOR_
