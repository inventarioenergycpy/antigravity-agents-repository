---
tipo: tabla
categoria: hist
owner: XXSIGEC
dominio: servicios
num_rows: 4268950
tags:
  - sigec-explorer
  - tabla
  - hist
  - dominio/servicios
  - documentada/negocio
aliases:
  - "ORDENATIVOS_HIST"
---

# 📂 ORDENATIVOS_HIST

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 4,268,950

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TRT_NUMERO` | NUMBER | NO |  |  |
| `TOR_CODIGO` | VARCHAR2 | NO |  |  |
| `ORD_NUMERO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `ORD_FECHA_GENERACION` | DATE | NO |  |  |
| `SCF_CODIGO_ORIGEN` | NUMBER | NO |  |  |
| `SEC_CODIGO_ORIGEN` | VARCHAR2 | NO |  |  |
| `SCF_CODIGO_DESTINO` | NUMBER | NO |  |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | NO |  | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
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
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
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
| `RCL_NUMERO` | NUMBER | YES |  |  |
| `USR_RESULTADO` | NUMBER | YES |  |  |
| `PCL_NUMERO` | VARCHAR2 | YES |  |  |
| `AGE_CODIGO_ORIGEN` | VARCHAR2 | YES |  |  |
| `AGE_CODIGO_DESTINO` | VARCHAR2 | YES |  |  |
| `PROJECT_NUMBER` | NUMBER | YES |  |  |
| `ORD_PROC_CORREO` | VARCHAR2 | YES |  |  |
| `USR_NUMERO_EJEC_ORD` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ODT_NUMERO` → [[ORDENATIVOS_TEMP]] _ODT_NUMERO es PK de ORDENATIVOS_TEMP_
