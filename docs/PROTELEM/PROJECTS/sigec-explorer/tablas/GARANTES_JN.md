---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 11016
tags:
  - sigec-explorer
  - tabla
  - journal
  - documentada/negocio
aliases:
  - "GARANTES_JN"
---

# 📝 GARANTES_JN

**Filas estimadas:** 11,016

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO_GARANTIZADO` | NUMBER | YES |  |  |
| `CNT_NUMERO_GARANTIZADO` | NUMBER | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `GAR_NUMERO_REFINAN` | NUMBER | YES |  |  |
| `USR_NUMERO_BORRA` | NUMBER | NO |  |  |
| `JN_DATETIME` | DATE | NO |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `GAR_FECHA_FIN` | DATE | YES |  |  |
| `GAR_FECHA_CARGA` | DATE | YES |  |  |
