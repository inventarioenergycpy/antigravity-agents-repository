---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 42017
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_VALIDACIONES_CNT_ORD"
---

# 🔧 XXCO_VALIDACIONES_CNT_ORD

**Filas estimadas:** 42,017

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CRF_ANIO` | NUMBER | YES |  |  |
| `CRF_PERIODO` | NUMBER | YES |  |  |
| `CRF_ANIO2` | NUMBER | YES |  |  |
| `CRF_PERIODO2` | NUMBER | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `USR_CARGA` | NUMBER | YES |  |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `ORD_NUMERO` | NUMBER | YES |  |  |
| `VOR_RES_ES_PROBLEMA` | VARCHAR2 | YES |  |  |
