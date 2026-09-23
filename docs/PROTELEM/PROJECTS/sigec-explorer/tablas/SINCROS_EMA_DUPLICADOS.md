---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 325
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
aliases:
  - "SINCROS_EMA_DUPLICADOS"
---

# 📋 SINCROS_EMA_DUPLICADOS

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 325

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SIN_NUMERO` | NUMBER | NO |  |
| `GRL_CODIGO` | VARCHAR2 | NO |  |
| `GRL_ANIO` | NUMBER | NO |  |
| `GRL_PERIODO` | NUMBER | NO |  |
| `RTL_CODIGO` | NUMBER | NO |  |
| `SCF_CODIGO` | NUMBER | YES |  |
| `SIR_NUMERO` | NUMBER | NO |  |
| `SIN_FECHA_SINCRONIZACION` | DATE | YES |  |
| `CLIENTES_ENVIADOS` | NUMBER | YES |  |
| `CLIENTES_RECIBIDOS` | NUMBER | YES |  |
| `LCT_FECHA_LECTURA_MIN` | DATE | YES |  |
| `LCT_FECHA_LECTURA_MAX` | DATE | YES |  |
| `FOTO` | NUMBER | YES |  |
| `LECTURAS_EN_PROD` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `SIN_NUMERO` → [[XXCO_OBSERVACIONES_ORDENATIVO]] _SIN_NUMERO es PK de XXCO_OBSERVACIONES_ORDENATIVO_
