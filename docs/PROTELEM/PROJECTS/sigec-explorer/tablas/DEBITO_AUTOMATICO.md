---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1612080
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "DEBITO_AUTOMATICO"
---

# 📋 DEBITO_AUTOMATICO

**Filas estimadas:** 1,612,080

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DAU_NUMERO` | NUMBER | NO |  |  |
| `DAU_TIPO_REG` | VARCHAR2 | NO |  |  |
| `DAU_COD_TARJETA` | VARCHAR2 | NO |  |  |
| `DAU_NRO_TARJETA` | VARCHAR2 | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DAU_COD_MOV` | VARCHAR2 | YES |  |  |
| `DAU_FECHA_GENERACION` | DATE | YES |  |  |
| `DAU_FECHA_INICIO` | DATE | YES |  |  |
| `PRS_DOCUMENTO` | NUMBER | YES |  | Número de documento del titular en PERSONAS (NUMBER), con PRS_TIPO_DOC ('DNI', 'LC', 'LE', 'CI'…). Distinto de PRS_CUIT (que a veces está y a veces no). Es el 'número de documento del titular' de una consulta comercial. |
| `DAU_ESTADO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO_ORIGEN` | NUMBER | YES |  |  |
| `DAU_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `DAU_FECHA_ENVIO` | DATE | YES |  |  |
| `DAU_FECH_TARJETA` | NUMBER | YES |  |  |
| `ORDEN` | NUMBER | YES |  |  |
| `DAU_NUMERO_FINAN` | NUMBER | YES |  |  |
| `DAU_ARCHIVO` | VARCHAR2 | YES |  |  |
