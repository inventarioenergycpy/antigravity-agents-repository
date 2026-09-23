---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: contratos
num_rows: 442
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/contratos
  - documentada/negocio
aliases:
  - "STD_INT_DET_TMP"
---

# ⏱️ STD_INT_DET_TMP

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 442

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SUCURSAL` | NUMBER | YES |  |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |  |
| `SRV` | NUMBER | YES |  |  |
| `CNT` | NUMBER | YES |  |  |
| `CNT_ESTADO` | VARCHAR2 | YES |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `NOMBRE` | VARCHAR2 | YES |  |  |
| `SALDO` | NUMBER | YES |  |  |
| `SALDO_TOTAL` | NUMBER | YES |  |  |
