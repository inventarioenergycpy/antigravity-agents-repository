---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 3925
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "AJUSTE_COOP_PER_10"
---

# 📋 AJUSTE_COOP_PER_10

**Filas estimadas:** 3,925

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TIPO` | VARCHAR2 | YES |  |  |
| `SEGMENTO` | VARCHAR2 | YES |  |  |
| `TIT_CLAVE_OLD` | VARCHAR2 | YES |  |  |
| `TIT_DESCRIPCION_OLD` | VARCHAR2 | YES |  |  |
| `ITA_CANTIDAD_OLD` | NUMBER | YES |  |  |
| `ITA_IMPORTE_OLD` | NUMBER | YES |  |  |
| `TIT_CLAVE_NEW` | VARCHAR2 | YES |  |  |
| `TIT_DESCRIPCION_NEW` | VARCHAR2 | NO |  |  |
| `ITA_CANTIDAD_NEW` | NUMBER | YES |  |  |
| `ITA_IMPORTE_NEW` | NUMBER | YES |  |  |
