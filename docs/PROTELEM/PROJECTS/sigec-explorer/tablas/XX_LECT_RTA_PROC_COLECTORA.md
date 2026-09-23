---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 37189227
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "XX_LECT_RTA_PROC_COLECTORA"
---

# 📋 XX_LECT_RTA_PROC_COLECTORA

**Filas estimadas:** 37,189,227

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PCL_NUMERO` | NUMBER | NO |  |  |
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `RTA_CODIGO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `STE_NUMERO` | NUMBER | NO |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
