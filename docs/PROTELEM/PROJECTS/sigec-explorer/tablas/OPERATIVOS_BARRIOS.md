---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 3393
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "OPERATIVOS_BARRIOS"
---

# 📋 OPERATIVOS_BARRIOS

**Filas estimadas:** 3,393

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `OPE_NUMERO` | NUMBER | YES | 🔗 → [[OPERATIVOS]] |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `OAC_OBSERVACIONES` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **OBA_OPE_FK**: `OPE_NUMERO` → [[OPERATIVOS]] (`OPE_NUMERO`)

## FK inferidas (alta confianza)

- `OPE_NUMERO` → [[OPERATIVOS]] _OPE_NUMERO es PK de OPERATIVOS_
