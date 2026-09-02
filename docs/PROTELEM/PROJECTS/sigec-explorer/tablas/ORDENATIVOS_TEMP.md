---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: servicios
num_rows: 285960
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/servicios
  - documentada/negocio
aliases:
  - "ORDENATIVOS_TEMP"
---

# ⏱️ ORDENATIVOS_TEMP

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 285,960

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ODT_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `ODT_OBSERVACION` | VARCHAR2 | YES |  |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `SRV_PLAN_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_ZONA_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_LOCALIDAD_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_RUTA_ORIGINAL` | NUMBER | YES |  |  |
| `SRV_SUMINISTRO_ORIGINAL` | NUMBER | YES |  | Clave del suministro propagada a tablas de lectura/facturación. |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `ODT_ARRASTRE` | VARCHAR2 | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `PCL_NUMERO` | NUMBER | YES |  |  |
| `ODT_FECHA_CARGA` | DATE | YES |  |  |
