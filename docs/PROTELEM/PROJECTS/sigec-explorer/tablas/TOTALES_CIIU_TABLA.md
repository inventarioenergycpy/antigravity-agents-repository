---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 310063
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "TOTALES_CIIU_TABLA"
---

# 📋 TOTALES_CIIU_TABLA

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 310,063

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ZON_CODIGO` | VARCHAR2 | YES |  |  |
| `CNT_CIIU` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | YES |  |  |
| `CANT_CNT` | NUMBER | YES |  |  |
| `CANT_KWH` | NUMBER | YES |  |  |
| `IMPORTE_ENERGIA` | NUMBER | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
- `CNT_CIIU` → [[CODIGOS_CIIU]] _CNT_CIIU es PK de CODIGOS_CIIU_
