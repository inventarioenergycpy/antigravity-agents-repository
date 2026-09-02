---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 38355220
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "ORDENATIVOS"
---

# 📋 ORDENATIVOS

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 38,355,220

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TRT_NUMERO` | NUMBER | NO |  |  |
| `TOR_CODIGO` | VARCHAR2 | NO | 🔗 → [[TIPOS_ORDENATIVO]] |  |
| `ORD_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `ORD_FECHA_GENERACION` | DATE | NO |  |  |
| `SCF_CODIGO_ORIGEN` | NUMBER | NO | 🔗 → [[AGENCIAS]] |  |
| `SEC_CODIGO_ORIGEN` | VARCHAR2 | NO |  |  |
| `SCF_CODIGO_DESTINO` | NUMBER | NO | 🔗 → [[AGENCIAS]] |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | NO | 🔗 → [[SECTORES]] | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
| `ORD_FECHA_INICIO` | DATE | NO |  |  |
| `ORD_FECHA_VENCIMIENTO` | DATE | YES |  |  |
| `ORD_DATOS_ADICIONALES` | VARCHAR2 | YES |  |  |
| `ORD_PRIORIDAD` | NUMBER | NO |  |  |
| `ORD_RESULTADO` | VARCHAR2 | YES |  |  |
| `ORD_FECHA_FIN` | DATE | YES |  |  |
| `USR_CODIGO_RESULTADO` | VARCHAR2 | YES |  |  |
| `ORD_DATOS_RESULTADOS` | VARCHAR2 | YES |  |  |
| `ORD_FECHA_CARGA_RESULTADO` | DATE | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `ODT_NUMERO` | NUMBER | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES | 🔗 → [[PERSONAS]] | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `USR_NUMERO_ORIGEN` | NUMBER | YES |  |  |
| `USR_NUMERO_DESTINO` | NUMBER | YES |  |  |
| `ORD_SITUACION` | VARCHAR2 | NO |  |  |
| `ORD_ESTADO` | VARCHAR2 | NO |  |  |
| `SRV_CODIGO_ORIGEN` | NUMBER | YES |  |  |
| `CNT_NUMERO_ORIGEN` | NUMBER | YES |  |  |
| `TRT_NUMERO_ORIGEN` | NUMBER | YES |  |  |
| `ZOP_CODIGO` | VARCHAR2 | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `CNR_NUMERO` | NUMBER | YES |  |  |
| `USR_NUMERO_ANULA` | NUMBER | YES |  |  |
| `ORD_DATOS_ANULA` | VARCHAR2 | YES |  |  |
| `USR_IMPRIME` | NUMBER | YES |  |  |
| `ORD_FECHA_ANULA` | DATE | YES |  |  |
| `SCF_CODIGO_EXP` | NUMBER | YES |  |  |
| `EXP_NUMERO` | NUMBER | YES |  |  |
| `TIL_CODIGO` | VARCHAR2 | YES |  |  |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `STE_TIPO` | VARCHAR2 | YES |  | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `LCT_CODIGO` | NUMBER | YES |  |  |
| `RCL_NUMERO` | NUMBER | YES | 🔗 → [[RECLAMOS]] |  |
| `USR_RESULTADO` | NUMBER | YES |  |  |
| `PCL_NUMERO` | VARCHAR2 | YES |  |  |
| `AGE_CODIGO_ORIGEN` | VARCHAR2 | YES | 🔗 → [[AGENCIAS]] |  |
| `AGE_CODIGO_DESTINO` | VARCHAR2 | YES | 🔗 → [[AGENCIAS]] |  |
| `PROJECT_NUMBER` | NUMBER | YES |  |  |
| `ORD_PROC_CORREO` | VARCHAR2 | YES |  |  |
| `USR_NUMERO_EJEC_ORD` | NUMBER | YES |  |  |
| `LOR_NUMERO` | NUMBER | YES |  |  |
| `SIN_NUMERO` | NUMBER | YES |  |  |
| `LOR_NUMERO_PADRE` | NUMBER | YES |  |  |
| `ORD_FECHA_INICIO_ORIGINAL` | DATE | YES |  |  |
| `ORD_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
| `SRV_TELEMEDIBLE` | VARCHAR2 | YES |  |  |
| `APP_ID` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **ORD_AGE_DESTINO_FK**: `SCF_CODIGO_DESTINO`, `AGE_CODIGO_DESTINO` → [[AGENCIAS]] (`SCF_CODIGO`, `AGE_CODIGO`)
- **ORD_AGE_ORIGEN_FK**: `SCF_CODIGO_ORIGEN`, `AGE_CODIGO_ORIGEN` → [[AGENCIAS]] (`SCF_CODIGO`, `AGE_CODIGO`)
- **ORD_FK_RCL**: `RCL_NUMERO` → [[RECLAMOS]] (`RCL_NUMERO`)
- **ORD_PRS_FK**: `PRS_NUMERO` → [[PERSONAS]] (`PRS_NUMERO`)
- **ORD_SEC_DESTINO_FK**: `SEC_CODIGO_DESTINO` → [[SECTORES]] (`SEC_CODIGO`)
- **ORD_TOR_FK**: `TOR_CODIGO` → [[TIPOS_ORDENATIVO]] (`TOR_CODIGO`)

## Tablas que referencian esta tabla

- [[XXCO_DATOS_INSPECCION]] via `ORD_NUMERO`
- [[XXCO_EQUIPO_TRANSFORMADORES]] via `ORD_NUMERO`
- [[XXCO_LECTURAS_LABORATORIO]] via `ORD_NUMERO`
- [[XXCO_MEDICIONES]] via `ORD_NUMERO`
- [[XXCO_PRECINTOS]] via `ORD_NUMERO`

## FK inferidas (alta confianza)

- `APP_ID` → [[XXCO_OBSERVACIONES_ORDENATIVO]] _APP_ID es PK de XXCO_OBSERVACIONES_ORDENATIVO_
- `SIN_NUMERO` → [[XXCO_OBSERVACIONES_ORDENATIVO]] _SIN_NUMERO es PK de XXCO_OBSERVACIONES_ORDENATIVO_
- `ODT_NUMERO` → [[ORDENATIVOS_TEMP]] _ODT_NUMERO es PK de ORDENATIVOS_TEMP_
- `LOR_NUMERO` → [[XXCO_LOTE_ORDENATIVOS_MOV]] _LOR_NUMERO es PK de XXCO_LOTE_ORDENATIVOS_MOV_
