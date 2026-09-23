---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 45
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "XX_VALORES_PARAMETROS_ORD"
---

# 📋 XX_VALORES_PARAMETROS_ORD

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 45

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `VPO_VALOR` | VARCHAR2 | NO |  |
| `TPO_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XX_TIPOS_PARAMETROS_ORD]] |

## FK declaradas → otras tablas

- **VPO_TPO_FK**: `TPO_CODIGO` → [[XX_TIPOS_PARAMETROS_ORD]] (`TPO_CODIGO`)
