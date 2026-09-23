---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 28096100
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "LECTURAS_TEMP_HISTO"
---

# 📋 LECTURAS_TEMP_HISTO

**Prefijo `LTM_`:** Lecturas temporales (LECTURAS_TEMP)

**Filas estimadas:** 28,096,100

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `LTM_FECHA_LECTURA` | DATE | YES |  |  |
| `HORA` | VARCHAR2 | YES |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `LTM_VALOR_LEIDO` | NUMBER | YES |  |  |
| `USR_CODIGO` | NUMBER | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `PCL_NUMERO` | NUMBER | YES |  |  |
| `TOT_CONS_ESTADO` | NUMBER | YES |  |  |
| `TOT_INTENTOS_GRABAR` | NUMBER | YES |  |  |
| `LTM_ORDEN_LECTURA` | NUMBER | YES |  |  |
