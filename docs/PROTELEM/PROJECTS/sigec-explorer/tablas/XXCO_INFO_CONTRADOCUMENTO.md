---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 207730
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_INFO_CONTRADOCUMENTO"
---

# 🔧 XXCO_INFO_CONTRADOCUMENTO

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 207,730

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO_CANCELA` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO_CANCELA` | NUMBER | NO |  |  |
| `DOC_TIPO_CANCELADO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO_CANCELADO` | NUMBER | NO |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `LCT_FECHA_LECTURA` | DATE | YES |  | Fecha en que se tomó la lectura. |
| `LCT_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `LCT_CONSUMO` | NUMBER | YES |  | Consumo calculado del período (diferencia entre lecturas). |
| `LCT_CONSUMO_INFORMADO` | NUMBER | YES |  |  |
| `IFC_FECHA` | DATE | YES |  |  |
