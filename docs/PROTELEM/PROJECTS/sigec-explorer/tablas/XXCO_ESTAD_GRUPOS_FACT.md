---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 29664
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_ESTAD_GRUPOS_FACT"
---

# 🔧 XXCO_ESTAD_GRUPOS_FACT

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 29,664

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CRF_ANIO` | NUMBER | NO | 🔑 PK |  |
| `CRF_PERIODO` | NUMBER | NO | 🔑 PK |  |
| `GRF_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `DOC_FECHA_VENC_1` | DATE | YES |  | LA fecha de vencimiento de la factura: es la unica poblada (100% de las facturas 2025). DOC_FECHA_VENC_2 y DOC_FECHA_VENC_3 estan VACIAS (0 filas), igual que DOC_RECARGO_VENC_2 y _VENC_3 — no existen 2do/3er vencimiento en los datos, aunque el modelo los prevea. DOC_FECHA_VENC es redundante (= VENC_1 en 99,99%). Tiempos medios: emision -> vencimiento 27,4 dias; fin del periodo leido -> vencimiento 47,7 dias. |
| `DOC_FECHA_VENC_2` | DATE | YES |  |  |
| `DOC_FECHA_VENC_3` | DATE | YES |  |  |
| `DIAS_A_INTIMAR` | NUMBER | YES |  |  |
| `EST_FECHA_INTIMACION` | DATE | YES |  |  |
| `EST_ESTADO` | VARCHAR2 | YES |  |  |
| `CANTIDAD` | NUMBER | YES |  |  |
| `NRO_MIN` | NUMBER | YES |  |  |
| `NRO_MAX` | NUMBER | YES |  |  |
| `FECHA_REAL_INTIMACION` | DATE | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `GRF_FACT_OBSERVACION` | VARCHAR2 | YES |  |  |

## Tablas que referencian esta tabla

- [[XXCO_ESTAD_GRUPOS_FACT_INT]] via `CRF_ANIO`, `CRF_PERIODO`, `GRF_CODIGO`, `SCF_CODIGO`
