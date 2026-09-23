---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 6095
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "TMP_EXCESO_DEM"
---

# 📋 TMP_EXCESO_DEM

**Filas estimadas:** 6,095

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `ANIO` | NUMBER | YES |  |  |
| `PER` | NUMBER | YES |  |  |
| `CDR_EP` | VARCHAR2 | YES |  |  |
| `VALOR_EP` | NUMBER | YES |  |  |
| `CDR_FP` | VARCHAR2 | YES |  |  |
| `VALOR_FP` | NUMBER | YES |  |  |
| `CDR_EP_LECT` | VARCHAR2 | YES |  |  |
| `VALOR_EP_LECT` | NUMBER | YES |  |  |
| `CDR_FP_LECT` | VARCHAR2 | YES |  |  |
| `VALOR_FP_LECT` | NUMBER | YES |  |  |
| `ITM_EP` | VARCHAR2 | YES |  |  |
| `CANT_ITM_EP` | NUMBER | YES |  |  |
| `TIT_FP` | VARCHAR2 | YES |  |  |
| `CANT_ITM_FP` | NUMBER | YES |  |  |
| `TMP_FECHA_PROCESO` | DATE | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `TRT_NUMERO` | NUMBER | YES |  |  |
