---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 650
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_TCL_SOCIAL"
---

# 🔧 XXCO_TCL_SOCIAL

**Filas estimadas:** 650

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `APELLIDOS` | VARCHAR2 | YES |  |  |
| `NOMBRES` | VARCHAR2 | YES |  |  |
| `N_DOC` | VARCHAR2 | YES |  |  |
| `LOCALIDAD` | VARCHAR2 | YES |  |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `SUB_ENER` | VARCHAR2 | YES |  |  |
| `RESOL_ENER` | VARCHAR2 | YES |  |  |
| `RESOL_FEC_ENER` | VARCHAR2 | YES |  |  |
| `FEC_RECEP_RESOL` | VARCHAR2 | YES |  |  |
| `SUMINISTRO` | VARCHAR2 | YES |  | Clave de punto de suministro con nombre corto sin prefijo (7 tablas de integración/TMP). |
| `CNT_NUMERO` | VARCHAR2 | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `ESTADO` | VARCHAR2 | YES |  |  |
| `FEC_PROCESO` | DATE | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
