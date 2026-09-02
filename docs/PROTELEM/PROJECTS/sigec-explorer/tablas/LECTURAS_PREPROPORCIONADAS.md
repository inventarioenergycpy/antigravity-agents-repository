---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 21640027
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "LECTURAS_PREPROPORCIONADAS"
---

# 📋 LECTURAS_PREPROPORCIONADAS

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 21,640,027

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO |  |  |
| `EQP_ORDEN` | NUMBER | NO |  |  |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `LCT_FECHA_LECTURA` | DATE | NO |  | Fecha en que se tomó la lectura. |
| `LCT_VALOR_LEIDO` | NUMBER | NO |  | Valor leído del medidor en esa lectura (estado del contador). |
| `LCT_CONSUMO` | NUMBER | NO |  | Consumo calculado del período (diferencia entre lecturas). |
| `LCT_TIPO_LECTURA` | VARCHAR2 | YES |  |  |
| `LEP_FECHA_LECTURA_NUEVA` | DATE | NO |  |  |
| `LEP_FECHA_CARGA` | DATE | NO |  |  |
| `LEP_USR_NUMERO` | NUMBER | NO |  |  |
| `LCT_CODIGO` | NUMBER | YES |  |  |
| `LCT_CONSUMO_INFORMADO` | NUMBER | YES |  |  |
