---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 70413990
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "MOVIMIENTOS_FORMA_PAGO"
---

# 📋 MOVIMIENTOS_FORMA_PAGO

**Filas estimadas:** 70,413,990

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
| `MFP_ON_LINE` | VARCHAR2 | YES |  |
| `MFP_ESTADO_CHEQUE` | VARCHAR2 | YES |  |
