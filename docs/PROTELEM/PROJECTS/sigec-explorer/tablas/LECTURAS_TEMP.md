---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: lecturas
num_rows: 96203
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "LECTURAS_TEMP"
---

# ⏱️ LECTURAS_TEMP

**Prefijo `LTM_`:** Lecturas temporales (LECTURAS_TEMP)

**Filas estimadas:** 96,203

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LTM_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `STE_TIPO` | VARCHAR2 | YES |  | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `LTM_ENTEROS` | NUMBER | YES |  |  |
| `LTM_FECHA_LECTURA` | DATE | YES |  |  |
| `LTM_VALOR_LEIDO` | NUMBER | YES |  |  |
| `LTM_ORDEN_LECTURA` | NUMBER | YES |  |  |
| `LTM_ANORMALIDAD` | VARCHAR2 | YES |  |  |
| `SRV_PLAN_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_ZONA_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_LOCALIDAD_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_RUTA_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_SUMINISTRO_ORIGINAL` | NUMBER | YES |  | Clave del suministro propagada a tablas de lectura/facturación. |
| `LTM_TIPO_REGISTRO` | VARCHAR2 | YES |  |  |
| `LTM_TITULAR` | VARCHAR2 | YES |  |  |
| `LTM_DOMICILIO` | VARCHAR2 | YES |  |  |
| `LTM_ACTIVIDAD` | VARCHAR2 | YES |  |  |
| `CAT_CODIGO` | NUMBER | YES |  |  |
| `LTM_NOTAS` | VARCHAR2 | YES |  |  |
| `LTM_OBSERVACION` | VARCHAR2 | YES |  |  |
| `USR_CODIGO` | VARCHAR2 | YES |  |  |
| `LTM_ERROR` | VARCHAR2 | YES |  |  |
| `LTM_DIFERENCIA` | NUMBER | YES |  |  |
| `EQP_ORDEN` | NUMBER | YES |  |  |
| `GRM_NUMERO` | NUMBER | YES |  |  |
| `LTM_TIPO_LECTURA` | VARCHAR2 | YES |  |  |
| `LTM_CONSUMO_INFORMADO` | NUMBER | YES |  |  |
| `LTM_NUEVO_EQUIPO` | VARCHAR2 | YES |  |  |
| `LTM_EQUIPO_RETIRADO` | VARCHAR2 | YES |  |  |
| `LTM_ARRASTRE` | VARCHAR2 | YES |  |  |
| `LTM_CAMBIA_RUTA` | VARCHAR2 | YES |  |  |
| `ORA_ERROR` | NUMBER | YES |  |  |
| `LTM_SESSION_ID` | NUMBER | YES |  |  |
| `LTM_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `LTM_DECIMALES` | NUMBER | YES |  |  |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `PCL_NUMERO` | NUMBER | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `LTM_ACCESO_MEDIDOR` | VARCHAR2 | YES |  |  |
| `LTM_GPS_LATITUD` | NUMBER | YES |  |  |
| `LTM_GPS_LONGITUD` | NUMBER | YES |  |  |
| `LTM_FECHA_CARGA` | DATE | YES |  |  |
