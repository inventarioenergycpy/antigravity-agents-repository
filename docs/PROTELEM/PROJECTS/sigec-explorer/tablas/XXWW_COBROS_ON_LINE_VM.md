---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 65841640
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "XXWW_COBROS_ON_LINE_VM"
---

# 📋 XXWW_COBROS_ON_LINE_VM

> [!info] Significado de negocio
> Log de cobros del canal online/web (~65,8M filas). Su columna CONTRATO trae el número de contrato de 10 dígitos TAL COMO lo ve el cliente (ej. '0315074102'), junto a TIPO_DOC/NUMERO_DOC del comprobante pagado. Es la fuente para verificar el formato del número de contrato de cara al cliente.

**Filas estimadas:** 65,841,640

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ID_PRODUCTO` | VARCHAR2 | YES |  |
| `WEBSERVICE` | VARCHAR2 | YES |  |
| `METODO` | VARCHAR2 | YES |  |
| `FECHA` | DATE | YES |  |
| `CONTRATO` | VARCHAR2 | YES |  |
| `TIPO_DOC` | VARCHAR2 | YES |  |
| `NUMERO_DOC` | NUMBER | YES |  |
| `IMPORTE` | NUMBER | YES |  |
| `PROCESADO` | VARCHAR2 | YES |  |
| `METODO_PAGO` | VARCHAR2 | YES |  |
| `NUMERO_PAGO` | VARCHAR2 | YES |  |
| `ID_TRANSACCION` | VARCHAR2 | YES |  |
| `PROCESA_ORDENATIVO` | VARCHAR2 | YES |  |
| `SITE_TRANSACTION_ID` | VARCHAR2 | YES |  |
| `ID_TICKET` | VARCHAR2 | YES |  |
| `FECHA_CIERRE_LOTE` | DATE | YES |  |
| `PROCESA_CONTRACARGO` | VARCHAR2 | YES |  |
| `LOTE_COBRANZA` | NUMBER | YES |  |
| `ID_COBRO` | NUMBER | NO | 🔑 PK |
| `FECHA_CARGA` | DATE | YES |  |
| `ORIGEN_LOGS` | NUMBER | YES |  |
| `TIPO_DOC_CTRC` | VARCHAR2 | YES |  |
| `NUMERO_DOC_CTRC` | NUMBER | YES |  |
| `LOG_ID` | NUMBER | YES |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |
| `ID_SOLICITUD` | NUMBER | YES |  |
| `ID_PAGO360` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
- `LOG_ID` → [[XXWW_WEBSERVICE_LOG_30_VM]] _LOG_ID es PK de XXWW_WEBSERVICE_LOG_30_VM_
