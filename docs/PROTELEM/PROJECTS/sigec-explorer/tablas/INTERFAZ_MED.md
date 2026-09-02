---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 589890
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "INTERFAZ_MED"
---

# 📋 INTERFAZ_MED

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 589,890

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `IMD_FECHA` | DATE | YES |  |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `ORD_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `STE_NUMERO_INST` | NUMBER | YES |  |  |
| `CDR_ENTEROS_INST` | NUMBER | YES |  |  |
| `LCT_VALOR_LEIDO_INST` | NUMBER | YES |  |  |
| `EQP_PRECINTO` | VARCHAR2 | YES |  |  |
| `STE_NUMERO_RET` | NUMBER | YES |  |  |
| `LCT_VALOR_LEIDO_RET` | NUMBER | YES |  |  |
| `COD_ERROR` | NUMBER | YES |  |  |
| `ORA_ERROR` | NUMBER | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `FECHA_PROC` | DATE | YES |  |  |
| `USR_NUMERO_EJEC_ORD` | NUMBER | YES |  |  |
| `LCT_VALOR_LEIDO_RET_ER` | NUMBER | YES |  |  |
| `SEC_CODIGO` | VARCHAR2 | YES |  |  |
