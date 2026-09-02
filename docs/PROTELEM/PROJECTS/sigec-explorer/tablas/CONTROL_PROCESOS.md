---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 2903287
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "CONTROL_PROCESOS"
---

# 📋 CONTROL_PROCESOS

**Filas estimadas:** 2,903,287

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `CPR_NUMERO` | NUMBER | NO | 🔑 PK |
| `CPR_TIPO_PROCESO` | VARCHAR2 | NO |  |
| `CPR_FECHA_INICIO` | DATE | YES |  |
| `CPR_FECHA_FIN` | DATE | YES |  |
| `USR_NUMERO_INCORPORA` | NUMBER | NO |  |
| `USR_NUMERO_ACTUALIZA` | NUMBER | YES |  |
| `CPR_NUMERO_PADRE` | NUMBER | YES |  |
| `URC_CODIGO` | NUMBER | YES |  |
| `CPR_CANT_REG` | NUMBER | YES |  |
| `CPR_IMPORTE` | NUMBER | YES |  |
| `CPR_OBSERVACIONES` | VARCHAR2 | YES |  |
| `PRC_CODIGO` | VARCHAR2 | NO |  |
| `EST_CODIGO` | VARCHAR2 | NO |  |
| `CPR_FECHA_RENDICION` | DATE | YES |  |
| `SCF_CODIGO` | NUMBER | YES |  |
| `ASI_NUMERO` | NUMBER | YES |  |
| `MPA_TIPO_MEDIO_PAGO` | VARCHAR2 | YES |  |
| `URC_CODIGO_MPA` | NUMBER | YES |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |
| `CPR_TIPO_CARGA` | VARCHAR2 | YES |  |
| `CPR_ULTIMA_ACTUALIZACION` | DATE | YES |  |

## FK inferidas (alta confianza)

- `MPA_TIPO_MEDIO_PAGO` → [[MEDIOS_PAGO]] _MPA_TIPO_MEDIO_PAGO es PK de MEDIOS_PAGO_
