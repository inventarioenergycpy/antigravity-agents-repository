---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 415
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "OIM"
---

# 📋 OIM

**Filas estimadas:** 415

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `AGF_CODIGO` | NUMBER | NO | 🔑 PK | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `OIM_TIPO` | VARCHAR2 | NO | 🔑 PK |  |
| `OIM_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `OIM_ESTADO` | VARCHAR2 | YES |  |  |

## Tablas que referencian esta tabla

- [[CONTRATOS]] via `AGF_CODIGO_OIM`, `OIM_TIPO`
- [[DETALLES_OIM]] via `AGF_CODIGO`, `OIM_TIPO`
