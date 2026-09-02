---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 904
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_CNT_INYECTORES"
---

# 🔧 XXCO_CNT_INYECTORES

**Filas estimadas:** 904

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CIN_TIPO` | VARCHAR2 | YES |  |  |
| `CIN_MARCA` | VARCHAR2 | YES |  |  |
| `CIN_MODELO` | VARCHAR2 | YES |  |  |
| `CIN_NRO_SERIE` | VARCHAR2 | YES |  |  |
| `CIN_TENSION_CONEX_RED` | NUMBER | YES |  |  |
| `CIN_POTENCIA_NOMINAL_KW` | NUMBER | YES |  |  |
| `CIN_FECHA_DESDE` | DATE | YES |  |  |
| `CIN_FECHA_HASTA` | DATE | YES |  |  |
| `CIN_ESTADO` | VARCHAR2 | YES |  |  |
