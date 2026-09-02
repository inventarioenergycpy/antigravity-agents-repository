---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 15
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "MEDIOS_PAGO"
---

# 📋 MEDIOS_PAGO

**Filas estimadas:** 15

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `URC_CODIGO` | NUMBER | NO | 🔑 PK |
| `MPA_TIPO_MEDIO_PAGO` | VARCHAR2 | NO | 🔑 PK |
| `MPA_ESTADO` | VARCHAR2 | YES |  |
| `MPA_OBSERVACIONES` | VARCHAR2 | YES |  |
| `MPA_DEBITO_AUTOMATICO` | VARCHAR2 | YES |  |
| `MPA_REINSERTA_ALTA` | VARCHAR2 | YES |  |
| `MPA_IVA_CF` | VARCHAR2 | YES |  |
| `MPA_TARJETA` | VARCHAR2 | YES |  |
| `MPA_RESTRINGE_CARGA` | VARCHAR2 | YES |  |
| `URC_CODIGO_COBRADORA` | NUMBER | YES |  |
| `MPA_VALIDA_BOL` | VARCHAR2 | YES |  |
| `MPA_TIPO_MEDIO_PAGO_AFIP` | VARCHAR2 | YES |  |
| `MPA_IMPRIME_CODIGO_BARRA` | VARCHAR2 | YES |  |
