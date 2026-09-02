---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 228800
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "XX_INFORMES_PROCESOS_DET_BOL"
---

# 📋 XX_INFORMES_PROCESOS_DET_BOL

**Filas estimadas:** 228,800

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `BOL_NUMERO` | NUMBER | NO | 🔑 PK |
| `URC_CODIGO_DEPOSITO` | NUMBER | NO | 🔑 PK |
| `DBO_ORDEN` | NUMBER | NO | 🔑 PK |
| `CPR_NUMERO` | NUMBER | NO |  |
| `INV_NUMERO` | NUMBER | NO |  |
| `TIV_CODIGO` | VARCHAR2 | YES |  |
| `BOL_CLASE` | VARCHAR2 | YES |  |
| `ASI_NUMERO` | NUMBER | YES |  |
| `DBO_IMPORTE` | NUMBER | YES |  |
| `SIGNO` | VARCHAR2 | YES |  |
| `TIT_CLAVE` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `BOL_CLASE` → [[VALIDACION_BOLETAS]] _BOL_CLASE es PK de VALIDACION_BOLETAS_
