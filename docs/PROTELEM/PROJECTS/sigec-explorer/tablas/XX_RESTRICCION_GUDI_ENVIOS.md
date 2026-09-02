---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 21
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_RESTRICCION_GUDI_ENVIOS"
---

# 📋 XX_RESTRICCION_GUDI_ENVIOS

**Filas estimadas:** 21

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RG_NRO` | NUMBER | NO | 🔗 → [[XX_RESTRICCION_GUDI]] |
| `CNT_GUDI` | VARCHAR2 | NO |  |
| `GE_DEM_MAX` | NUMBER | YES |  |
| `GE_PRO_ESC` | VARCHAR2 | YES |  |
| `GE_ESTADO` | VARCHAR2 | YES |  |
| `GE_REPORTE` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **GE_FK**: `RG_NRO` → [[XX_RESTRICCION_GUDI]] (`RG_NRO`)

## FK inferidas (alta confianza)

- `CNT_GUDI` → [[XX_GUDI_MAIL]] _CNT_GUDI es PK de XX_GUDI_MAIL_
- `RG_NRO` → [[XX_RESTRICCION_GUDI]] _RG_NRO es PK de XX_RESTRICCION_GUDI_
