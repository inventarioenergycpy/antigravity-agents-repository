---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 209223
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "FRAUDES_WEB"
---

# 📋 FRAUDES_WEB

**Filas estimadas:** 209,223

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `FECHA_HOY` | DATE | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `NRO_ACTA` | VARCHAR2 | YES |  |  |
| `RAZON_SOCIAL` | VARCHAR2 | YES |  |  |
| `CALLE` | VARCHAR2 | YES |  |  |
| `NRO` | VARCHAR2 | YES |  |  |
| `PISO` | VARCHAR2 | YES |  |  |
| `DPTO` | VARCHAR2 | YES |  |  |
| `BARRIO` | VARCHAR2 | YES |  |  |
| `LOCALIDAD` | VARCHAR2 | YES |  |  |
| `FECHA_ACTA` | DATE | YES |  |  |
| `ACTIVIDAD_PRINCIPAL` | VARCHAR2 | YES |  |  |
| `ACTIVIDAD_SECUNDARIA` | VARCHAR2 | YES |  |  |
| `ACTIVIDAD_OBSERVACION` | VARCHAR2 | YES |  |  |
| `FECHA_DESDE` | DATE | YES |  |  |
| `FECHA_HASTA` | DATE | YES |  |  |
| `NRO_LOCALIDAD` | NUMBER | YES |  |  |
| `ORIGEN` | VARCHAR2 | YES |  |  |
| `NRO_DOCUMENTO` | NUMBER | YES |  |  |
| `FECHA_CONSOLIDACION` | DATE | YES |  |  |
