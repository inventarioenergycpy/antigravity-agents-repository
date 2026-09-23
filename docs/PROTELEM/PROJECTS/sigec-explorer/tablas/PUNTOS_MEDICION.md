---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 1496540
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "PUNTOS_MEDICION"
---

# 📋 PUNTOS_MEDICION

> [!info] Significado de negocio
> Puntos de medición de un suministro (SRV_CODIGO, GRM_NUMERO). Destino de FK declarada de EQUIPOS.

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 1,496,540

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `GRM_CALLE` | VARCHAR2 | YES |  |  |
| `GRM_NRO` | VARCHAR2 | YES |  |  |
| `GRM_PISO` | VARCHAR2 | YES |  |  |
| `GRM_DEPTO` | VARCHAR2 | YES |  |  |
| `GRM_DIRECCION` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `GRM_ESTADO` | VARCHAR2 | YES |  |  |

## Tablas que referencian esta tabla

- [[EQUIPOS]] via `GRM_NUMERO`, `SRV_CODIGO`
