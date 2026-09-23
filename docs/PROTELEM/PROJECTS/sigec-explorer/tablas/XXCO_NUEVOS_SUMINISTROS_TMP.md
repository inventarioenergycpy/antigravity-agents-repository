---
tipo: tabla
categoria: temp
owner: XXSIGEC
tags:
  - sigec-explorer
  - tabla
  - temp
  - documentada/negocio
aliases:
  - "XXCO_NUEVOS_SUMINISTROS_TMP"
---

# ⏱️ XXCO_NUEVOS_SUMINISTROS_TMP

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `NRO_CONTANCIA` | NUMBER | YES |  |  |
| `TITULAR` | VARCHAR2 | YES |  |  |
| `TIPO_NRO_DOC` | VARCHAR2 | YES |  |  |
| `CUIT` | VARCHAR2 | YES |  |  |
| `MAIL` | VARCHAR2 | YES |  |  |
| `DOMIC_CALLE` | VARCHAR2 | YES |  |  |
| `DOMIC_BARRIO_LOC` | VARCHAR2 | YES |  |  |
| `DOMIC_CP` | VARCHAR2 | YES |  |  |
| `DOMIC_PROVINCIA` | VARCHAR2 | YES |  |  |
| `TE_CEL` | VARCHAR2 | YES |  |  |
| `TIPO_SUMIN` | VARCHAR2 | YES |  |  |
| `ACTIVIDAD` | VARCHAR2 | YES |  |  |
| `OTRA_ACTIVIDAD` | VARCHAR2 | YES |  |  |
| `SUMIN_CALLE` | VARCHAR2 | YES |  |  |
| `SUMIN_BARRIO_LOC` | VARCHAR2 | YES |  |  |
| `SUMIN_CP` | VARCHAR2 | YES |  |  |
| `SUMIN_PROVINCIA` | VARCHAR2 | YES |  |  |
| `DATOS_CATASTRALES` | VARCHAR2 | YES |  |  |
| `FACT_CALLE` | VARCHAR2 | YES |  |  |
| `FACT_BARRIO_LOC` | VARCHAR2 | YES |  |  |
| `FACT_CP` | VARCHAR2 | YES |  |  |
| `FECHA` | DATE | YES |  |  |
| `CLAVE` | VARCHAR2 | YES |  |  |
| `PROPIEDAD` | VARCHAR2 | YES |  |  |
| `MEDIDOR` | VARCHAR2 | YES |  | Número de medidor, pero SOLO en 4 tablas de carga/TMP (ACTA_TMP, XXCO_XML_*). La clave real y extendida de medidor es STE_NUMERO. No existe columna NRO_MEDIDOR. |
| `CLIENTE` | NUMBER | YES |  |  |
| `CONTRATO` | VARCHAR2 | YES |  |  |
| `VERIFICADOR` | NUMBER | YES |  |  |
| `OBSERVACIONES` | CLOB | YES |  |  |
| `FACT_PROVINCIA` | VARCHAR2 | YES |  |  |
| `DIRECCION_CALLE` | VARCHAR2 | YES |  |  |
| `DIRECCION_NRO` | VARCHAR2 | YES |  |  |
| `DIRECCION_PISO` | VARCHAR2 | YES |  |  |
| `DIRECCION_DPTO` | VARCHAR2 | YES |  |  |
| `DIRECCION_LOCAL` | VARCHAR2 | YES |  |  |
| `DIRECCION_TORRE` | VARCHAR2 | YES |  |  |
| `DIRECCION_LOTE` | VARCHAR2 | YES |  |  |
| `DIRECCION_MZA` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
