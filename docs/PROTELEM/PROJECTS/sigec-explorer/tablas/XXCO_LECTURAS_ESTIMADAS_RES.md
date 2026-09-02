---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: contratos
num_rows: 389477
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/contratos
  - documentada/negocio
aliases:
  - "XXCO_LECTURAS_ESTIMADAS_RES"
---

# 🔧 XXCO_LECTURAS_ESTIMADAS_RES

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 389,477

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `CRL_ANIO` | NUMBER | YES |  |  |
| `CRL_PERIODO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `CONS_DIARIO` | NUMBER | YES |  |  |
| `TIPO_CALCULO` | VARCHAR2 | YES |  |  |
| `DIAS_N` | NUMBER | YES |  |  |
| `DIAS_A_ESTIMAR` | NUMBER | YES |  |  |
| `LCT_CODIGO` | NUMBER | YES |  |  |
| `CNT_FECHA_INICIO` | DATE | YES |  |  |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
