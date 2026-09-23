---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 37437
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "BOLETIN_TAR_BAJA"
---

# 📋 BOLETIN_TAR_BAJA

**Filas estimadas:** 37,437

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `BTB_COD_TARJETA` | VARCHAR2 | YES |  |  |
| `BTB_NRO_TARJETA` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `BTB_FECHA_BAJA` | DATE | YES |  |  |
| `BTB_ESTADO` | VARCHAR2 | YES |  |  |
| `BTB_FECHA_PROCESO` | DATE | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
