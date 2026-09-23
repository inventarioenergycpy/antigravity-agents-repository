---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 86
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_MENSAJES"
---

# 🔧 XXCO_MENSAJES

**Filas estimadas:** 86

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `MSJ_CODIGO` | NUMBER | NO |  |  |
| `MSJ_NOMBRE` | VARCHAR2 | NO |  |  |
| `MSJ_NOMBRE_CODIFICADO` | VARCHAR2 | NO |  |  |
| `GCO_GRUPO` | VARCHAR2 | NO |  |  |
| `MSJ_TIPO_FACTURA` | VARCHAR2 | YES |  |  |
| `MSJ_TEXTO` | VARCHAR2 | NO |  |  |
| `MSJ_ESTADO` | VARCHAR2 | NO |  |  |
| `MSJ_FECHA_DESDE` | DATE | NO |  |  |
| `MSJ_FECHA_HASTA` | DATE | NO |  |  |
| `MSJ_TIPO_TEXTO` | VARCHAR2 | NO |  |  |
| `MSJ_AREA_TEMPLATE` | VARCHAR2 | NO |  |  |
| `MSJ_ORDEN_IMPRESION` | NUMBER | NO |  |  |
| `MSJ_ESTILO_IMPRESION` | VARCHAR2 | YES |  |  |
| `MSJ_TIPO` | VARCHAR2 | YES |  |  |
| `MSJ_DESC_VARIABLES` | VARCHAR2 | YES |  |  |
| `MSJ_RELATO_CONDICION` | VARCHAR2 | YES |  |  |
| `MSJ_TEXTO_V2` | VARCHAR2 | YES |  |  |
| `MSJ_AREA_TEMPLATE_V2` | VARCHAR2 | YES |  |  |
| `DOC_GRUPO` | VARCHAR2 | YES |  | Circuito al que pertenece el documento en DOCUMENTOS. 'N' = normal, el de facturación de energía (14,09M de 14,10M docs en 2025). Los demás son circuitos aparte y no deben mezclarse: T (Factura Telec./comp. interno), O, L, C, G, A. Filtrar DOC_GRUPO='N' junto con DOC_TIPO='F'. |
