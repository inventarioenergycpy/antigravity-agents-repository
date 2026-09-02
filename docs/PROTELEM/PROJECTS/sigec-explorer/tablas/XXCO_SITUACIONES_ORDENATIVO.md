---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 21
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_SITUACIONES_ORDENATIVO"
---

# 🔧 XXCO_SITUACIONES_ORDENATIVO

**Filas estimadas:** 21

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ORD_ESTADO` | VARCHAR2 | NO |  |
| `ORD_SITUACION` | VARCHAR2 | NO |  |
| `LOR_NUMERO` | VARCHAR2 | NO |  |
| `SIN_NUMERO` | VARCHAR2 | NO |  |
| `ORD_RESULTADO` | VARCHAR2 | NO |  |
| `SIN_CONFIRMADA` | VARCHAR2 | NO |  |
| `ORD_RESULTADO_EN_PROCESO` | VARCHAR2 | NO |  |
| `SOR_SITUACION_DESC` | VARCHAR2 | NO |  |
| `SOR_COLOR_SITUACION` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `SIN_NUMERO` → [[XXCO_OBSERVACIONES_ORDENATIVO]] _SIN_NUMERO es PK de XXCO_OBSERVACIONES_ORDENATIVO_
- `LOR_NUMERO` → [[XXCO_LOTE_ORDENATIVOS_MOV]] _LOR_NUMERO es PK de XXCO_LOTE_ORDENATIVOS_MOV_
