---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "LECTURAS_COOP"
---

# 📋 LECTURAS_COOP

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TCL_CODIGO` | NUMBER | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `PICO1` | NUMBER | YES |  |  |
| `RESTO1` | NUMBER | YES |  |  |
| `VALLE1` | NUMBER | YES |  |  |
| `PICO2` | NUMBER | YES |  |  |
| `RESTO2` | NUMBER | YES |  |  |
| `VALLE2` | NUMBER | YES |  |  |
| `PICO3` | NUMBER | YES |  |  |
| `RESTO3` | NUMBER | YES |  |  |
| `VALLE3` | NUMBER | YES |  |  |
| `T_PICO` | NUMBER | YES |  |  |
| `T_RESTO` | NUMBER | YES |  |  |
| `T_VALLE` | NUMBER | YES |  |  |
