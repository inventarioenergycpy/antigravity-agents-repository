---
tipo: tabla
categoria: temp
owner: XXSIGEC
num_rows: 199357
tags:
  - sigec-explorer
  - tabla
  - temp
  - documentada/negocio
aliases:
  - "DEBITO_AUTOMATICO_TEMP"
---

# ⏱️ DEBITO_AUTOMATICO_TEMP

**Filas estimadas:** 199,357

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DAT_NUMERO` | NUMBER | NO |  |  |
| `DAT_TIPO_REG` | VARCHAR2 | NO |  |  |
| `DAT_COD_TARJETA` | VARCHAR2 | NO |  |  |
| `DAT_NRO_TARJETA` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DAT_COD_MOV` | VARCHAR2 | YES |  |  |
| `DAT_FECHA` | DATE | YES |  |  |
| `DAT_TOT_INEXIS` | NUMBER | YES |  |  |
| `DAT_TOT_ALTAS` | NUMBER | YES |  |  |
| `DAT_TOT_BAJAS` | NUMBER | YES |  |  |
| `DAT_TOT_BIMES` | NUMBER | YES |  |  |
| `DAT_ESTADO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO_ORIGEN` | NUMBER | YES |  |  |
| `USR_CODIGO_CARGA` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_INEXIS` | NUMBER | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `DAT_FECH_TARJETA` | NUMBER | YES |  |  |
| `ORDEN` | NUMBER | YES |  |  |
| `DAT_NUMERO_FINAN` | NUMBER | YES |  |  |
