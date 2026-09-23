---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 1655050
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "RECLAMOS"
---

# 📋 RECLAMOS

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 1,655,050

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `RCL_FRAUDE` | VARCHAR2 | YES |  |  |
| `RCL_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `PRS_NUMERO_DENUNCIADO` | NUMBER | YES | 🔗 → [[PERSONAS]] |  |
| `RCL_ANIO` | NUMBER | NO |  |  |
| `RCL_FECHA_RECEPCION` | DATE | NO |  |  |
| `RCL_FECHA_EST_RESOLUCION` | DATE | NO |  |  |
| `RCL_MEDIO_RECEPCION` | VARCHAR2 | NO |  |  |
| `RCL_CANT_REITERACION` | NUMBER | YES |  |  |
| `RCL_NOMBRE_ULT_REITERACION` | VARCHAR2 | YES |  |  |
| `RCL_ORIGEN` | VARCHAR2 | YES |  |  |
| `RCL_ESTADO` | VARCHAR2 | NO |  |  |
| `RCL_FUNDADO` | VARCHAR2 | YES |  |  |
| `RCL_OBSERVACION_RESOLUCION` | VARCHAR2 | YES |  |  |
| `RCL_OBSERVACION_RECEPCION` | VARCHAR2 | YES |  |  |
| `RCL_FECHA_ULT_REITERACION` | DATE | YES |  |  |
| `RCL_FECHA_REAL_RESOLUCION` | DATE | YES |  |  |
| `SEC_CODIGO` | VARCHAR2 | NO |  |  |
| `USR_NUMERO` | NUMBER | NO |  |  |
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `TRO_CODIGO` | VARCHAR2 | NO |  |  |
| `AGF_CODIGO` | NUMBER | NO |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `RCL_NRO_RECLAMO` | NUMBER | NO |  |  |
| `RCL_NRO_DENUNCIA` | NUMBER | NO |  |  |
| `RCL_FECHA_RESOL_LG` | DATE | YES |  | Fecha de resolucion del reclamo CON constatacion en terreno. NO tiene relacion con el area Legales pese al sufijo _LG. Verificado 2025: se puebla en 33.663 de 33.690 reclamos con acta en DATOS_RESULTADOS (99,92%) y en solo 11 de 153.069 sin acta (0,007%). RCL_FECHA_REAL_RESOLUCION esta vacia al 100%. |
| `TRO_CODIGO_HIJO` | VARCHAR2 | YES |  |  |
| `USR_NUMERO_MODIFICA` | NUMBER | YES |  |  |
| `RCL_RECLAMANTE` | VARCHAR2 | YES |  |  |
| `RCL_DIRECCION` | VARCHAR2 | YES |  |  |
| `RCL_CALLE` | VARCHAR2 | YES |  |  |
| `RCL_NRO` | VARCHAR2 | YES |  |  |
| `RCL_PISO` | VARCHAR2 | YES |  |  |
| `RCL_DEPTO` | VARCHAR2 | YES |  |  |
| `RCL_FECHA_CARGA` | DATE | YES |  |  |
| `RCL_RECHA_CONSOLIDACION` | DATE | YES |  |  |
| `RCL_FECHA_CONSOLIDACION` | DATE | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `TRT_NUMERO` | NUMBER | YES |  |  |
| `OPE_NUMERO` | NUMBER | YES | 🔗 → [[OPERATIVOS]] |  |
| `LIQ_NUMERO` | NUMBER | YES | 🔗 → [[LIQUIDACIONES_ILICITOS]] |  |
| `RCL_FECHA_PRESCRIPCION` | DATE | YES |  |  |
| `RCL_GPS_LATITUD` | NUMBER | YES |  |  |
| `RCL_GPS_LONGITUD` | NUMBER | YES |  |  |
| `RCL_DENOM_CATASTRAL` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **RCL_LIQ_FK**: `LIQ_NUMERO` → [[LIQUIDACIONES_ILICITOS]] (`LIQ_NUMERO`)
- **RCL_OPE_FK**: `OPE_NUMERO` → [[OPERATIVOS]] (`OPE_NUMERO`)
- **RCL_PRS_FK**: `PRS_NUMERO_DENUNCIADO` → [[PERSONAS]] (`PRS_NUMERO`)

## Tablas que referencian esta tabla

- [[ORDENATIVOS]] via `RCL_NUMERO`
- [[RECLAMOS_ASOCIADOS]] via `RCL_NUMERO`

## FK inferidas (alta confianza)

- `LIQ_NUMERO` → [[LIQUIDACIONES_ILICITOS]] _LIQ_NUMERO es PK de LIQUIDACIONES_ILICITOS_
- `OPE_NUMERO` → [[OPERATIVOS]] _OPE_NUMERO es PK de OPERATIVOS_
