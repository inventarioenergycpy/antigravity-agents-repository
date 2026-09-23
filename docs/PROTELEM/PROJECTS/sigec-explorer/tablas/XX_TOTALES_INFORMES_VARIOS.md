---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 2180767
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "XX_TOTALES_INFORMES_VARIOS"
---

# 📋 XX_TOTALES_INFORMES_VARIOS

**Filas estimadas:** 2,180,767

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `INV_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `TIT_CLAVE` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TIPOS_ITEM]] |  |
| `TIV_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `TIV_SIGNO` | VARCHAR2 | NO | 🔑 PK |  |
| `TNV_IMPORTE` | NUMBER | YES |  |  |
| `TNV_CANTIDAD_ITEMS` | NUMBER | YES |  |  |
| `SCF_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `CODE_COMBINATION_ID` | NUMBER | YES |  |  |
| `TIV_MES_EMISION` | NUMBER | NO | 🔑 PK |  |
| `TIV_TIPO` | VARCHAR2 | NO | 🔑 PK |  |
| `ENE_VENDOR_ID` | NUMBER | NO | 🔑 PK |  |
| `AGF_CODIGO` | VARCHAR2 | NO | 🔑 PK | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `VENDOR_SITE_ID` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **INV_TIT_FK**: `TIT_CLAVE` → [[TIPOS_ITEM]] (`TIT_CLAVE`)
