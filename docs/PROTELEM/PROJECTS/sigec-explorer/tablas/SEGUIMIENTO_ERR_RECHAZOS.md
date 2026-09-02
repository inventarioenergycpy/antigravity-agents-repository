---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 372
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "SEGUIMIENTO_ERR_RECHAZOS"
---

# 📋 SEGUIMIENTO_ERR_RECHAZOS

**Filas estimadas:** 372

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SER_NOMBRE_ARCHIVO` | VARCHAR2 | NO |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SER_FECHA_RECHAZO` | DATE | NO |  |  |
| `SER_COD_IMPRESION` | VARCHAR2 | NO |  |  |
| `SER_NRO_IMPRESION` | NUMBER | YES |  |  |
| `SER_COD_MOVIM` | VARCHAR2 | YES |  |  |
| `SER_FECHA_PROCESO` | DATE | YES |  |  |
