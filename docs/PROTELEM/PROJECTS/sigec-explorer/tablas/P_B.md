---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 41270
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "P_B"
---

# 📋 P_B

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 41,270

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `LCT_FECHA_LECTURA` | DATE | YES |  | Fecha en que se tomó la lectura. |
| `LCT_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `LCT_VALOR_LEIDO` | NUMBER | YES |  | Valor leído del medidor en esa lectura (estado del contador). |
| `LCT_VALOR_LEIDO_ANTERIOR` | NUMBER | YES |  |  |
| `LCT_CONSUMO` | NUMBER | YES |  | Consumo calculado del período (diferencia entre lecturas). |
| `LCT_CONSUMO_INFORMADO` | NUMBER | YES |  |  |
| `SRV_CODIGO_N` | NUMBER | YES |  |  |
| `LCT_FECHA_LECTURA_N` | DATE | YES |  |  |
| `LCT_FECHA_LECTURA_ANTERIOR_N` | DATE | YES |  |  |
| `LCT_VALOR_LEIDO_N` | NUMBER | YES |  |  |
| `LCT_VALOR_LEIDO_ANTERIOR_N` | NUMBER | YES |  |  |
| `LCT_CONSUMO_N` | NUMBER | YES |  |  |
| `LCT_CONSUMO_INFORMADO_N` | NUMBER | YES |  |  |
| `NRO_SESSION` | NUMBER | YES |  |  |
| `USR_UNIX` | VARCHAR2 | YES |  |  |
| `NRO_ORACLE` | NUMBER | YES |  |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |  |
| `SERVIDOR` | VARCHAR2 | YES |  |  |
| `TERMINAL` | VARCHAR2 | YES |  |  |
| `PROGRAMA` | VARCHAR2 | YES |  |  |
| `OPERACION` | VARCHAR2 | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
