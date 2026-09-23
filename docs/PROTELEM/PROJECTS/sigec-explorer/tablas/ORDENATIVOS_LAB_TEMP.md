---
tipo: tabla
categoria: temp
owner: XXSIGEC
num_rows: 2
tags:
  - sigec-explorer
  - tabla
  - temp
  - documentada/negocio
aliases:
  - "ORDENATIVOS_LAB_TEMP"
---

# ⏱️ ORDENATIVOS_LAB_TEMP

**Filas estimadas:** 2

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TOR_CODIGO` | VARCHAR2 | NO |  |  |
| `ORD_NUMERO` | NUMBER | NO |  |  |
| `GRM_NUMERO` | NUMBER | YES |  |  |
| `EEQ_CARGA_MAXIMA` | NUMBER | YES |  |  |
| `EEQ_CARGA_MINIMA` | NUMBER | YES |  |  |
| `EEQ_PORCENTAJE_ERROR` | NUMBER | YES |  |  |
| `ORD_RESULTADO` | VARCHAR2 | YES |  |  |
| `ORD_FECHA_CARGA_RESULTADO` | DATE | YES |  |  |
| `ORD_DATOS_RESULTADOS` | VARCHAR2 | YES |  |  |
| `EQP_ORDEN` | NUMBER | YES |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `TRT_NUMERO` | NUMBER | YES |  |  |
