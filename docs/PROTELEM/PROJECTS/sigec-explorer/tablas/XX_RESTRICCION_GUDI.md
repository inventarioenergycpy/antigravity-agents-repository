---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 3
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "XX_RESTRICCION_GUDI"
---

# 📋 XX_RESTRICCION_GUDI

**Filas estimadas:** 3

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `RG_NRO` | NUMBER | NO | 🔑 PK |
| `RG_FEC_DESDE` | DATE | NO |  |
| `RG_FEC_HASTA` | DATE | NO |  |
| `RG_MENSAJE` | VARCHAR2 | NO |  |
| `USR_NUMERO` | NUMBER | YES |  |
| `RG_FECHA_ALTA` | DATE | NO |  |
| `RG_ASUNTO` | VARCHAR2 | NO |  |

## Tablas que referencian esta tabla

- [[XX_RESTRICCION_GUDI_ENVIOS]] via `RG_NRO`
