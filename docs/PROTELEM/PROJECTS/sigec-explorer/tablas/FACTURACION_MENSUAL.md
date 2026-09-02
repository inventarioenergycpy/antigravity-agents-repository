---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 9246300
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "FACTURACION_MENSUAL"
---

# 📋 FACTURACION_MENSUAL

**Filas estimadas:** 9,246,300

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `TEN_CODIGO` | VARCHAR2 | NO |  |  |
| `LCT_FECHA_LECTURA` | DATE | NO |  | Fecha en que se tomó la lectura. |
| `DIAS` | NUMBER | YES |  |  |
| `CONSUMO` | NUMBER | YES |  |  |
| `BAR_CODIGO` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | NO |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `BAR_CODIGO` → [[XXCO_BARRIOS]] _BAR_CODIGO es PK de XXCO_BARRIOS_
