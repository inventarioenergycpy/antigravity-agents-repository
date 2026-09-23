---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 28
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_TIPOS_ORDENATIVO_COLECTOR"
---

# 🔧 XXCO_TIPOS_ORDENATIVO_COLECTOR

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 28

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `TOR_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `TOR_CODIGO_GENERAR` | VARCHAR2 | YES |  |  |
| `TOR_SCRIPCION_REQUERIDA` | VARCHAR2 | YES |  |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | YES |  | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
| `ORD_PRIORIDAD` | NUMBER | YES |  |  |
| `TOR_TIPO_MODULO_COLECTORA` | VARCHAR2 | YES |  |  |
| `TOR_ACCION` | VARCHAR2 | YES |  |  |
| `TOR_COLUMNA_ACCION` | VARCHAR2 | YES |  |  |
| `TOR_FOTO_REQUERIDA` | VARCHAR2 | YES |  |  |
| `TOR_VIGENTE` | VARCHAR2 | YES |  |  |
