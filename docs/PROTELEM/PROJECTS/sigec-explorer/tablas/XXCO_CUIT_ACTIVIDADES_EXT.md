---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_CUIT_ACTIVIDADES_EXT"
---

# 🔧 XXCO_CUIT_ACTIVIDADES_EXT

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `TIPO_DOC` | VARCHAR2 | YES |  |  |
| `NRO_DOC` | NUMBER | YES |  |  |
| `CUIT` | NUMBER | YES |  |  |
| `ACT_CODIGO` | NUMBER | YES |  |  |
