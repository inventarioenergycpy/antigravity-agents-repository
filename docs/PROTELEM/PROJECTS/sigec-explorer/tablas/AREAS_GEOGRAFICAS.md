---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 3318
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "AREAS_GEOGRAFICAS"
---

# 📋 AREAS_GEOGRAFICAS

> [!info] Significado de negocio
> Dimensión geográfica (PK AGF_CODIGO, ~3318 filas). Columnas: AGF_NOMBRE, AGF_TIPO (ZL=zona-localidad, LC=localidad, BA=barrio, NU, DP=departamento…), AGF_CODIGO1 (padre), SCF_CODIGO (sucursal). SERVICIOS.AGF_CODIGO apunta a nivel ZL. Córdoba capital = AGF 1000 (ZL 'CORDOBA'); su Sucursal = SCF_CODIGO 1 (más amplia, incluye Malagueño, Juárez Celman, etc.).

**Filas estimadas:** 3,318

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `AGF_CODIGO` | NUMBER | NO | 🔑 PK | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `AGF_NOMBRE` | VARCHAR2 | NO |  |  |
| `AGF_TIPO` | VARCHAR2 | NO |  |  |
| `AGF_CODIGO1` | NUMBER | YES |  |  |
| `AGF_C_POSTAL` | NUMBER | YES |  |  |
| `AGF_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES | 🔗 → [[SUCURSALES]] |  |

## FK declaradas → otras tablas

- **AGF_FK_SCF**: `SCF_CODIGO` → [[SUCURSALES]] (`SCF_CODIGO`)

## Tablas que referencian esta tabla

- [[PROCURADORES]] via `AGF_CODIGO`
- [[XX_TIT_INFORMES_ESTATALES]] via `AGF_CODIGO`
