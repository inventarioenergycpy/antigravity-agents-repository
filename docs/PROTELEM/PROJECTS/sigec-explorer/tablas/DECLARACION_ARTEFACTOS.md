---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1775773
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "DECLARACION_ARTEFACTOS"
---

# 📋 DECLARACION_ARTEFACTOS

**Filas estimadas:** 1,775,773

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DAR_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `DAR_FECHA_VIGENCIA` | DATE | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DAR_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `USR_CODIGO` | VARCHAR2 | YES |  |  |
| `DAR_FECHA_PASAJE_WEB` | DATE | YES |  |  |
