---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 481
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "ORDENATIVOS_AUTORIZADOS"
---

# 📋 ORDENATIVOS_AUTORIZADOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 481

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SEC_CODIGO_ORIGEN` | VARCHAR2 | NO | 🔑 PK |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | NO | 🔑 PK | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TIPOS_ORDENATIVO]] |  |

## FK declaradas → otras tablas

- **OAU_ASOCIADO_A**: `TOR_CODIGO` → [[TIPOS_ORDENATIVO]] (`TOR_CODIGO`)
