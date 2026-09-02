---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 121
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "TMP_RCL_AUD"
---

# 📋 TMP_RCL_AUD

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 121

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LIQ_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `AUD_FECHA` | DATE | YES |  |  |
| `V_USER_NAME` | VARCHAR2 | YES |  |  |
| `V_RESPONSABILITY_NAME` | VARCHAR2 | YES |  |  |
| `V_FORM_NAME` | VARCHAR2 | YES |  |  |
| `V_APPLICATION_NAME` | VARCHAR2 | YES |  |  |
| `NEW_LIQ_NUMERO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `LIQ_NUMERO` → [[LIQUIDACIONES_ILICITOS]] _LIQ_NUMERO es PK de LIQUIDACIONES_ILICITOS_
