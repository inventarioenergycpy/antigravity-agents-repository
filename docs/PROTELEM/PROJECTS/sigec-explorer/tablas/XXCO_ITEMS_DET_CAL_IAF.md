---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 16320
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_ITEMS_DET_CAL_IAF"
---

# 🔧 XXCO_ITEMS_DET_CAL_IAF

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 16,320

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `CONSUMO` | NUMBER | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | YES |  |  |
| `DCAI_FACT_PRE_UNIT` | NUMBER | YES |  |  |
| `DCAI_FACT_IMPORTE` | NUMBER | YES |  |  |
| `DCAI_FACT_CANTIDAD` | NUMBER | YES |  |  |
| `DCAI_RECA_PRE_UNIT` | NUMBER | YES |  |  |
| `DCAI_RECA_IMPORTE` | NUMBER | YES |  |  |
| `DCAI_RECA_CANTIDAD` | NUMBER | YES |  |  |
| `DCAI_SUB_PRE_UNIT` | NUMBER | YES |  |  |
| `DCAI_SUB_IMPORTE` | NUMBER | YES |  |  |
| `DCAI_SUB_CANTIDAD` | NUMBER | YES |  |  |
| `DCAI_PERIODO` | NUMBER | YES |  |  |
| `IAF_NUMERO` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
