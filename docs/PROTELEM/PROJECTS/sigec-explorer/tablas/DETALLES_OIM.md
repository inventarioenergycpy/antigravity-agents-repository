---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1378
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "DETALLES_OIM"
---

# 📋 DETALLES_OIM

**Filas estimadas:** 1,378

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `AGF_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[OIM]] | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `OIM_TIPO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[OIM]] |  |
| `DIL_FECHA_VIGENCIA` | DATE | NO | 🔑 PK |  |
| `DIL_FECHA_FIN` | DATE | NO |  |  |
| `DIL_IMPORTE` | NUMBER | YES |  |  |
| `DIL_PORCENTAJE` | NUMBER | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | YES | 🔗 → [[TIPOS_ITEM]] |  |

## FK declaradas → otras tablas

- **DIL_FK_OIM**: `AGF_CODIGO`, `OIM_TIPO` → [[OIM]] (`AGF_CODIGO`, `OIM_TIPO`)
- **DIL_FK_TIT**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
