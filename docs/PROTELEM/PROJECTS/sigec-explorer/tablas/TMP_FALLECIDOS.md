---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 95180
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "TMP_FALLECIDOS"
---

# 📋 TMP_FALLECIDOS

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 95,180

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LINEA` | NUMBER | YES |  |  |
| `CUIT` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NRO` | NUMBER | YES |  |  |
| `NOMBRE` | VARCHAR2 | YES |  |  |
| `VERFAL` | VARCHAR2 | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `PRS_CUIT` | NUMBER | YES |  |  |
| `PRS_TIPO_DOC` | VARCHAR2 | YES |  |  |
| `PRS_DOCUMENTO` | NUMBER | YES |  | Número de documento del titular en PERSONAS (NUMBER), con PRS_TIPO_DOC ('DNI', 'LC', 'LE', 'CI'…). Distinto de PRS_CUIT (que a veces está y a veces no). Es el 'número de documento del titular' de una consulta comercial. |
| `CONTRATOS` | VARCHAR2 | YES |  |  |
| `SUMINISTRO` | NUMBER | YES |  | Clave de punto de suministro con nombre corto sin prefijo (7 tablas de integración/TMP). |
| `CONTRATO` | NUMBER | YES |  |  |
| `CONTRATOS_GARANTIZADOS` | VARCHAR2 | YES |  |  |
| `CNT_ESTADO` | VARCHAR2 | YES |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `DOC_NRO` → [[XXCO_DOC_CORREO_XML]] _DOC_NRO es PK de XXCO_DOC_CORREO_XML_
