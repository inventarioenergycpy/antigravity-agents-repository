---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 866
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "TIPOS_ITEM"
---

# 📋 TIPOS_ITEM

**Filas estimadas:** 866

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TIT_CLAVE` | VARCHAR2 | NO | 🔑 PK |  |
| `TIT_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `TIT_DESCRIPCION_COMPLETA` | VARCHAR2 | YES |  |  |
| `TIT_GRUPO` | VARCHAR2 | YES |  |  |
| `GIT_GRUPO` | VARCHAR2 | YES |  |  |
| `TIT_IVA` | VARCHAR2 | YES |  |  |
| `GII_CODIGO` | VARCHAR2 | YES | 🔗 → [[GRUPOS_ITEM_IVA]] |  |
| `TIT_PERCEPCION` | VARCHAR2 | YES |  |  |
| `TIT_LEY` | VARCHAR2 | YES |  |  |
| `GIL_CODIGO` | VARCHAR2 | YES | 🔗 → [[GRUPOS_ITEM_LEY]] |  |
| `TIT_OIM` | VARCHAR2 | YES |  |  |
| `TIT_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |  |
| `TIT_PORCENTAJE_REEMBOLSO` | NUMBER | YES |  |  |
| `TIT_CONSUMO` | VARCHAR2 | YES |  |  |
| `TIT_COS_FI` | VARCHAR2 | YES |  |  |
| `TIT_GRUPO_LISTADO` | VARCHAR2 | YES |  |  |
| `TIT_GRUPO_LISTADO_1` | VARCHAR2 | YES |  |  |
| `TIT_GRUPO_LISTADO_2` | VARCHAR2 | YES |  |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `SEC_CODIGO_ORIGEN` | VARCHAR2 | YES |  |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | YES |  | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `TIT_GRUPO_ESTADISTICO` | VARCHAR2 | YES |  |  |
| `TIT_CALCULO_FLAG` | VARCHAR2 | YES |  |  |
| `TIT_LEY_PAE` | VARCHAR2 | YES |  |  |
| `TIT_PRESUPUESTARIO` | VARCHAR2 | YES |  |  |
| `TIT_ORDEN_IMPRESION` | NUMBER | YES |  |  |
| `TIT_INTERFACE_CE` | VARCHAR2 | YES |  |  |
| `TIT_CANT_PRECIO_IAF` | VARCHAR2 | YES |  |  |
| `TIT_IB` | VARCHAR2 | YES |  |  |
| `TIT_GRUPO_IB` | VARCHAR2 | YES |  |  |
| `TIT_CARGO_NNO` | VARCHAR2 | YES |  |  |
| `TIT_AJUSTE_AUTOMATICO` | VARCHAR2 | YES |  |  |
| `TIT_TIPO_CARGO` | VARCHAR2 | YES |  |  |
| `TIT_ORIGEN_IMPUESTO` | VARCHAR2 | YES |  |  |
| `TIT_CAMMESA` | VARCHAR2 | YES |  |  |
| `TIT_SUBS_COOP` | VARCHAR2 | YES |  |  |
| `TIT_BANDA_HORARIA` | VARCHAR2 | YES |  |  |
| `TIT_POTENCIA` | VARCHAR2 | YES |  |  |
| `TIT_SEGMENTO` | NUMBER | YES |  |  |
| `TIT_CARGO_OIE` | VARCHAR2 | YES |  |  |
| `TIT_CONCEPTO` | VARCHAR2 | YES |  |  |
| `ITM_UNIDAD` | VARCHAR2 | YES |  |  |
| `TIT_DESCRIPCION_LARGA` | VARCHAR2 | YES |  |  |
| `TIT_VIGENCIA_DESDE` | DATE | YES |  |  |
| `TIT_VIGENCIA_HASTA` | DATE | YES |  |  |

## FK declaradas → otras tablas

- **TIT_FK_GII**: `GII_CODIGO` → [[GRUPOS_ITEM_IVA]] (`GII_CODIGO`)
- **TIT_FK_GIL**: `GIL_CODIGO` → [[GRUPOS_ITEM_LEY]] (`GIL_CODIGO`)

## Tablas que referencian esta tabla

- [[CONCEPTOS_TARIFAS]] via `TIT_CLAVE`
- [[DETALLES_IVA_ADICIONAL]] via `TIT_CLAVE`
- [[DETALLES_IVA_PERCEPCION]] via `TIT_CLAVE`
- [[DETALLES_LEY]] via `TIT_CLAVE`
- [[DETALLES_OIM]] via `TIT_CLAVE`
- [[DETALLES_PENALIZACION]] via `TIT_CLAVE`
- [[ESCALONES]] via `TIT_CLAVE`
- [[ITEMS_IVA]] via `TIT_CLAVE`
- [[PENALIZACIONES]] via `TIT_CLAVE_BONIF`, `TIT_CLAVE_PENALIZ`
- [[PRECIOS_PRESTACION]] via `TIT_CLAVE`
- [[STOCK_ELEMENTOS]] via `TIT_CLAVE`
- [[XXCO_ITEMS_ING_BRUTOS]] via `TIT_CLAVE`
- [[XX_TOTALES_INFORMES_VARIOS]] via `TIT_CLAVE`
