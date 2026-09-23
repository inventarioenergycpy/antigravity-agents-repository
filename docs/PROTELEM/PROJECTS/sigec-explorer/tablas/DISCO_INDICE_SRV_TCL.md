---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1409
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "DISCO_INDICE_SRV_TCL"
---

# 📋 DISCO_INDICE_SRV_TCL

**Filas estimadas:** 1,409

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ISU_FECHA_ALTA` | DATE | YES |  |  |
| `ZON_CODIGO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `ISU_GRUPO` | VARCHAR2 | YES |  |  |
| `ISU_CANTIDAD` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
