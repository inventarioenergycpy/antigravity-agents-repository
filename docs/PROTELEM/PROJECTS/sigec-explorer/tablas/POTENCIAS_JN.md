---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 11632
tags:
  - sigec-explorer
  - tabla
  - journal
  - documentada/negocio
aliases:
  - "POTENCIAS_JN"
---

# 📝 POTENCIAS_JN

**Filas estimadas:** 11,632

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `POT_ORIGEN` | VARCHAR2 | YES |  |  |
| `POT_FECHA` | DATE | YES |  |  |
| `POT_VALOR` | NUMBER | YES |  |  |
| `POT_ESTADO` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `POT_OBSERVACION` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
