---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: equipos
num_rows: 5931860
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/equipos
  - documentada/negocio
aliases:
  - "EQUIPOS_JN"
---

# 📝 EQUIPOS_JN

**Prefijo `EQP_`:** Equipos instalados en puntos de medición (EQUIPOS)

**Filas estimadas:** 5,931,860

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `JN_OPERATION` | VARCHAR2 | NO |  |  |
| `JN_ORACLE_USER` | VARCHAR2 | NO |  |  |
| `JN_DATETIME` | DATE | NO |  |  |
| `JN_NOTES` | VARCHAR2 | YES |  |  |
| `JN_APPLN` | VARCHAR2 | YES |  |  |
| `JN_SESSION` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO |  |  |
| `EQP_ORDEN` | NUMBER | NO |  |  |
| `STE_TIPO` | VARCHAR2 | YES |  | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `EQP_FACTOR_INTENSIDAD` | NUMBER | YES |  |  |
| `EQP_FACTOR_TENSION` | NUMBER | YES |  |  |
| `EQP_FECHA_INSTAL` | DATE | YES |  |  |
| `EQP_PRECINTO` | VARCHAR2 | YES |  |  |
| `EQP_FECHA_RETIRO` | DATE | YES |  |  |
| `EQP_ESTADO` | VARCHAR2 | YES |  |  |
| `OBSERVACION` | VARCHAR2 | YES |  |  |
