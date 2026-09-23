---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 92
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
aliases:
  - "XXCO_CHEQUES_RECHAZADOS"
---

# 🔧 XXCO_CHEQUES_RECHAZADOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 92

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CPR_NUMERO` | NUMBER | NO | 🔑 PK |
| `CHR_FECHA` | DATE | NO |  |
| `MOV_NUMERO` | NUMBER | NO | 🔑 PK |
| `MFP_NUMERO` | NUMBER | NO | 🔑 PK |
| `CHR_TRANSACCION` | NUMBER | YES |  |
| `DOC_TIPO_CONTRA` | VARCHAR2 | YES |  |
| `DOC_NUMERO_CONTRA` | NUMBER | YES |  |
| `CHR_FECHA_CONTRA` | DATE | YES |  |
| `USR_NUMERO` | NUMBER | YES |  |
| `CHR_ENVIO_MAIL` | DATE | YES |  |
| `CHR_OBSERVACIONES` | VARCHAR2 | YES |  |
