---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "EXT_TMP_SRV"
---

# 📋 EXT_TMP_SRV

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `SRV_SUBESTACION_TEC` | VARCHAR2 | YES |  |  |
| `SRV_DISTRIBUIDOR_TEC` | VARCHAR2 | YES |  |  |
| `SRV_TIPO_DISTRIB_TEC` | VARCHAR2 | YES |  |  |
