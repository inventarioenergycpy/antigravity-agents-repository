---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 10317943
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_PLAN_FINANCIACION"
---

# 🔧 XXCO_PLAN_FINANCIACION

**Filas estimadas:** 10,317,943

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_NUMERO_FINAN` | NUMBER | NO |  |  |
| `USR_CODIGO` | VARCHAR2 | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PFT_CUOTA_NUMERO` | NUMBER | YES |  |  |
| `PFT_DIA` | NUMBER | YES |  |  |
| `PFT_DOW` | VARCHAR2 | YES |  |  |
| `PFT_FECHA_VENC` | DATE | YES |  |  |
| `PFT_CUOTA_BASICA` | NUMBER | YES |  |  |
| `PFT_INTERES` | NUMBER | YES |  |  |
| `PFT_CUOTA_FIJA` | NUMBER | YES |  |  |
| `PFT_IMPUESTO` | NUMBER | YES |  |  |
| `PFT_IMPORTE_PAGARE` | NUMBER | YES |  |  |
| `PFT_SALDO_FINANCIADO` | NUMBER | YES |  |  |
| `PFT_AFORO` | NUMBER | YES |  |  |
| `PFT_TOTAL_FINANCIADO` | NUMBER | YES |  |  |
| `PFT_PERCEPCION` | NUMBER | YES |  |  |
