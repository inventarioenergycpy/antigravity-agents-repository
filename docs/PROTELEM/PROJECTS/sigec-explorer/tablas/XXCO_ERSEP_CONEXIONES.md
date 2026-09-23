---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 27774
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_ERSEP_CONEXIONES"
---

# 🔧 XXCO_ERSEP_CONEXIONES

**Filas estimadas:** 27,774

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TRT_NUMERO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `MODIF_RES` | VARCHAR2 | YES |  |  |
| `ORD_FECHA_FIN_MAX` | DATE | YES |  |  |
| `ORD_FECHA_GENERACION_MIN` | DATE | YES |  |  |
| `POT_VALOR_MAX` | NUMBER | YES |  |  |
| `ORD_DATOS_ADICIONALES` | CHAR | YES |  |  |
| `CANTIDAD_ORD` | NUMBER | YES |  |  |
| `FECHA_EJECUCION` | DATE | YES |  |  |
