---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 39098380
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_FOTOS"
---

# 🔧 XXCO_FOTOS

**Filas estimadas:** 39,098,380

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `FOTO_ID` | NUMBER | YES |  |
| `FOTO_NOMBRE` | VARCHAR2 | NO | 🔑 PK |
| `FOTO_EMPRESA` | VARCHAR2 | YES |  |
| `FOTO_FECHA` | DATE | YES |  |
| `FOTO_MEDIDOR` | VARCHAR2 | YES |  |
| `FOTO_PROCESADA` | NUMBER | YES |  |
| `FOTO_FECHA_PROCESO` | DATE | YES |  |
| `LCR_NUMERO` | NUMBER | YES |  |
| `ORC_NUMERO` | NUMBER | YES |  |
| `ORD_NUMERO` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `ORC_NUMERO` → [[XXCO_ORDENATIVOS_COLECTOR]] _ORC_NUMERO es PK de XXCO_ORDENATIVOS_COLECTOR_
