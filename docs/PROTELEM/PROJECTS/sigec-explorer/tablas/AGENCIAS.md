---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 70
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "AGENCIAS"
---

# 📋 AGENCIAS

**Filas estimadas:** 70

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `AGE_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `AGE_DENOMINACION` | VARCHAR2 | YES |  |  |
| `AGE_CALLE` | VARCHAR2 | YES |  |  |
| `AGE_NRO` | VARCHAR2 | YES |  |  |
| `AGE_PISO` | VARCHAR2 | YES |  |  |
| `AGE_DEPTO` | VARCHAR2 | YES |  |  |
| `AGE_LOCAL` | VARCHAR2 | YES |  |  |
| `AGE_TELEFONO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |

## Tablas que referencian esta tabla

- [[INTERFAZ_MED_ORD]] via `AGE_CODIGO`, `SCF_CODIGO`
- [[ORDENATIVOS]] via `AGE_CODIGO_DESTINO`, `AGE_CODIGO_ORIGEN`, `SCF_CODIGO_DESTINO`, `SCF_CODIGO_ORIGEN`
- [[UNIDADES_RECAUDADORAS]] via `AGE_CODIGO`, `SCF_CODIGO`
