---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 7573487
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "POTENCIAS"
---

# 📋 POTENCIAS

**Filas estimadas:** 7,573,487

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `POT_ORIGEN` | VARCHAR2 | NO |  |  |
| `POT_FECHA` | DATE | NO |  |  |
| `POT_VALOR` | NUMBER | NO |  |  |
| `POT_ESTADO` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `POT_FECHA_ALTA` | DATE | YES |  |  |
| `POT_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `POT_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
