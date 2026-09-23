---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 1039
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "SECTORES_ORDENATIVOS"
---

# 📋 SECTORES_ORDENATIVOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 1,039

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SEC_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `SOR_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `SOR_CON_PARTE` | VARCHAR2 | YES |  |
| `SOR_HABILITADO_AUTO_CIERRE` | VARCHAR2 | YES |  |
| `SOR_PROCESO_COORDENADAS` | VARCHAR2 | YES |  |
