---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 416
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "VOLVER_ATRAS_RUTAS"
---

# 📋 VOLVER_ATRAS_RUTAS

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 416

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA` | DATE | YES |  | Fecha en que se tomó la lectura. |
| `CANT_DIAS` | NUMBER | YES |  |  |
| `LCT_VALOR_LEIDO` | NUMBER | YES |  | Valor leído del medidor en esa lectura (estado del contador). |
| `LCT_CONSUMO` | NUMBER | YES |  | Consumo calculado del período (diferencia entre lecturas). |
| `FECHA_CARGA_TABLA` | DATE | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `MARCA` | VARCHAR2 | YES |  |  |
