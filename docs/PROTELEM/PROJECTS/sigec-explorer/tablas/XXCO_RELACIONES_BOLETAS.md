---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 74947
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
aliases:
  - "XXCO_RELACIONES_BOLETAS"
---

# 🔧 XXCO_RELACIONES_BOLETAS

> Detalle de las relaciones entre boletas de cobros y depositos

**Filas estimadas:** 74,947

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RBO_NUMERO` | NUMBER | NO | 🔑 PK |
| `BOL_NUMERO_ORIG` | NUMBER | NO |  |
| `BOL_CLASE_ORIG` | VARCHAR2 | NO |  |
| `URC_CODIGO_DEPOSITO_ORIG` | NUMBER | NO |  |
| `BOL_NUMERO_DEST` | NUMBER | NO |  |
| `BOL_CLASE_DEST` | VARCHAR2 | NO |  |
| `URC_CODIGO_DEPOSITO_DEST` | NUMBER | NO |  |
| `RBO_FECHA` | DATE | NO |  |
| `RBO_IMPORTE` | NUMBER | NO |  |
| `RBO_ESTADO` | VARCHAR2 | NO |  |
| `USR_NUMERO` | NUMBER | NO |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `RBO_FECHA_CARGA` | DATE | YES |  |
| `RBO_OBSERVACIONES` | VARCHAR2 | YES |  |
