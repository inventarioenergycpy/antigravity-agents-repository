---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: lecturas
num_rows: 67700907
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "XXCO_LECTURAS_AJUSTADAS_ORIG"
---

# 🔧 XXCO_LECTURAS_AJUSTADAS_ORIG

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 67,700,907

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LCT_CODIGO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO |  |  |
| `EQP_ORDEN` | NUMBER | NO |  |  |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `LCT_FECHA_LECTURA` | DATE | NO |  | Fecha en que se tomó la lectura. |
| `LCT_VALOR_LEIDO` | NUMBER | NO |  | Valor leído del medidor en esa lectura (estado del contador). |
| `LCT_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `LCT_VALOR_LEIDO_ANTERIOR` | NUMBER | YES |  |  |
| `LCT_CONSUMO` | NUMBER | YES |  | Consumo calculado del período (diferencia entre lecturas). |
| `LCT_CONSUMO_INFORMADO` | NUMBER | YES |  |  |
| `LCT_ESTADO` | VARCHAR2 | YES |  |  |
| `LCT_ORIGEN` | VARCHAR2 | YES |  |  |
| `LCT_FECHA_CARGA` | DATE | YES |  |  |
| `LCT_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `LCT_CODIGO_ORIGEN` | NUMBER | YES |  |  |
| `LCT_ANIO` | NUMBER | YES |  |  |
| `LCT_PERIODO` | NUMBER | YES |  |  |
| `LCT_FECHA_CARGA_AJUSTE` | DATE | YES |  |  |
