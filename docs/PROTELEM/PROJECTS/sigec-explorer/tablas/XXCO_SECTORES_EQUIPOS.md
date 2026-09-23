---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 1441
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_SECTORES_EQUIPOS"
---

# 🔧 XXCO_SECTORES_EQUIPOS

**Filas estimadas:** 1,441

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SEC_CODIGO_ORIGEN` | VARCHAR2 | NO | 🔗 → [[SECTORES]] |  |
| `SCF_CODIGO_ORIGEN` | NUMBER | NO | 🔗 → [[SUCURSALES]] |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | NO | 🔗 → [[SECTORES]] | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
| `SCF_CODIGO_DESTINO` | NUMBER | NO | 🔗 → [[SUCURSALES]] |  |
| `OBSERVACION` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **SCF_CODIGO_DESTINO_FK**: `SCF_CODIGO_DESTINO` → [[SUCURSALES]] (`SCF_CODIGO`)
- **SCF_CODIGO_ORIGEN_FK**: `SCF_CODIGO_ORIGEN` → [[SUCURSALES]] (`SCF_CODIGO`)
- **SEC_CODIGO_DESTINO_FK**: `SEC_CODIGO_DESTINO` → [[SECTORES]] (`SEC_CODIGO`)
- **SEC_CODIGO_ORIGEN_FK**: `SEC_CODIGO_ORIGEN` → [[SECTORES]] (`SEC_CODIGO`)
