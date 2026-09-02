---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: equipos
num_rows: 8905140
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/equipos
  - documentada/negocio
aliases:
  - "INTERFAZ_MED_ORD"
---

# 📋 INTERFAZ_MED_ORD

**Prefijo `STE_`:** Stock de equipos — atributos del medidor físico (STOCK_EQUIPOS)

**Filas estimadas:** 8,905,140

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `IMD_ID` | NUMBER | NO | 🔑 PK |  |
| `IMD_FECHA` | DATE | NO |  |  |
| `TOR_CODIGO` | VARCHAR2 | NO |  |  |
| `ORD_NUMERO` | NUMBER | NO |  |  |
| `ORD_RESULTADO` | VARCHAR2 | NO |  |  |
| `SRV_CODIGO` | NUMBER | YES | 🔗 → [[CONTRATOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES | 🔗 → [[CONTRATOS]] | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | YES | 🔗 → [[PERSONAS]] | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `STE_TIPO_INST` | VARCHAR2 | YES |  |  |
| `STE_NUMERO_INST` | NUMBER | YES |  |  |
| `EQP_PRECINTO` | VARCHAR2 | YES |  |  |
| `STE_TIPO_RET` | VARCHAR2 | YES |  |  |
| `STE_NUMERO_RET` | NUMBER | YES |  |  |
| `COD_ERROR` | NUMBER | YES |  |  |
| `IMD_DESCRIPCION_ERROR` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `IMD_FECHA_PROC` | DATE | NO |  |  |
| `SEC_CODIGO` | VARCHAR2 | NO | 🔗 → [[SECTORES]] |  |
| `SCF_CODIGO` | NUMBER | NO | 🔗 → [[AGENCIAS]] |  |
| `AGE_CODIGO` | VARCHAR2 | NO | 🔗 → [[AGENCIAS]] |  |
| `USR_NUMERO_PROCESO` | NUMBER | YES |  |  |
| `USR_NUMERO_EJEC_ORD` | NUMBER | YES |  |  |
| `IMD_DATOS_ADICIONALES` | VARCHAR2 | YES |  |  |
| `TRT_NUMERO` | NUMBER | YES |  |  |
| `EQP_FACTOR_INTENSIDAD` | NUMBER | YES |  |  |
| `EQP_FACTOR_TENSION` | NUMBER | YES |  |  |
| `EQP_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `APP_ID` | NUMBER | YES |  |  |
| `SIN_NUMERO` | NUMBER | YES |  |  |
| `SIN_DIRECCION` | VARCHAR2 | YES |  |  |
| `ORD_EJECUTADO` | VARCHAR2 | YES |  |  |
| `TOB_CODIGO` | VARCHAR2 | YES |  |  |
| `IMD_FECHA_RESOLUCION` | DATE | YES |  |  |
| `APP_ORD_NRO_CAMPO_INTERNO` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **IMD_AGE_FK**: `SCF_CODIGO`, `AGE_CODIGO` → [[AGENCIAS]] (`SCF_CODIGO`, `AGE_CODIGO`)
- **IMD_CNT_FK**: `SRV_CODIGO`, `CNT_NUMERO` → [[CONTRATOS]] (`SRV_CODIGO`, `CNT_NUMERO`)
- **IMD_PER_FK**: `PRS_NUMERO` → [[PERSONAS]] (`PRS_NUMERO`)
- **IMD_SEC_FK**: `SEC_CODIGO` → [[SECTORES]] (`SEC_CODIGO`)

## Tablas que referencian esta tabla

- [[INTERFAZ_MED_ITEMS]] via `IMD_ID`

## FK inferidas (alta confianza)

- `AGE_CODIGO` → [[AGENCIAS]] _AGE_CODIGO es PK de AGENCIAS_
- `APP_ID` → [[XXCO_OBSERVACIONES_ORDENATIVO]] _APP_ID es PK de XXCO_OBSERVACIONES_ORDENATIVO_
- `SIN_NUMERO` → [[XXCO_OBSERVACIONES_ORDENATIVO]] _SIN_NUMERO es PK de XXCO_OBSERVACIONES_ORDENATIVO_
- `TOB_CODIGO` → [[XXCO_OBSERVACIONES_ORDENATIVO]] _TOB_CODIGO es PK de XXCO_OBSERVACIONES_ORDENATIVO_
