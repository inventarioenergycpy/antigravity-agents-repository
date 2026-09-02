---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 72093
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_DEVOLCION_50_BSP"
---

# 🔧 XXCO_DEVOLCION_50_BSP

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 72,093

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_FECHA_INICIO` | DATE | YES |  |  |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
| `DOC_NUMERO_2` | NUMBER | YES |  |  |
| `IMP_TARIFA_2` | NUMBER | YES |  |  |
| `TCL_CODIGO_2` | NUMBER | YES |  |  |
| `CLA_CODIGO_2` | NUMBER | YES |  |  |
| `CPR_NUMERO_2` | NUMBER | YES |  |  |
| `DOC_NUMERO_3` | NUMBER | YES |  |  |
| `IMP_TARIFA_3` | NUMBER | YES |  |  |
| `TCL_CODIGO_3` | NUMBER | YES |  |  |
| `CLA_CODIGO_3` | NUMBER | YES |  |  |
| `CPR_NUMERO_3` | NUMBER | YES |  |  |
| `DOC_NUMERO_4` | NUMBER | YES |  |  |
| `IMP_TARIFA_4` | NUMBER | YES |  |  |
| `TCL_CODIGO_4` | NUMBER | YES |  |  |
| `CLA_CODIGO_4` | NUMBER | YES |  |  |
| `CPR_NUMERO_4` | NUMBER | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `GRF_PAR_IMPAR` | VARCHAR2 | YES |  |  |
| `IAF_NUMERO` | NUMBER | YES |  |  |
| `IAF_IMPORTE` | NUMBER | YES |  |  |
