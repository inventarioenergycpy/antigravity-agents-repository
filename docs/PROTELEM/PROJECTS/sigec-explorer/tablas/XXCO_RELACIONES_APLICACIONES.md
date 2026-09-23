---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: cobranza
num_rows: 116597
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/cobranza
aliases:
  - "XXCO_RELACIONES_APLICACIONES"
---

# 🔧 XXCO_RELACIONES_APLICACIONES

**Prefijo `APL_`:** Aplicaciones / imputación de pagos (APLICACIONES)

> Registracion de relaciones entre aplicaciones clasifcadas por tipo

**Filas estimadas:** 116,597

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `APL_NUMERO` | NUMBER | NO | 🔑 PK |
| `APL_NUMERO_RELACION` | NUMBER | NO | 🔑 PK |
| `RAP_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `RAP_OBSERVACIONES` | VARCHAR2 | YES |  |
| `RAP_FECHA` | DATE | YES |  |
