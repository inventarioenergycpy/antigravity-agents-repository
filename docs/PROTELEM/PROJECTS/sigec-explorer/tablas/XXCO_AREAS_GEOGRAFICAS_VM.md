---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 2920
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_AREAS_GEOGRAFICAS_VM"
---

# 🔧 XXCO_AREAS_GEOGRAFICAS_VM

**Filas estimadas:** 2,920

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `AGF_CODIGO` | NUMBER | NO |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `AGF_NOMBRE` | VARCHAR2 | NO |  |  |
| `AGF_TIPO` | VARCHAR2 | NO |  |  |
| `AGF_TIPO_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `AGF_CODIGO_PADRE` | NUMBER | YES |  |  |
| `AGF_C_POSTAL` | NUMBER | YES |  |  |
| `AGF_SUBTIPO` | VARCHAR2 | YES |  |  |
| `AGF_SUBTIPO_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `AGF_LATITUD` | VARCHAR2 | YES |  |  |
| `AGF_LONGITUD` | VARCHAR2 | YES |  |  |
| `AGF_LATITUD_DEC` | VARCHAR2 | YES |  |  |
| `AGF_LONGITUD_DEC` | VARCHAR2 | YES |  |  |
| `AGF_CATASTRO` | NUMBER | YES |  |  |
| `AGF_SUBSIDIDADO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
