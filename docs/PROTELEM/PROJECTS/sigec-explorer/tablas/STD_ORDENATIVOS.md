---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 6675
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "STD_ORDENATIVOS"
---

# 📋 STD_ORDENATIVOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 6,675

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ZON_CODIGO` | VARCHAR2 | YES |  |
| `ORD_FECHA_GENERACION` | DATE | YES |  |
| `TOR_CODIGO` | VARCHAR2 | NO |  |
| `CANTIDAD` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
