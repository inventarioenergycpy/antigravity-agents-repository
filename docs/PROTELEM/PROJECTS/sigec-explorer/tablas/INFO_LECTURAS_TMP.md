---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: lecturas
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "INFO_LECTURAS_TMP"
---

# ⏱️ INFO_LECTURAS_TMP

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SESSION_ID` | NUMBER | YES |  |  |
| `SECUENCIA` | NUMBER | YES |  |  |
| `INDICE` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `POT_DA` | NUMBER | YES |  |  |
| `POT_DAP` | NUMBER | YES |  |  |
| `POT_DAF` | NUMBER | YES |  |  |
| `STE_TIPO` | VARCHAR2 | YES |  | Tipo de equipo/medidor. Completa la PK compuesta de STOCK_EQUIPOS (STE_NUMERO, STE_TIPO); las FK a medidor siempre llevan ambas columnas. |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `LCT_FECHA_LECTURA_01` | DATE | YES |  |  |
| `LCT_CONSUMO_01` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_02` | DATE | YES |  |  |
| `LCT_CONSUMO_02` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_03` | DATE | YES |  |  |
| `LCT_CONSUMO_03` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_04` | DATE | YES |  |  |
| `LCT_CONSUMO_04` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_05` | DATE | YES |  |  |
| `LCT_CONSUMO_05` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_06` | DATE | YES |  |  |
| `LCT_CONSUMO_06` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_07` | DATE | YES |  |  |
| `LCT_CONSUMO_07` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_08` | DATE | YES |  |  |
| `LCT_CONSUMO_08` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_09` | DATE | YES |  |  |
| `LCT_CONSUMO_09` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_10` | DATE | YES |  |  |
| `LCT_CONSUMO_10` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_11` | DATE | YES |  |  |
| `LCT_CONSUMO_11` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_12` | DATE | YES |  |  |
| `LCT_CONSUMO_12` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_13` | DATE | YES |  |  |
| `LCT_CONSUMO_13` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_14` | DATE | YES |  |  |
| `LCT_CONSUMO_14` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_15` | DATE | YES |  |  |
| `LCT_CONSUMO_15` | NUMBER | YES |  |  |
