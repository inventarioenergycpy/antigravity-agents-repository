---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 359
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "MC_TEMPORAL"
---

# 📋 MC_TEMPORAL

**Filas estimadas:** 359

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `NRO_TARJETA` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `ESTADO` | VARCHAR2 | YES |  |  |
| `DESCRIPCION` | VARCHAR2 | YES |  |  |
| `ETAPA` | NUMBER | YES |  |  |
