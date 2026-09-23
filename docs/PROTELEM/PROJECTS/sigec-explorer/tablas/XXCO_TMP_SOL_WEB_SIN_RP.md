---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: contratos
num_rows: 24
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/contratos
  - documentada/negocio
aliases:
  - "XXCO_TMP_SOL_WEB_SIN_RP"
---

# 🔧 XXCO_TMP_SOL_WEB_SIN_RP

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 24

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SOLIC_CODIGO` | NUMBER | NO |  |  |
| `SOLIC_FECHA_ALTA` | DATE | YES |  |  |
| `SOLIC_FECHA_RESOLUCION` | DATE | YES |  |  |
| `SOLIC_MENSAJE_AL_USUARIO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO_OUT` | NUMBER | YES |  |  |
| `CNT_NUMERO_OUT` | NUMBER | YES |  |  |
| `CNT_ESTADO` | VARCHAR2 | NO |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
