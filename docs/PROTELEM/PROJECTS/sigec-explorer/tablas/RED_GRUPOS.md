---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 87827
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "RED_GRUPOS"
---

# 📋 RED_GRUPOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 87,827

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `GRF_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `CRF_ANIO` | NUMBER | NO | 🔑 PK |
| `CRF_PERIODO` | NUMBER | NO | 🔑 PK |
| `RTI_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `RMO_ARCHIVO` | VARCHAR2 | YES |  |
| `DOC_NUMERO_DESDE` | NUMBER | YES |  |
| `DOC_NUMERO_HASTA` | NUMBER | YES |  |
| `RGP_FECHA_CARGA` | DATE | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `RMO_ORDEN` | NUMBER | YES |  |
| `RGP_VTO_MINIMO` | DATE | YES |  |

## FK inferidas (alta confianza)

- `RMO_ARCHIVO` → [[RED_MONITOR]] _RMO_ARCHIVO es PK de RED_MONITOR_
