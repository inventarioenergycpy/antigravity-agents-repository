---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 13828
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "ERSEP_TARSOCIAL"
---

# 📋 ERSEP_TARSOCIAL

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 13,828

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RAZON_SOCI` | CHAR | YES |  |
| `DOC_TIPO` | CHAR | YES |  |
| `DOC_NRO` | NUMBER | YES |  |
| `CALLE` | CHAR | YES |  |
| `CALLE_NRO` | NUMBER | YES |  |
| `BARRIO` | CHAR | YES |  |
| `LOCALIDAD` | CHAR | YES |  |
| `SUBS` | CHAR | YES |  |
| `RES_NRO` | NUMBER | YES |  |
| `RES_FECHA` | DATE | YES |  |
| `SOL_NRO` | CHAR | YES |  |
| `ING_FECHA` | CHAR | YES |  |
| `EPEC` | CHAR | YES |  |
| `FECHA_CARGA` | DATE | YES |  |
| `FECHA_ACTUALIZA` | DATE | YES |  |

## FK inferidas (alta confianza)

- `DOC_NRO` → [[XXCO_DOC_CORREO_XML]] _DOC_NRO es PK de XXCO_DOC_CORREO_XML_
