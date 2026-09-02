---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 2170330
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_XML_DETALLE"
---

# 🔧 XXCO_XML_DETALLE

**Filas estimadas:** 2,170,330

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `XIN_NOMBRE_ARCHIVO` | VARCHAR2 | NO | 🔗 → [[XXCO_XML_INTERBANKING]] |
| `XDE_FECHA` | DATE | YES |  |
| `XDE_DOC_TIPO` | VARCHAR2 | YES |  |
| `XDE_DOC_NUMERO` | NUMBER | YES |  |
| `XDE_IMPORTE` | NUMBER | YES |  |
| `XDE_FECHA_PAGO` | DATE | YES |  |
| `XDE_PROCESAR` | VARCHAR2 | YES |  |
| `XDE_NRO_INTERNO` | NUMBER | YES |  |
| `XDE_NRO_OPERACION_IB` | NUMBER | YES |  |
| `XDE_ESTADO` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **XDE_XIN_FK**: `XIN_NOMBRE_ARCHIVO` → [[XXCO_XML_INTERBANKING]] (`XIN_NOMBRE_ARCHIVO`)

## FK inferidas (alta confianza)

- `XIN_NOMBRE_ARCHIVO` → [[XXCO_XML_INTERBANKING]] _XIN_NOMBRE_ARCHIVO es PK de XXCO_XML_INTERBANKING_
