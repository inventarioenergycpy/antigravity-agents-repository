---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 18152497
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "OBSERVACIONES_CONTRATO"
---

# 📋 OBSERVACIONES_CONTRATO

**Filas estimadas:** 18,152,497

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `OCO_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `OCO_FECHA` | DATE | NO |  |  |
| `OCO_NOVEDAD` | VARCHAR2 | YES |  |  |
| `OCO_DETALLE` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
