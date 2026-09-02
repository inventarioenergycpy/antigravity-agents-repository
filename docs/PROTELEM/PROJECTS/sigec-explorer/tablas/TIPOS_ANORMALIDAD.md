---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 2
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "TIPOS_ANORMALIDAD"
---

# 📋 TIPOS_ANORMALIDAD

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 2

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TAN_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `TAN_DESCRIPCION` | CHAR | NO |  |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `SEC_CODIGO_ORIGEN` | VARCHAR2 | YES |  |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | YES |  | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
