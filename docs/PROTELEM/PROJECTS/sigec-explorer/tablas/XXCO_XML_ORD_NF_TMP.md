---
tipo: tabla
categoria: temp
owner: XXSIGEC
tags:
  - sigec-explorer
  - tabla
  - temp
  - documentada/negocio
aliases:
  - "XXCO_XML_ORD_NF_TMP"
---

# ⏱️ XXCO_XML_ORD_NF_TMP

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ORD_NUMERO` | NUMBER | NO |  |  |
| `DRE_NOMBRE_DUENIO` | VARCHAR2 | YES |  |  |
| `RCL_CALLE` | VARCHAR2 | YES |  |  |
| `RCL_NRO` | VARCHAR2 | YES |  |  |
| `RCL_PISO` | VARCHAR2 | YES |  |  |
| `RCL_DEPTO` | VARCHAR2 | YES |  |  |
| `RCL_DIRECCION` | VARCHAR2 | YES |  |  |
| `AGF_NOMBRE` | VARCHAR2 | YES |  |  |
| `AGF_C_POSTAL` | NUMBER | YES |  |  |
| `ZON_CODIGO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `SCF_TELEFONO` | VARCHAR2 | YES |  |  |
| `SCF_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `DRE_NRO_ACTA_INSPECCION` | VARCHAR2 | NO |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
