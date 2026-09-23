---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 871
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_CNT_GENERADORES"
---

# 🔧 XXCO_CNT_GENERADORES

**Filas estimadas:** 871

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CGE_FUENTE` | VARCHAR2 | YES |  |  |
| `CGE_FECHA_DESDE` | DATE | YES |  |  |
| `CGE_FECHA_HASTA` | DATE | YES |  |  |
| `CGE_CANTIDAD` | NUMBER | YES |  |  |
| `CGE_ESTADO` | VARCHAR2 | YES |  |  |
