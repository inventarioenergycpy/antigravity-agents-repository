---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: equipos
num_rows: 358
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/equipos
aliases:
  - "XXCO_ESTRUC_PLANOS_GRP_REP"
---

# 🔧 XXCO_ESTRUC_PLANOS_GRP_REP

**Filas estimadas:** 358

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `EPT_TIPO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_ESTRUC_PLANOS_DETALLES]] |
| `EPD_SECUENCIA` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_ESTRUC_PLANOS_DETALLES]] |
| `EPG_SECUENCIA` | NUMBER | NO | 🔑 PK |
| `EPG_COLUMNA` | VARCHAR2 | YES |  |
| `EPG_VARIABLE` | VARCHAR2 | YES |  |
| `EPG_TAMANIO` | NUMBER | YES |  |
| `EPG_PAD` | VARCHAR2 | YES |  |
| `EPG_LR_PAD` | VARCHAR2 | YES |  |
| `EPG_MASCARA` | VARCHAR2 | YES |  |
| `EPG_ACUMULA_TOTALES` | VARCHAR2 | YES |  |
| `EPG_ACUMULA_EN` | VARCHAR2 | YES |  |
| `EPG_COLUMNA_XML` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **EPG_EPD_FK**: `EPT_TIPO`, `EPD_SECUENCIA` → [[XXCO_ESTRUC_PLANOS_DETALLES]] (`EPT_TIPO`, `EPD_SECUENCIA`)
