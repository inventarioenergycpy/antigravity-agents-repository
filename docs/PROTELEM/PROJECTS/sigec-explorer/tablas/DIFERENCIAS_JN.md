---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: documentos
num_rows: 30353
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/documentos
aliases:
  - "DIFERENCIAS_JN"
---

# 📝 DIFERENCIAS_JN

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 30,353

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `JN_SECUENCIA_DIF` | NUMBER | YES |  |
| `DIF_NUMERO` | NUMBER | NO |  |
| `CPR_NUMERO` | NUMBER | NO |  |
| `URC_CODIGO` | NUMBER | YES |  |
| `DIF_IMPORTE` | NUMBER | YES |  |
| `DIF_ESTADO` | VARCHAR2 | YES |  |
| `DIF_OBSERVACIONES` | VARCHAR2 | YES |  |
| `DOC_NUMERO` | NUMBER | YES |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |
| `ASI_NUMERO` | NUMBER | YES |  |
| `JN_USR_NUMERO` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `TIT_CLAVE` | VARCHAR2 | NO |  |
| `SCF_CODIGO` | NUMBER | NO |  |
| `DIF_FECHA` | DATE | YES |  |
| `URC_CODIGO_MOV` | NUMBER | YES |  |
| `BOL_NUMERO` | NUMBER | YES |  |
| `URC_CODIGO_DEPOSITO` | NUMBER | YES |  |
| `DIF_NUMERO_FINAN` | NUMBER | YES |  |
| `DIF_USR_NUMERO_AUTORIZA` | NUMBER | YES |  |
| `JN_ACCION` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `DIF_NUMERO` → [[DIFERENCIAS]] _DIF_NUMERO es PK de DIFERENCIAS_
