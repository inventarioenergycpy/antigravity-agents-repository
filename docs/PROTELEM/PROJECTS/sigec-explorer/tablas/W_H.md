---
tipo: tabla
categoria: hist
owner: XXSIGEC
dominio: servicios
num_rows: 177793
tags:
  - sigec-explorer
  - tabla
  - hist
  - dominio/servicios
  - documentada/negocio
aliases:
  - "W_H"
---

# 📂 W_H

**Filas estimadas:** 177,793

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `COH_ANIO_PERIODO` | NUMBER | YES |  |  |
| `COH_CONSUMO` | NUMBER | YES |  |  |
| `COH_CANTIDAD_DIAS` | NUMBER | YES |  |  |
| `COH_ANIO_PERIODO_N` | NUMBER | YES |  |  |
| `COH_CONSUMO_N` | NUMBER | YES |  |  |
| `COH_CANTIDAD_DIAS_N` | NUMBER | YES |  |  |
| `NRO_SESSION` | NUMBER | YES |  |  |
| `USR_UNIX` | VARCHAR2 | YES |  |  |
| `NRO_ORACLE` | NUMBER | YES |  |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |  |
| `SERVIDOR` | VARCHAR2 | YES |  |  |
| `TERMINAL` | VARCHAR2 | YES |  |  |
| `PROGRAMA` | VARCHAR2 | YES |  |  |
| `OPERACION` | VARCHAR2 | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
