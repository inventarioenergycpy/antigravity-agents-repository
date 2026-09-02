---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 1224560
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "ANALISIS_FACT_DETALLE_TABLA"
---

# 📋 ANALISIS_FACT_DETALLE_TABLA

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 1,224,560

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ZON_CODIGO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `AGF_CODIGO_OIM` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `CANT_FACT` | NUMBER | YES |  |  |
| `CANT_ENERGIA` | NUMBER | YES |  |  |
| `CANT_ECO` | NUMBER | YES |  |  |
| `CANT_EDI` | NUMBER | YES |  |  |
| `CANT_ENO` | NUMBER | YES |  |  |
| `CANT_EPI` | NUMBER | YES |  |  |
| `CANT_ERE` | NUMBER | YES |  |  |
| `CANT_EVA` | NUMBER | YES |  |  |
| `CANT_DEM` | NUMBER | YES |  |  |
| `CANT_EXC` | NUMBER | YES |  |  |
| `IMPORTE_CFI` | NUMBER | YES |  |  |
| `IMPORTE_ECO` | NUMBER | YES |  |  |
| `IMPORTE_EDI` | NUMBER | YES |  |  |
| `IMPORTE_ENO` | NUMBER | YES |  |  |
| `IMPORTE_EPI` | NUMBER | YES |  |  |
| `IMPORTE_ERE` | NUMBER | YES |  |  |
| `IMPORTE_EVA` | NUMBER | YES |  |  |
| `IMPORTE_DEM` | NUMBER | YES |  |  |
| `IMPORTE_EXC` | NUMBER | YES |  |  |
| `IMPORTE_ENERGIA` | NUMBER | YES |  |  |
| `IMPORTE_CMI` | NUMBER | YES |  |  |
| `IMPORTE_COS` | NUMBER | YES |  |  |
| `IMPORTE_OTROS_DEB` | NUMBER | YES |  |  |
| `IMPORTE_OTROS_CRED` | NUMBER | YES |  |  |
| `IMPORTE_IVA` | NUMBER | YES |  |  |
| `IMPORTE_DGI` | NUMBER | YES |  |  |
| `IMPORTE_OIM` | NUMBER | YES |  |  |
| `IMPORTE_NAC` | NUMBER | YES |  |  |
| `IMPORTE_TOT` | NUMBER | YES |  |  |
| `CANT_DEP` | NUMBER | YES |  |  |
| `CANT_DEF` | NUMBER | YES |  |  |
| `CANT_DEC` | NUMBER | YES |  |  |
| `IMPORTE_DEP` | NUMBER | YES |  |  |
| `IMPORTE_DEF` | NUMBER | YES |  |  |
| `IMPORTE_DEC` | NUMBER | YES |  |  |
| `CANT_DRD` | NUMBER | YES |  |  |
| `IMPORTE_DRD` | NUMBER | YES |  |  |
| `IMPORTE_EEP` | NUMBER | YES |  |  |
| `IMPORTE_EEV` | NUMBER | YES |  |  |
| `IMPORTE_EER` | NUMBER | YES |  |  |
| `F75_FECHA_CARGA` | DATE | YES |  |  |
| `AFT_FOTO` | NUMBER | YES |  |  |
| `IMPORTE_SUBSI` | NUMBER | YES |  |  |
| `IMPORTE_SUBSI_DEV` | NUMBER | YES |  |  |
| `IMPORTE_SPI` | NUMBER | YES |  |  |
| `IMPORTE_SRE` | NUMBER | YES |  |  |
| `IMPORTE_SVA` | NUMBER | YES |  |  |
| `CANT_SPI` | NUMBER | YES |  |  |
| `CANT_SRE` | NUMBER | YES |  |  |
| `CANT_SVA` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
