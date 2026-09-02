---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 105283
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "SEGUIMIENTO_IMP_RECHAZOS"
---

# 📋 SEGUIMIENTO_IMP_RECHAZOS

**Filas estimadas:** 105,283

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SIR_CODIGO_RECHAZO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SIR_FECHA_RECHAZO` | DATE | NO |  |  |
| `SIR_COD_IMPRESION` | VARCHAR2 | YES |  |  |
| `SIR_NRO_IMPRESION` | NUMBER | YES |  |  |
| `SIR_ESTADO` | VARCHAR2 | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `SIR_FECHA_PROCESO` | DATE | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
