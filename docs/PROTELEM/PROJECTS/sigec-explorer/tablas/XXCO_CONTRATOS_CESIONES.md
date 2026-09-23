---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 77
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_CONTRATOS_CESIONES"
---

# 🔧 XXCO_CONTRATOS_CESIONES

**Filas estimadas:** 77

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CSN_NUMERO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CCS_FECHA_FIN` | DATE | YES |  |  |
| `CCS_FECHA_CARGA` | DATE | YES |  |  |
| `CCS_FECHA_INICIO` | DATE | YES |  |  |
