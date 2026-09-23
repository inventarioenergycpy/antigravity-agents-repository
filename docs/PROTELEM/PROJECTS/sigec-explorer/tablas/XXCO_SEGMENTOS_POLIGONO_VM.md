---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 60857
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_SEGMENTOS_POLIGONO_VM"
---

# 🔧 XXCO_SEGMENTOS_POLIGONO_VM

**Filas estimadas:** 60,857

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `LONG_INICIO` | NUMBER | YES |  |
| `LAT_INICIO` | NUMBER | YES |  |
| `LONG_FIN` | NUMBER | YES |  |
| `LAT_FIN` | NUMBER | YES |  |
| `POL_CODIGO` | VARCHAR2 | YES |  |
| `POL_TIPO` | VARCHAR2 | YES |  |
| `PTO_INICIO` | NUMBER | YES |  |
| `PTO_FIN` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `POL_CODIGO` → [[XXAG_POLIGONOS]] _POL_CODIGO es PK de XXAG_POLIGONOS_
- `POL_TIPO` → [[XXAG_POLIGONOS]] _POL_TIPO es PK de XXAG_POLIGONOS_
