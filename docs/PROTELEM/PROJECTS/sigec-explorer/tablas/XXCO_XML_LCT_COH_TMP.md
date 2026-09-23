---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: lecturas
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "XXCO_XML_LCT_COH_TMP"
---

# ⏱️ XXCO_XML_LCT_COH_TMP

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ANIO` | NUMBER | YES |  |  |
| `MES` | NUMBER | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `CONSUMO` | NUMBER | YES |  |  |
| `TIPO_LECTURA` | VARCHAR2 | YES |  |  |
| `CANTIDAD_DIAS` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `ANIO_PERIODO` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA` | DATE | YES |  | Fecha en que se tomó la lectura. |
| `LCT_VALOR_LEIDO` | NUMBER | YES |  | Valor leído del medidor en esa lectura (estado del contador). |
| `LCT_FECHA_LECTURA_ANT` | DATE | YES |  |  |
| `LCT_VALOR_LEIDO_ANT` | NUMBER | YES |  |  |
| `GRM_NUMERO` | NUMBER | YES |  |  |
| `LCT_ESTADO` | VARCHAR2 | YES |  |  |
| `EQP_ORDEN` | NUMBER | YES |  |  |
