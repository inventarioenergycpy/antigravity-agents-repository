---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 28313
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "DEBITO_AUTOMATICO_NOVE_ERROR"
---

# 📋 DEBITO_AUTOMATICO_NOVE_ERROR

**Filas estimadas:** 28,313

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DNE_TIPO_REG` | VARCHAR2 | NO |  |  |
| `DNE_COD_TARJETA` | VARCHAR2 | NO |  |  |
| `DNE_NRO_TARJETA` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DNE_COD_MOV` | VARCHAR2 | YES |  |  |
| `DNE_TOT_RECHA` | NUMBER | YES |  |  |
| `DNE_FECH_TARJETA` | NUMBER | YES |  |  |
| `DNE_FECHA` | DATE | YES |  |  |
| `DNE_COD_ERROR` | VARCHAR2 | YES |  |  |
| `DNE_FECHA_ENVIADO` | DATE | YES |  |  |
