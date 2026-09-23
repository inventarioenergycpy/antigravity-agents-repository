---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 6313537
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_ESTADISTICAS_POST"
---

# 🔧 XXCO_ESTADISTICAS_POST

**Filas estimadas:** 6,313,537

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CRF_ANIO` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_ESTADISTICAS]] |  |
| `CRF_PERIODO` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_ESTADISTICAS]] |  |
| `GRF_CODIGO` | VARCHAR2 | NO | 🔑 PK · 🔗 → [[XXCO_ESTADISTICAS]] |  |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_ESTADISTICAS]] |  |
| `EST_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_ESTADISTICAS]] |  |
| `EST_COMPROBANTES` | NUMBER | NO | 🔑 PK · 🔗 → [[XXCO_ESTADISTICAS]] |  |
| `ESP_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |

## FK declaradas → otras tablas

- **XXCO_ESTADISTICAS_POST_R01**: `EST_CODIGO`, `GRF_CODIGO`, `SCF_CODIGO`, `CRF_ANIO`, `CRF_PERIODO`, `EST_COMPROBANTES` → [[XXCO_ESTADISTICAS]] (`EST_CODIGO`, `GRF_CODIGO`, `SCF_CODIGO`, `CRF_ANIO`, `CRF_PERIODO`, `EST_COMPROBANTES`)
