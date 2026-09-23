---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 26360
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "TEMP_INDICADORES_ENTE"
---

# 📋 TEMP_INDICADORES_ENTE

**Filas estimadas:** 26,360

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ANIO` | NUMBER | YES |  |
| `PERIODO` | NUMBER | YES |  |
| `ZON_CODIGO` | VARCHAR2 | YES |  |
| `ENTE` | NUMBER | YES |  |
| `IMPORTE_ORIGINAL` | NUMBER | YES |  |
| `SALDO` | NUMBER | YES |  |
| `FECHA_EJEC` | DATE | YES |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
