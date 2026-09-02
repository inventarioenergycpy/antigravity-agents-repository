---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 118
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_CONCURSO_DEUDA"
---

# 🔧 XXCO_CONCURSO_DEUDA

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 118

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `FECHA_CONCURSO` | DATE | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
