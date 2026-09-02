---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 671
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "DETALLES_LISTA_OTROS"
---

# 📋 DETALLES_LISTA_OTROS

**Filas estimadas:** 671

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PTO_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[PRECIOS_TARIFA_OTROS]] |
| `DLO_ORDEN` | NUMBER | NO | 🔑 PK |
| `TIT_CLAVE` | VARCHAR2 | NO |  |
| `DLO_PRECIO_UNIT` | NUMBER | NO |  |
| `TFA_CODIGO` | VARCHAR2 | NO |  |
| `DLO_CONSUMO_DESDE` | NUMBER | YES |  |
| `DLO_CONSUMO_HASTA` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **DLO_FK_TAB**: `PTO_NUMERO` → [[PRECIOS_TARIFA_OTROS]] (`PTO_NUMERO`)
