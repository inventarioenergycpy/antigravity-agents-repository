---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 43957
tags:
  - sigec-explorer
  - tabla
  - journal
  - documentada/negocio
aliases:
  - "EXCESOS_A_FACTURAR_JN"
---

# 📝 EXCESOS_A_FACTURAR_JN

**Filas estimadas:** 43,957

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `JN_SECUENCIA_EAF` | NUMBER | YES |  |  |
| `EAF_ANIO` | NUMBER | YES |  |  |
| `EAF_FRECUENCIA` | NUMBER | YES |  |  |
| `EAF_PERIODO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `EAF_CANTIDAD` | NUMBER | YES |  |  |
| `EAF_ESTADO` | VARCHAR2 | YES |  |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `JN_OBSERVACION` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
