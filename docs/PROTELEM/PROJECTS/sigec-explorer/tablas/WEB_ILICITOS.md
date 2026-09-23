---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 9204
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "WEB_ILICITOS"
---

# 📋 WEB_ILICITOS

**Filas estimadas:** 9,204

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DRE_NOMBRE_DUENIO` | VARCHAR2 | YES |  |  |
| `RCL_CALLE` | VARCHAR2 | YES |  |  |
| `RCL_NRO` | VARCHAR2 | YES |  |  |
| `RCL_DIRECCION` | VARCHAR2 | YES |  |  |
| `AGF_NOMBRE` | VARCHAR2 | NO |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `DRE_CONSUMO_ESTIMADO` | NUMBER | YES |  |  |
| `DRE_FECHA_CONSTATACION` | DATE | YES |  |  |
| `DRE_ACTIVIDAD1` | VARCHAR2 | YES |  |  |
| `DRE_ACTIVIDAD2` | VARCHAR2 | YES |  |  |
| `TRO_CODIGO` | VARCHAR2 | NO |  |  |
| `RCL_NUMERO` | NUMBER | NO |  |  |
| `DRE_NRO_ACTA_INSPECCION` | VARCHAR2 | YES |  |  |
