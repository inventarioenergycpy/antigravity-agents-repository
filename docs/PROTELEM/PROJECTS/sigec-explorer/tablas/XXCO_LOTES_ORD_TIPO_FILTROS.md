---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 37
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_LOTES_ORD_TIPO_FILTROS"
---

# 🔧 XXCO_LOTES_ORD_TIPO_FILTROS

**Filas estimadas:** 37

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `LTF_NUMERO` | NUMBER | YES |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |
| `SEC_CODIGO` | VARCHAR2 | YES |  |
| `LTF_FILTRO` | VARCHAR2 | YES |  |
| `LTF_VIGENCIA_DESDE` | DATE | YES |  |
| `LTF_VIGENCIA_HASTA` | DATE | YES |  |

## FK inferidas (alta confianza)

- `LTF_NUMERO` → [[XXCO_LOTES_ORD_FILTROS]] _LTF_NUMERO es PK de XXCO_LOTES_ORD_FILTROS_
