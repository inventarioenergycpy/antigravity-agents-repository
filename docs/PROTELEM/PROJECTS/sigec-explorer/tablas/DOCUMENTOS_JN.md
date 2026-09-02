---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: documentos
num_rows: 1085187
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/documentos
  - documentada/negocio
aliases:
  - "DOCUMENTOS_JN"
---

# 📝 DOCUMENTOS_JN

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 1,085,187

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `JN_USUARIO` | VARCHAR2 | YES |  |  |
| `JN_TIPO_OPERACION` | VARCHAR2 | YES |  |  |
| `JN_OBSERVACION` | VARCHAR2 | YES |  |  |
| `DOC_SITUACION` | VARCHAR2 | YES |  | Situacion del documento de deuda en DETALLE_SALDO. El valor 'G' = en Gestion Judicial y tiene correlacion 1:1 con FECHA_PASE_GJ (los 158.883 documentos con pase a GJ tienen DOC_SITUACION='G'): es el indicador equivalente y mas simple de usar. NO existe estado de retorno: 157.751 siguen con saldo pendiente, 1.132 sin SALDO_ACTUAL y CERO saldados. |
| `CTA_CODIGO` | VARCHAR2 | YES |  |  |
| `CODE_COMBINATION_ID` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_2` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_3` | NUMBER | YES |  |  |
| `DOC_FECHA_VENC` | DATE | YES |  |  |
| `DOC_FECHA_VENC_2` | DATE | YES |  |  |
| `DOC_FECHA_VENC_3` | DATE | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
