---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 217773
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_LOTES_ORD_FILTROS"
---

# 🔧 XXCO_LOTES_ORD_FILTROS

**Filas estimadas:** 217,773

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `LOF_NUMERO` | NUMBER | NO | 🔑 PK |
| `LOR_NUMERO` | NUMBER | YES |  |
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `ORD_NUMERO` | NUMBER | NO | 🔑 PK |
| `LTF_NUMERO` | NUMBER | NO | 🔑 PK |
| `FECHA_PROCESO` | DATE | YES |  |
| `LOF_PROCESAR` | VARCHAR2 | YES |  |
| `LOF_OBSERVACIONES` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `LOR_NUMERO` → [[XXCO_LOTE_ORDENATIVOS_MOV]] _LOR_NUMERO es PK de XXCO_LOTE_ORDENATIVOS_MOV_
