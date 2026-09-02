---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 129
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "SECTORES_GRUPOS"
---

# 📋 SECTORES_GRUPOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 129

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GCO_GRUPO` | VARCHAR2 | NO | 🔑 PK |
| `SEC_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
