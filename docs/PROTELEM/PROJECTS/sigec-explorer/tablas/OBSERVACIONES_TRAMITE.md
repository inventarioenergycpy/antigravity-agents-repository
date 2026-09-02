---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 65290980
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "OBSERVACIONES_TRAMITE"
---

# 📋 OBSERVACIONES_TRAMITE

**Filas estimadas:** 65,290,980

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TRT_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `OTR_FECHA` | DATE | NO | 🔑 PK |  |
| `OTR_DETALLE` | VARCHAR2 | NO |  |  |
| `OTR_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `USR_NUMERO` | NUMBER | YES |  |  |
