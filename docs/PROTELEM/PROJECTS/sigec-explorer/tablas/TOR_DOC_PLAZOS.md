---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 19
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "TOR_DOC_PLAZOS"
---

# 📋 TOR_DOC_PLAZOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 19

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TDO_NUMERO` | NUMBER | NO |  |
| `TOR_CODIGO` | VARCHAR2 | NO | 🔗 → [[TIPOS_ORDENATIVO]] |
| `DOC_TIPO` | VARCHAR2 | YES |  |
| `TPL_PLAZO` | VARCHAR2 | YES | 🔗 → [[TIPOS_PLAZOS]] |

## FK declaradas → otras tablas

- **TDO_TOR_FK**: `TOR_CODIGO` → [[TIPOS_ORDENATIVO]] (`TOR_CODIGO`)
- **TDO_TPL_FK**: `TPL_PLAZO` → [[TIPOS_PLAZOS]] (`TPL_CODIGO`)
