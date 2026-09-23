---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 16402
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "MOVIMIENTOS_FORMA_PAGO_ANU"
---

# 📋 MOVIMIENTOS_FORMA_PAGO_ANU

**Filas estimadas:** 16,402

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `MFP_NUMERO` | NUMBER | NO | 🔑 PK |
| `MFP_TRANSACCION` | NUMBER | NO |  |
| `MFP_FECHA` | DATE | NO |  |
| `MFP_FORMA_PAGO` | VARCHAR2 | NO |  |
| `MFP_NUMERO_CHEQUE` | VARCHAR2 | YES |  |
| `MFP_IMPORTE` | NUMBER | NO |  |
| `URC_CODIGO_COBRADORA` | NUMBER | NO |  |
| `URC_CODIGO_BANCO` | NUMBER | YES |  |
| `CPR_NUMERO` | NUMBER | NO |  |
| `MFP_ERROR` | VARCHAR2 | YES |  |
| `MFP_WARN` | VARCHAR2 | YES |  |
| `MFP_NRO_AUTORIZA` | NUMBER | YES |  |
| `URC_CODIGO_TARJETA` | NUMBER | YES |  |
| `MFP_SUCURSAL_CHEQUE` | NUMBER | YES |  |
