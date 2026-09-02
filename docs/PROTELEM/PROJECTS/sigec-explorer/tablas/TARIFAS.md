---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 405
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "TARIFAS"
---

# 📋 TARIFAS

> [!info] Significado de negocio
> Catálogo de tarifas/clases tarifarias (405 filas). PK TCL_CODIGO. TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO (1=Residencial,2=Comercial,3=Industrial/Grandes Consumos,4=Cooperativas,5=Oficial,6=Alumbrado,7=Servicio de Agua,8=Rural). Peaje y Uso Propio están dentro del grupo 3.

> Tabla de tarifas

**Filas estimadas:** 405

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | NO | 🔑 PK | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `TCL_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `TCL_GRUPO` | VARCHAR2 | NO |  | Grupo/rubro tarifario en TARIFAS. Mapea al sector de venta: 1=Residencial, 2=Comercial(Gral y Serv), 3=Industrial(Grandes Consumos), 4=Cooperativas, 5=Oficial(Gob y Us.Esp.), 6=Alumbrado Público, 7=Servicio de Agua, 8=Rural. Peaje y Uso Propio viven dentro del grupo 3 (identificar por TCL_DESCRIPCION). |
| `TCL_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |  |
| `TCL_LEY_PAE` | VARCHAR2 | YES |  |  |
| `TCL_BASE_LEY` | VARCHAR2 | YES |  |  |
| `TCL_GARANTES_FLAG` | VARCHAR2 | NO |  |  |
| `TCL_COOPERATIVAS_FLAG` | VARCHAR2 | YES |  |  |
| `TCL_LCT_SITIO` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO_BASE` | VARCHAR2 | YES |  |  |
| `TCL_INGRESOS_BRUTOS` | VARCHAR2 | YES |  |  |
| `TCL_CARGO_NNO` | VARCHAR2 | YES |  |  |
| `TCL_ESTADO` | VARCHAR2 | YES |  |  |
| `TCL_APLICA_AXO_TCL_REC_BON` | VARCHAR2 | YES |  |  |

## Tablas que referencian esta tabla

- [[CLASES]] via `TCL_CODIGO`
- [[CONCEPTOS_TARIFAS]] via `TCL_CODIGO`
- [[CUADRANTES_TARIFA]] via `TCL_CODIGO`
- [[CUADRANTES_TARIFA_DET]] via `TCL_CODIGO`
- [[LIQUIDACIONES_ILICITOS]] via `TCL_CODIGO`
- [[XX_TARIFAS_GRUPOS]] via `TCL_CODIGO`
