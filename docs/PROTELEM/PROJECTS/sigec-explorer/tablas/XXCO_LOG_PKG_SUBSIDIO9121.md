---
tipo: tabla
categoria: custom
owner: XXSIGEC
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_LOG_PKG_SUBSIDIO9121"
---

# 🔧 XXCO_LOG_PKG_SUBSIDIO9121

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LOG_SESSION` | NUMBER | YES |  |  |
| `LOG_OK_ERROR` | VARCHAR2 | YES |  |  |
| `LOG_OBSERVACION` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `IAF_DETALLE` | VARCHAR2 | YES |  |  |
| `IAF_IMPORTE` | NUMBER | YES |  |  |
