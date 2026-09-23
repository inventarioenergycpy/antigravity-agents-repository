---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 112
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "GRUPOS_ITEM_HABILITADOS"
---

# 📋 GRUPOS_ITEM_HABILITADOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 112

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `GIT_GRUPO` | VARCHAR2 | NO | 🔑 PK |
| `GIH_INGRESABLE` | VARCHAR2 | YES |  |
| `GDO_CODIGO` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `GDO_CODIGO` → [[GRUPOS_DOCUMENTO]] _GDO_CODIGO es PK de GRUPOS_DOCUMENTO_
