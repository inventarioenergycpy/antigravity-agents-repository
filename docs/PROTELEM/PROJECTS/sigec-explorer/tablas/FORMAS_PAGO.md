---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 5977073
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "FORMAS_PAGO"
---

# 📋 FORMAS_PAGO

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 5,977,073

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `FPG_TRANSACCION` | NUMBER | NO |  |
| `FPG_NUMERO` | NUMBER | NO |  |
| `URC_CODIGO` | NUMBER | NO | 🔗 → [[UNIDADES_RECAUDADORAS]] |
| `FPG_TIPO` | VARCHAR2 | NO |  |
| `FPG_CHEQUE` | NUMBER | YES |  |
| `FPG_DIAS_ACREDITACION` | NUMBER | YES |  |
| `FPG_FECHA` | DATE | YES |  |
| `FPG_IMPORTE` | NUMBER | NO |  |
| `FPG_ESTADO` | VARCHAR2 | YES |  |
| `URC_CODIGO_DEPOSITO` | NUMBER | YES |  |
| `FPG_NRO_AUTORIZA` | NUMBER | YES |  |
| `URC_CODIGO_TARJETA` | NUMBER | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `FPG_SUCURSAL_CHEQUE` | NUMBER | YES |  |
| `BOL_NUMERO` | NUMBER | YES |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |
| `DOC_NUMERO` | NUMBER | YES |  |
| `PAGO_DOBLE` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **FPG_FK_URC**: `URC_CODIGO` → [[UNIDADES_RECAUDADORAS]] (`URC_CODIGO`)
