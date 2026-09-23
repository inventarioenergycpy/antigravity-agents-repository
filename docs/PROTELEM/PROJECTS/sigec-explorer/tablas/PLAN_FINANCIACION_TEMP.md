---
tipo: tabla
categoria: temp
owner: XXSIGEC
num_rows: 1143337
tags:
  - sigec-explorer
  - tabla
  - temp
  - documentada/negocio
aliases:
  - "PLAN_FINANCIACION_TEMP"
---

# ⏱️ PLAN_FINANCIACION_TEMP

**Filas estimadas:** 1,143,337

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SESSION_ID` | NUMBER | NO |  |  |
| `USR_NUMERO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PFT_NUMERO` | NUMBER | YES |  |  |
| `PFT_DIA` | NUMBER | YES |  |  |
| `PFT_DOW` | VARCHAR2 | YES |  |  |
| `PFT_FECHA_VENC` | DATE | YES |  |  |
| `PFT_IMPORTE` | NUMBER | YES |  |  |
| `PFT_INTERES` | NUMBER | YES |  |  |
| `PFT_IMPUESTO` | NUMBER | YES |  |  |
| `PFT_IMPORTE_PAGARE` | NUMBER | YES |  |  |
| `PFT_TOTAL_FINANCIADO` | NUMBER | YES |  |  |
| `PFT_AFORO` | NUMBER | YES |  |  |
