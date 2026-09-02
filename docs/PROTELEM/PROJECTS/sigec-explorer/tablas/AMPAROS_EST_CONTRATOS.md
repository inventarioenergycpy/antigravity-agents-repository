---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: contratos
num_rows: 750
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/contratos
  - documentada/negocio
aliases:
  - "AMPAROS_EST_CONTRATOS"
---

# 📋 AMPAROS_EST_CONTRATOS

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 750

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DIS` | NUMBER | NO |  |  |
| `SERV` | NUMBER | YES |  |  |
| `CNT` | NUMBER | YES |  |  |
| `NOMBRE` | VARCHAR2 | NO |  |  |
| `TAR_ULT` | VARCHAR2 | NO |  |  |
| `CLA_ULT` | VARCHAR2 | NO |  |  |
| `CNT_FECHA_INICIO` | DATE | NO |  |  |
| `CNT_ESTADO` | VARCHAR2 | NO |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
