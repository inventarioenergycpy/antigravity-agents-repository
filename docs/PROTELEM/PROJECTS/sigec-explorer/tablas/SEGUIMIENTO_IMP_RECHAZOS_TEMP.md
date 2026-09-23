---
tipo: tabla
categoria: temp
owner: XXSIGEC
num_rows: 4834
tags:
  - sigec-explorer
  - tabla
  - temp
  - documentada/negocio
aliases:
  - "SEGUIMIENTO_IMP_RECHAZOS_TEMP"
---

# ⏱️ SEGUIMIENTO_IMP_RECHAZOS_TEMP

**Filas estimadas:** 4,834

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRT_CODIGO_RECHAZO_TEMP` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SRT_COD_IMPRESION_TEMP` | VARCHAR2 | YES |  |  |
| `SRT_NRO_IMPRESION_TEMP` | NUMBER | YES |  |  |
| `SRT_FECHA_RECHAZO_TEMP` | DATE | YES |  |  |
| `SRT_FECHA_PROCESO_TEMP` | DATE | YES |  |  |
| `SRT_ESTADO_TEMP` | VARCHAR2 | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
