---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 15572
tags:
  - sigec-explorer
  - tabla
  - journal
  - documentada/negocio
aliases:
  - "CUADRANTES_JN"
---

# 📝 CUADRANTES_JN

**Filas estimadas:** 15,572

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO |  |  |
| `EQP_ORDEN` | NUMBER | NO |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `JN_USUARIO` | NUMBER | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `CDR_ORDEN` | NUMBER | YES |  |  |
| `CDR_ENTEROS` | NUMBER | YES |  |  |
| `CDR_DECIMALES` | NUMBER | YES |  |  |
| `OBSERVACION` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
