---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 74237
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "TMP_NAES"
---

# 📋 TMP_NAES

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 74,237

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `CUIT` | NUMBER | YES |  |  |
| `ACT_CODIGO` | NUMBER | YES |  |  |
| `PROCESADO` | VARCHAR2 | YES |  |  |
