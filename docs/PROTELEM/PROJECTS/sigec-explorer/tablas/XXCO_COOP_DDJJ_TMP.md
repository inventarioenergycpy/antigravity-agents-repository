---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: lecturas
num_rows: 220
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "XXCO_COOP_DDJJ_TMP"
---

# ⏱️ XXCO_COOP_DDJJ_TMP

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 220

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `LCT_ANIO` | NUMBER | YES |  |  |
| `LCT_PERIODO` | NUMBER | YES |  |  |
| `CDJ_IIBB` | NUMBER | YES |  |  |
| `CDJ_SUBSIDIO` | NUMBER | YES |  |  |
| `CDJ_CLIENTES_CARENCIADOS` | NUMBER | YES |  |  |
| `CDJ_CLIENTES_INDIGENTES` | NUMBER | YES |  |  |
| `CDJ_CONSUMO_1` | NUMBER | YES |  |  |
| `CDJ_CONSUMO_2` | NUMBER | YES |  |  |
| `CDJ_CONSUMO_3` | NUMBER | YES |  |  |
| `CDJ_CONSUMO_4` | NUMBER | YES |  |  |
| `CDJ_CONSUMO_5` | NUMBER | YES |  |  |
| `CDJ_CONSUMO_6` | NUMBER | YES |  |  |
| `CDJ_CONSUMO_7` | NUMBER | YES |  |  |
| `CDJ_CONSUMO_8` | NUMBER | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `FECHA_CALCULO` | DATE | YES |  |  |
| `CDJ_SUBSIDIO_CALCULADO` | NUMBER | YES |  |  |
| `IAF_NUMERO_SUB` | NUMBER | YES |  |  |
| `IAF_NUMERO_IIBB` | NUMBER | YES |  |  |
