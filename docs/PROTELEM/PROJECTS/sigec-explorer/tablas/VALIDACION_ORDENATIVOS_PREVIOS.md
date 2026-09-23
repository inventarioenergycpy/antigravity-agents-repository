---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 42
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "VALIDACION_ORDENATIVOS_PREVIOS"
---

# 📋 VALIDACION_ORDENATIVOS_PREVIOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 42

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TOR_CODIGO_VALIDACION` | VARCHAR2 | NO | 🔑 PK |
| `VOO_EVENTO` | VARCHAR2 | NO |  |
| `AOO_MISMO_TRT` | VARCHAR2 | YES |  |
| `AOO_CON_RESULTADO` | VARCHAR2 | YES |  |
| `AOO_SOLO_SITUACION` | VARCHAR2 | YES |  |
