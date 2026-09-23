---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 6901
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "ERSEP_CNT_NO_INTIMA"
---

# 📋 ERSEP_CNT_NO_INTIMA

**Filas estimadas:** 6,901

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CI` | VARCHAR2 | YES |  |  |
| `DNI` | VARCHAR2 | YES |  |  |
| `STICKER1` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `LOCALIDAD` | VARCHAR2 | YES |  |  |
| `MES1` | NUMBER | YES |  |  |
| `ANIO1` | NUMBER | YES |  |  |
| `MES2` | NUMBER | YES |  |  |
| `ANIO2` | NUMBER | YES |  |  |
| `MES3` | NUMBER | YES |  |  |
| `ANIO3` | NUMBER | YES |  |  |
| `FECHA_OFICIO` | DATE | YES |  |  |
| `NRO_NOTA` | VARCHAR2 | YES |  |  |
| `FECHA_NOTA` | DATE | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
