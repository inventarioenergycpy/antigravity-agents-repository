---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 21756
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_DOC_CONTR_ANTICIPO_VM"
---

# 🔧 XXCO_DOC_CONTR_ANTICIPO_VM

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 21,756

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_GRUPO` | VARCHAR2 | NO |  | Circuito al que pertenece el documento en DOCUMENTOS. 'N' = normal, el de facturación de energía (14,09M de 14,10M docs en 2025). Los demás son circuitos aparte y no deben mezclarse: T (Factura Telec./comp. interno), O, L, C, G, A. Filtrar DOC_GRUPO='N' junto con DOC_TIPO='F'. |
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_FECHA_EMISION` | DATE | NO |  |  |
