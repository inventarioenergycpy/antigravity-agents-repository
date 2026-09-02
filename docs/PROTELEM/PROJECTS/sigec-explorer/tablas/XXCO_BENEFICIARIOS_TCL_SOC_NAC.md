---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 366623
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_BENEFICIARIOS_TCL_SOC_NAC"
---

# 🔧 XXCO_BENEFICIARIOS_TCL_SOC_NAC

**Filas estimadas:** 366,623

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TSN_FECHA_CARGA` | DATE | YES |  |  |
| `TSN_FECHA_APLICACION_TCL` | DATE | YES |  |  |
| `ID_PERSONA` | NUMBER | YES |  |  |
| `DISTRIBUIDORA` | VARCHAR2 | YES |  |  |
| `TDOC_ORIG` | VARCHAR2 | YES |  |  |
| `NDOC_ORIG` | NUMBER | YES |  |  |
| `DENO_ORIG` | VARCHAR2 | YES |  |  |
| `CUIT_ORIG` | VARCHAR2 | YES |  |  |
| `CONTRATO` | NUMBER | YES |  |  |
| `TIPO_CLIENTE` | VARCHAR2 | YES |  |  |
| `LOCALIDAD` | VARCHAR2 | YES |  |  |
| `BARRIO` | VARCHAR2 | YES |  |  |
| `CALLE` | VARCHAR2 | YES |  |  |
| `NUMERO` | VARCHAR2 | YES |  |  |
| `PISO` | VARCHAR2 | YES |  |  |
| `DEPTO` | VARCHAR2 | YES |  |  |
| `TEMATICA` | VARCHAR2 | YES |  |  |
