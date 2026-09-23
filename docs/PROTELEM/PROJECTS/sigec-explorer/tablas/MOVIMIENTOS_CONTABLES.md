---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 4047437800
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "MOVIMIENTOS_CONTABLES"
---

# 📋 MOVIMIENTOS_CONTABLES

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 4,047,437,800

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `MOC_NUMERO` | NUMBER | NO |  |  |
| `ASI_NUMERO` | NUMBER | NO |  |  |
| `CTA_CODIGO` | VARCHAR2 | YES |  |  |
| `MOC_IMPORTE` | NUMBER | NO |  |  |
| `MOC_CONSUMO` | NUMBER | YES |  |  |
| `MOC_PERIODO` | NUMBER | YES |  |  |
| `MOC_ANIO` | NUMBER | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `BOL_NUMERO` | NUMBER | YES |  |  |
| `URC_CODIGO_DEPOSITO` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | YES |  |  |
| `MOC_FECHA` | DATE | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `MOC_INFORMADO` | VARCHAR2 | YES |  |  |
| `MOC_PROCESADO` | DATE | YES |  |  |
| `MOC_FEC_INFORMADO` | DATE | YES |  |  |
| `CODE_COMBINATION_ID` | NUMBER | YES |  |  |
