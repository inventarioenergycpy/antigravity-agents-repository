---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 2618
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "ACCIONES_ORDENATIVOS"
---

# 📋 ACCIONES_ORDENATIVOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 2,618

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SEC_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[RESULTADOS_ORDENATIVOS]] |
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[RESULTADOS_ORDENATIVOS]] |
| `ROD_RESULTADO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[RESULTADOS_ORDENATIVOS]] |
| `TOR_CODIGO_ACCION` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TIPOS_ORDENATIVO]] |
| `AOO_ACCION` | VARCHAR2 | NO |  |
| `ROD_RESULTADO_ACCION` | VARCHAR2 | YES |  |
| `AOO_SOLO_X_SRV_CODIGO` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **AOO_ROD_FK**: `TOR_CODIGO`, `SEC_CODIGO`, `ROD_RESULTADO` → [[RESULTADOS_ORDENATIVOS]] (`TOR_CODIGO`, `SEC_CODIGO`, `ROD_RESULTADO`)
- **AOO_TOR_FK**: `TOR_CODIGO_ACCION` → [[TIPOS_ORDENATIVO]] (`TOR_CODIGO`)
