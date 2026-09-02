---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: servicios
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/servicios
  - documentada/negocio
aliases:
  - "EXCESOS_A_FACTURAR_TEMP"
---

# ⏱️ EXCESOS_A_FACTURAR_TEMP

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

> - Retrofitted

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `EFT_NUMERO` | NUMBER | NO |  |  |
| `SRV_PLAN_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_ZONA_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_LOCALIDAD_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_RUTA_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_SUMINISTRO_ORIGINAL` | NUMBER | YES |  | Clave del suministro propagada a tablas de lectura/facturación. |
| `EFT_CANT_MESES` | NUMBER | YES |  |  |
| `EFT_VALOR_LEIDO` | NUMBER | YES |  |  |
| `EFT_ESTADO` | VARCHAR2 | YES |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `EFT_ERROR` | VARCHAR2 | YES |  |  |
