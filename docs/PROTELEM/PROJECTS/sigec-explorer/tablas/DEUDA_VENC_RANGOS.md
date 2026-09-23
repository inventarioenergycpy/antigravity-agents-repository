---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 1953
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "DEUDA_VENC_RANGOS"
---

# 📋 DEUDA_VENC_RANGOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 1,953

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ZONA` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `CNT_ESTADO` | VARCHAR2 | YES |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `MENOR_100_PESOS` | NUMBER | YES |  |  |
| `MENOR_100_CANT` | NUMBER | YES |  |  |
| `DE_100_199_PESOS` | NUMBER | YES |  |  |
| `DE_100_199_CANT` | NUMBER | YES |  |  |
| `DE_200_499_PESOS` | NUMBER | YES |  |  |
| `DE_200_499_CANT` | NUMBER | YES |  |  |
| `DE_500_999_PESOS` | NUMBER | YES |  |  |
| `DE_500_999_CANT` | NUMBER | YES |  |  |
| `DE_1000_1999_PESOS` | NUMBER | YES |  |  |
| `DE_1000_1999_CANT` | NUMBER | YES |  |  |
| `DE_2000_4999_PESOS` | NUMBER | YES |  |  |
| `DE_2000_4999_CANT` | NUMBER | YES |  |  |
| `DE_5000_9999_PESOS` | NUMBER | YES |  |  |
| `DE_5000_9999_CANT` | NUMBER | YES |  |  |
| `DE_10000_19999_PESOS` | NUMBER | YES |  |  |
| `DE_10000_19999_CANT` | NUMBER | YES |  |  |
| `DE_20000_49999_PESOS` | NUMBER | YES |  |  |
| `DE_20000_49999_CANT` | NUMBER | YES |  |  |
| `MAYOR_49999_PESOS` | NUMBER | YES |  |  |
| `MAYOR_49999_CANT` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
