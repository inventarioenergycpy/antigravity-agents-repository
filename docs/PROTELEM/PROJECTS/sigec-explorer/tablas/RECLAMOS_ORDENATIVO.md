---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 242
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "RECLAMOS_ORDENATIVO"
---

# 📋 RECLAMOS_ORDENATIVO

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 242

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TRO_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[TIPOS_RECLAMO]] |  |
| `SEC_CODIGO_ORIGEN` | VARCHAR2 | NO | 🔑 PK |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | NO | 🔑 PK | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `TRO_DIAS` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **ROR_FK_TRO**: `TRO_CODIGO` → [[TIPOS_RECLAMO]] (`TRO_CODIGO`)
