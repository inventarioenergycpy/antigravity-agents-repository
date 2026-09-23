---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 851983
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "ORDENATIVOS_TEMP_HISTO"
---

# 📋 ORDENATIVOS_TEMP_HISTO

**Filas estimadas:** 851,983

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `ODH_OBSERVACION` | VARCHAR2 | YES |  |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `ODH_ARRASTRE` | VARCHAR2 | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `PCL_NUMERO` | NUMBER | YES |  |  |
| `ODH_FECHA_CARGA` | DATE | YES |  |  |
