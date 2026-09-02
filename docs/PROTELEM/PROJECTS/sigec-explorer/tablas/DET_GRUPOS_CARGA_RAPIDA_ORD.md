---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 295
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "DET_GRUPOS_CARGA_RAPIDA_ORD"
---

# 📋 DET_GRUPOS_CARGA_RAPIDA_ORD

**Filas estimadas:** 295

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `DCR_ORDEN` | NUMBER | NO | 🔑 PK |
| `GCR_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[GRUPOS_CARGA_RAPIDA_ORD]] |
| `DCR_PROMPT` | VARCHAR2 | NO |  |
| `DCR_COLUMNA` | VARCHAR2 | NO |  |
| `DCR_TIPO_DATO` | VARCHAR2 | NO |  |
| `DCR_LOV_ASOCIADA` | VARCHAR2 | YES |  |
| `DCR_VALOR_DEFAULT` | VARCHAR2 | YES |  |
| `DCR_REQUERIDO` | VARCHAR2 | NO |  |
| `DCR_ACTUALIZABLE` | VARCHAR2 | NO |  |
| `DCR_MOSTRAR_LCT` | VARCHAR2 | YES |  |
| `DCR_PEDIR_DECIMALES` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **DCR_GCR_FK**: `GCR_CODIGO` → [[GRUPOS_CARGA_RAPIDA_ORD]] (`GCR_CODIGO`)
