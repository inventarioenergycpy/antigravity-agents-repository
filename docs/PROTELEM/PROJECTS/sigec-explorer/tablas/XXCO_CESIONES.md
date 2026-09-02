---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 15
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_CESIONES"
---

# 🔧 XXCO_CESIONES

**Filas estimadas:** 15

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CSN_NUMERO` | NUMBER | NO |  |  |
| `CSN_FECHA_INICIO` | DATE | NO |  |  |
| `CSN_FECHA_FIN` | DATE | YES |  |  |
| `CSN_FECHA_CARGA` | DATE | YES |  |  |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `CSN_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `URC_CODIGO` | NUMBER | NO |  |  |
