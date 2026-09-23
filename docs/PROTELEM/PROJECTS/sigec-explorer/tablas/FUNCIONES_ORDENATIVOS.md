---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "FUNCIONES_ORDENATIVOS"
---

# 📋 FUNCIONES_ORDENATIVOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `FUN_SHORT_NAME` | VARCHAR2 | NO |  |  |
| `TOR_CODIGO` | VARCHAR2 | NO |  |  |
| `SEC_CODIGO_ORIGEN` | VARCHAR2 | NO |  |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | NO |  | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
| `FOR_PREGUNTA` | VARCHAR2 | YES |  |  |
