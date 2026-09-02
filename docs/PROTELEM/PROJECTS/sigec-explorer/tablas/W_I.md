---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 3
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "W_I"
---

# 📋 W_I

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 3

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | YES |  |
| `DOC_NUMERO` | NUMBER | YES |  |
| `ITM_VENC_NRO` | VARCHAR2 | YES |  |
| `ITM_CANTIDAD` | NUMBER | YES |  |
| `ITM_CANTIDAD_N` | NUMBER | YES |  |
| `NRO_SESSION` | NUMBER | YES |  |
| `USR_UNIX` | VARCHAR2 | YES |  |
| `NRO_ORACLE` | NUMBER | YES |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |
| `SERVIDOR` | VARCHAR2 | YES |  |
| `TERMINAL` | VARCHAR2 | YES |  |
| `PROGRAMA` | VARCHAR2 | YES |  |
| `OPERACION` | VARCHAR2 | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |
| `ITM_IMPORTE` | NUMBER | YES |  |
| `ITM_IMPORTE_N` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
