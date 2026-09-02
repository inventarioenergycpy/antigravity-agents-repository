---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 31319797
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "TRANSICIONES_HISTORICAS"
---

# 📋 TRANSICIONES_HISTORICAS

**Filas estimadas:** 31,319,797

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRC_CODIGO` | VARCHAR2 | NO |  |  |
| `EST_CODIGO_ANTERIOR` | VARCHAR2 | NO |  |  |
| `EVE_CODIGO` | VARCHAR2 | NO |  |  |
| `EST_CODIGO_POSTERIOR` | VARCHAR2 | NO |  |  |
| `THI_FECHA` | DATE | NO |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `USR_NUMERO` | NUMBER | YES |  |  |
