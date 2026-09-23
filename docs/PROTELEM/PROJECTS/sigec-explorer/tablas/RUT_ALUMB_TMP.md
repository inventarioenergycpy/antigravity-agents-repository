---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: servicios
num_rows: 203
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/servicios
  - documentada/negocio
aliases:
  - "RUT_ALUMB_TMP"
---

# ⏱️ RUT_ALUMB_TMP

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 203

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CODIGO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `RTL_CODIGO_OLD` | NUMBER | YES |  |  |
| `ZON_CODIGO` | VARCHAR2 | YES |  |  |
| `RTL_CODIGO_NUEVO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
