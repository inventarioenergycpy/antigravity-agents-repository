---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: documentos
num_rows: 124437
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_REQ_RETENCION_DOC_TMP"
---

# ⏱️ XXCO_REQ_RETENCION_DOC_TMP

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 124,437

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `CRF_ANIO` | NUMBER | YES |  |  |
| `CRF_PERIODO` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | NO | 🔑 PK |  |
| `DOC_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `RET_FECHA` | DATE | YES |  |  |
| `LIB_FECHA` | DATE | YES |  |  |
