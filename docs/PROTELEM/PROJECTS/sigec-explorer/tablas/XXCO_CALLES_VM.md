---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 11390
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_CALLES_VM"
---

# 🔧 XXCO_CALLES_VM

**Filas estimadas:** 11,390

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CAL_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `CAL_NOMBRE` | VARCHAR2 | NO |  |  |
| `AGF_CODIGO` | NUMBER | NO |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `CAL_NOMBRE_CORTO` | VARCHAR2 | YES |  |  |
