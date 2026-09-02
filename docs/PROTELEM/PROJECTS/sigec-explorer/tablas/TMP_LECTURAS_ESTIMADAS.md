---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: contratos
num_rows: 381390
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/contratos
  - documentada/negocio
aliases:
  - "TMP_LECTURAS_ESTIMADAS"
---

# 📋 TMP_LECTURAS_ESTIMADAS

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 381,390

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LTE_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `LCT_CODIGO` | NUMBER | YES |  |  |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `LTE_ANIO` | NUMBER | YES |  |  |
| `LTE_PERIODO` | NUMBER | YES |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `LTE_FECHA_LECTURA_ESTIMADO` | DATE | YES |  |  |
| `LTE_CONSUMO_ESTIMADO` | NUMBER | YES |  |  |
| `LTE_TIPO_LECTURA_ESTIMADO` | VARCHAR2 | YES |  |  |
| `LTE_GRM_NUMERO` | NUMBER | YES |  |  |
| `LTE_EQP_ORDEN` | NUMBER | YES |  |  |
| `LTE_FECHA_ESTIMACION` | DATE | YES |  |  |
| `LTE_FECHA_VALIDACION` | DATE | YES |  |  |
| `LTE_USR_VALIDACION` | VARCHAR2 | YES |  |  |
| `LTE_VALOR_LEIDO_ESTIMADO` | NUMBER | YES |  |  |
| `LTE_VALOR_LEIDO_ANTERIOR` | NUMBER | YES |  |  |
| `LTE_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `LTE_DIF_MES_ANTERIOR` | NUMBER | YES |  |  |
| `LTE_DIF_ANIO_ANTERIOR` | NUMBER | YES |  |  |
| `LTE_CANT_DIAS_A_ESTIMAR` | NUMBER | YES |  |  |
| `LTE_PROM_DIARIO_ESTIMADO` | NUMBER | YES |  |  |
| `CDR_ORDEN` | NUMBER | YES |  |  |
| `LTE_CONS_GENERAL_SUM` | NUMBER | YES |  |  |
| `LTE_CONS_GENERAL_PROM` | NUMBER | YES |  |  |
| `LTE_DIF_CONS_EST_GENERAL` | NUMBER | YES |  |  |
| `LTE_PROM_CONS_EST_GENERAL` | NUMBER | YES |  |  |
| `LTE_CONSUMO_ESTIMADO_SC` | NUMBER | YES |  |  |
| `CNT_DIAS_VIGENCIA` | NUMBER | YES |  |  |
| `LTE_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `LTE_PORC_CERO` | NUMBER | YES |  |  |
| `LTE_PORC_EST` | NUMBER | YES |  |  |
| `RLE_CODIGO` | NUMBER | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `LTE_PORC_DIF_CONSUMO` | NUMBER | YES |  |  |
| `LTE_CONSUMO_X_ESTIMADOR` | NUMBER | YES |  |  |
| `LTE_VALOR_LEIDO_X_ESTIMADOR` | NUMBER | YES |  |  |
| `LTE_CONSUMO_VALIDADO` | NUMBER | YES |  |  |
| `LTE_VALOR_LEIDO_VALIDADO` | NUMBER | YES |  |  |
| `LTE_USR_MODIF_ESTIMACION` | NUMBER | YES |  |  |
| `LTE_USR_MODIF_FECHA` | DATE | YES |  |  |
| `LTE_CONSUMO_ANTES_MODIF_USR` | NUMBER | YES |  |  |
| `USR_NUMERO_ESTIMACION` | VARCHAR2 | YES |  |  |
| `LTE_VAL_LEIDO_ANTES_MODIF_USR` | NUMBER | YES |  |  |
| `RLE_NUMERO` | NUMBER | YES |  |  |
| `LTE_ESTADO` | VARCHAR2 | YES |  |  |
| `LTE_ORIGEN` | VARCHAR2 | YES |  |  |
| `LTE_GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `LTE_TCL_CODIGO` | VARCHAR2 | YES |  |  |
