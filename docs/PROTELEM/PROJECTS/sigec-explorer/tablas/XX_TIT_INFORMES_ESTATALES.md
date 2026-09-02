---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 404
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "XX_TIT_INFORMES_ESTATALES"
---

# 📋 XX_TIT_INFORMES_ESTATALES

**Filas estimadas:** 404

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TIT_CLAVE` | VARCHAR2 | NO |  |  |
| `AGF_CODIGO` | NUMBER | YES | 🔗 → [[AREAS_GEOGRAFICAS]] | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `ENE_VENDOR_ID` | NUMBER | NO | 🔗 → [[XX_ENTES_ESTATALES]] |  |
| `TIV_CODIGO` | VARCHAR2 | NO |  |  |
| `TIN_DET_DISTRITO` | VARCHAR2 | YES |  |  |
| `TIN_SCF_EXCLUIDO` | NUMBER | YES |  |  |
| `CODE_COMBINATION_ID` | NUMBER | YES |  |  |
| `VENDOR_SITE_ID` | NUMBER | YES |  |  |
| `PRS_NUMERO_RC` | NUMBER | YES |  |  |
| `TIN_PORCENTAJE_FAC` | NUMBER | YES |  |  |
| `TIT_APLICACION_AUTOMATICA` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **TIE_AGF_FK**: `AGF_CODIGO` → [[AREAS_GEOGRAFICAS]] (`AGF_CODIGO`)
- **TIE_ENE_FK**: `ENE_VENDOR_ID` → [[XX_ENTES_ESTATALES]] (`ENE_VENDOR_ID`)
