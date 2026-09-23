---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: documentos
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_XML_LCT_TMP"
---

# ⏱️ XXCO_XML_LCT_TMP

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `FECHA_LECTURA` | DATE | YES |  |  |
| `VALOR_ACTUAL` | NUMBER | YES |  |  |
| `LECTURA_ANTERIOR` | DATE | YES |  |  |
| `VALOR_LEIDO` | NUMBER | YES |  |  |
| `CONSUMO` | NUMBER | YES |  |  |
| `DIAS` | NUMBER | YES |  |  |
| `MEDIDOR` | NUMBER | YES |  | Número de medidor, pero SOLO en 4 tablas de carga/TMP (ACTA_TMP, XXCO_XML_*). La clave real y extendida de medidor es STE_NUMERO. No existe columna NRO_MEDIDOR. |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `LCT_TIPO_LECTURA` | VARCHAR2 | YES |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `LCT_POR_LECTURA` | NUMBER | YES |  |  |
