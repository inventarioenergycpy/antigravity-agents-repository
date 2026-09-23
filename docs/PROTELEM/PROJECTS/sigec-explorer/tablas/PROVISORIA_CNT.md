---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: contratos
num_rows: 98
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/contratos
  - documentada/negocio
aliases:
  - "PROVISORIA_CNT"
---

# 📋 PROVISORIA_CNT

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 98

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_FECHA_REQUISITOS` | DATE | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CNT_FECHA_INICIO` | DATE | NO |  |  |
| `GRU` | VARCHAR2 | YES |  |  |
| `CNT_COND_CORTE` | VARCHAR2 | NO |  |  |
