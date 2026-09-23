---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 12271
tags:
  - sigec-explorer
  - tabla
  - journal
aliases:
  - "PLAZOS_COBRANZA_JN"
---

# 📝 PLAZOS_COBRANZA_JN

**Filas estimadas:** 12,271

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `PCO_TIPO_PLAZO` | VARCHAR2 | NO |  |
| `SCF_CODIGO` | NUMBER | YES |  |
| `JN_FECHA` | DATE | YES |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |
| `PCO_DIAS_VENC_INT` | NUMBER | YES |  |
| `PCO_DIAS_INT_CORTE_ADM` | NUMBER | YES |  |
| `PCO_DIAS_INT_CORTE_OPE` | NUMBER | YES |  |
| `PCO_DIAS_CORTE_RETIRO` | NUMBER | YES |  |
| `PCO_DIAS_PLAZO` | NUMBER | YES |  |
| `OBSERVACION` | VARCHAR2 | YES |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `PCO_TIPO_PLAZO` → [[PLAZOS_COBRANZA]] _PCO_TIPO_PLAZO es PK de PLAZOS_COBRANZA_
