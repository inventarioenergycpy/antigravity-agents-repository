---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 11094220
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_DOC_TRT_ORD_DEUDA"
---

# 🔧 XXCO_DOC_TRT_ORD_DEUDA

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 11,094,220

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TRT_NUMERO` | NUMBER | NO |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `DOC_SALDO` | NUMBER | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
