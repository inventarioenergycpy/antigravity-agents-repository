---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 8132
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "PLAZOS_COBRANZA"
---

# 📋 PLAZOS_COBRANZA

**Filas estimadas:** 8,132

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PCO_TIPO_PLAZO` | VARCHAR2 | NO | 🔑 PK |
| `CAT_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |
| `PCO_DIAS_VENC_INT` | NUMBER | NO |  |
| `PCO_DIAS_INT_CORTE_ADM` | NUMBER | NO |  |
| `PCO_DIAS_INT_CORTE_OPE` | NUMBER | NO |  |
| `PCO_DIAS_CORTE_RETIRO` | NUMBER | YES |  |
| `PCO_DIAS_PLAZO` | NUMBER | NO |  |
