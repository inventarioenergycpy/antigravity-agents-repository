---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 640
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "PRECIOS_TARIFA_OTROS"
---

# 📋 PRECIOS_TARIFA_OTROS

**Filas estimadas:** 640

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PTO_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `TEN_CODIGO` | VARCHAR2 | NO |  |  |
| `PTO_FECHA_VIGENCIA` | DATE | NO |  |  |
| `PTO_FECHA_CARGA` | DATE | NO |  |  |
| `PTO_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `PTO_ESTADO` | VARCHAR2 | NO |  |  |

## Tablas que referencian esta tabla

- [[DETALLES_LISTA_OTROS]] via `PTO_NUMERO`
