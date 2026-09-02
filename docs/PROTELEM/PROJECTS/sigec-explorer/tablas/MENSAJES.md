---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 2
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "MENSAJES"
---

# 📋 MENSAJES

**Filas estimadas:** 2

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `MSG_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `MSG_TEXTO` | VARCHAR2 | NO |  |  |
| `MSG_ANIO` | NUMBER | YES |  |  |
| `MSG_PERIODO` | NUMBER | YES |  |  |
| `CAT_CODIGO` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
