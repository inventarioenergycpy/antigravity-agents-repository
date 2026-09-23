---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 286
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "TOTAL_FACTURADO_ANUAL_DEUDA"
---

# 📋 TOTAL_FACTURADO_ANUAL_DEUDA

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 286

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_ANIO` | NUMBER | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `CANT_DOC_FACTURADO` | NUMBER | YES |  |  |
| `SITUACION` | VARCHAR2 | YES |  |  |
| `DOC_SALDO` | NUMBER | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `CANT_DOC_DEUDA` | NUMBER | YES |  |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `FECHA_DEUDA` | DATE | YES |  |  |
