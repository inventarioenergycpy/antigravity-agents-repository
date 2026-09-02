---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 438
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_LOCALIDADES_OFICIALES"
---

# 🔧 XXCO_LOCALIDADES_OFICIALES

**Filas estimadas:** 438

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DPP` | VARCHAR2 | YES |  |  |
| `ID_DEPARTAMENTO` | VARCHAR2 | YES |  |  |
| `DEPARTAMENTO` | VARCHAR2 | YES |  |  |
| `ID_PEDANIA` | VARCHAR2 | YES |  |  |
| `PEDANIA` | VARCHAR2 | YES |  |  |
| `ID_PUEBLO` | VARCHAR2 | YES |  |  |
| `PUEBLO` | VARCHAR2 | YES |  |  |
| `EXPEDIENTE` | VARCHAR2 | YES |  |  |
| `AREA_HA` | NUMBER | YES |  |  |
| `TIPO` | VARCHAR2 | YES |  |  |
| `PUEBLO_ALTERNATIVO` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `AGF_CODIGO_ADICIONAL` | NUMBER | YES |  |  |
| `DPP_ADICIONAL1` | VARCHAR2 | YES |  |  |
| `DPP_ADICIONAL2` | VARCHAR2 | YES |  |  |
| `ZONA` | VARCHAR2 | YES |  |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `CP` | NUMBER | YES |  |  |
