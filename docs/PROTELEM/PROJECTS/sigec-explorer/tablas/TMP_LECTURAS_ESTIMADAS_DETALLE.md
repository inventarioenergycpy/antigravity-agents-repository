---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 134730
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "TMP_LECTURAS_ESTIMADAS_DETALLE"
---

# 📋 TMP_LECTURAS_ESTIMADAS_DETALLE

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 134,730

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LTE_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `LCT_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `LCT_FECHA_LECTURA` | DATE | YES |  | Fecha en que se tomó la lectura. |
| `LCT_CONSUMO` | NUMBER | YES |  | Consumo calculado del período (diferencia entre lecturas). |
| `LCT_TIPO_LECTURA` | VARCHAR2 | YES |  |  |
| `LCT_CANT_DIAS` | NUMBER | YES |  |  |
| `LCT_PROM_DIARIO` | NUMBER | YES |  |  |
| `LCT_TIPO_LECTURA_ANT` | VARCHAR2 | YES |  |  |
| `LCT_CANT_DIAS_ANT` | NUMBER | YES |  |  |
| `LCT_CONSUMO_MENSUAL_ANT` | NUMBER | YES |  |  |
| `LCT_CONSUMO_DIARIO_ANT` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_ANT` | DATE | YES |  |  |
| `LCT_FECHA_LECTURA_ANTERIOR_ANT` | DATE | YES |  |  |
| `LCT_VALOR_LEIDO_ANT` | NUMBER | YES |  |  |
| `LTD_DIF_LCT_LCT_ANT` | NUMBER | YES |  |  |
| `LTD_DIF_PROM_LCT_LCT_ANT` | NUMBER | YES |  |  |
| `LTE_PORC_DIF_CONSUMO` | NUMBER | YES |  |  |
