---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "EMPRESAS"
---

# 📋 EMPRESAS

**Filas estimadas:** 1

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `EMP_RAZON_SOCIAL` | VARCHAR2 | NO | 🔑 PK |  |
| `EMP_CENTRO_PROCESAMIENTO` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | NO |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `EMP_C_POSTAL` | NUMBER | YES |  |  |
| `EMP_DIRECCION` | VARCHAR2 | YES |  |  |
| `EMP_LOCALIDAD` | VARCHAR2 | YES |  |  |
| `EMP_TELEFONO` | VARCHAR2 | YES |  |  |
| `EMP_PREVISION` | NUMBER | YES |  |  |
| `EMP_ING_BRUTOS` | NUMBER | YES |  |  |
| `EMP_CUIT` | NUMBER | YES |  |  |
| `EMP_NOMBRE_SISTEMA` | VARCHAR2 | YES |  |  |
