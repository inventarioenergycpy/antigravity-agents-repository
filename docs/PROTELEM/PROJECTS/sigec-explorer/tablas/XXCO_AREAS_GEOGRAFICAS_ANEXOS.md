---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 2198
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_AREAS_GEOGRAFICAS_ANEXOS"
---

# 🔧 XXCO_AREAS_GEOGRAFICAS_ANEXOS

> Tabla para hacer agregar datos comerciales a la tabla xxdm_areas_geograficas y armar XXCO_AREAS_GEOGRAFICAS_VM

**Filas estimadas:** 2,198

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `AGF_CODIGO` | NUMBER | NO | 🔑 PK | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `AGF_SUBSIDIDADO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
