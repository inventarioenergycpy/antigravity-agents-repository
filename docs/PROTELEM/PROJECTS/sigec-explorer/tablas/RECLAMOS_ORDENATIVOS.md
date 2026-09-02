---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 114
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "RECLAMOS_ORDENATIVOS"
---

# 📋 RECLAMOS_ORDENATIVOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 114

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TRO_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TIPOS_RECLAMO]] |
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TRO_DIAS` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **RORD_FK_TRO**: `TRO_CODIGO` → [[TIPOS_RECLAMO]] (`TRO_CODIGO`)
