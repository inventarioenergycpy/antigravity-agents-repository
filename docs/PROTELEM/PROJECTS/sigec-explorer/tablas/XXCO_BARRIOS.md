---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 659
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_BARRIOS"
---

# 🔧 XXCO_BARRIOS

**Filas estimadas:** 659

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `BAR_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `BAR_NOMBRE` | VARCHAR2 | YES |  |  |
| `BAR_TIPO` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `BAR_SUBSIDIADO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
