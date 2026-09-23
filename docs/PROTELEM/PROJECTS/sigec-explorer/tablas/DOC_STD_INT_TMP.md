---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: documentos
num_rows: 14
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/documentos
  - documentada/negocio
aliases:
  - "DOC_STD_INT_TMP"
---

# ⏱️ DOC_STD_INT_TMP

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 14

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_SALDO` | NUMBER | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `NUMERO_ID` | NUMBER | YES |  |  |
