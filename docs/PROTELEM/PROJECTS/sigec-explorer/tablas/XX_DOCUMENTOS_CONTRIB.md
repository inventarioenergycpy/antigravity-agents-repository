---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XX_DOCUMENTOS_CONTRIB"
---

# 📋 XX_DOCUMENTOS_CONTRIB

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DCI_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[XX_CONT_PROYECTOS_ITEM]] |  |
| `DOC_TIPO` | VARCHAR2 | NO | 🔑 PK |  |
| `DOC_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `DOC_IMPORTE_BASICO` | NUMBER | NO |  | NO USAR como neto de la factura: coincide con DOC_IMPORTE_GRAVADO en solo el 70,6% y es MENOR en el 28,2% (muestra 322.120 docs de 2025). Poblada al 100% pero con semántica distinta al neto gravado. Para el neto usar DOC_IMPORTE_GRAVADO. |
| `DCT_SIGNO` | NUMBER | NO |  |  |

## FK declaradas → otras tablas

- **DCT_CPI_FK**: `DCI_NUMERO` → [[XX_CONT_PROYECTOS_ITEM]] (`DCI_NUMERO`)
