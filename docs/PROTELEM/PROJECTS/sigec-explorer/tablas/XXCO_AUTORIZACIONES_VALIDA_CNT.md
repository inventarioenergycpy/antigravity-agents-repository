---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 3494390
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_AUTORIZACIONES_VALIDA_CNT"
---

# 🔧 XXCO_AUTORIZACIONES_VALIDA_CNT

**Filas estimadas:** 3,494,390

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `GRL_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `CRF_ANIO` | NUMBER | NO | 🔑 PK |  |
| `CRF_PERIODO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `VLE_VALIDACION` | VARCHAR2 | NO | 🔑 PK |  |
| `AVC_FECHA` | DATE | NO | 🔑 PK |  |
| `USR_NUMERO` | NUMBER | NO |  |  |
| `AVC_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `AVC_ANULA_AUTORIZACION` | VARCHAR2 | YES |  |  |
