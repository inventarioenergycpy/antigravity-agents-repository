---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 103774233
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "ITEMS_A_FACTURAR"
---

# 📋 ITEMS_A_FACTURAR

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 103,774,233

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `IAF_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | NO | 🔗 → [[CONTRATOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔗 → [[CONTRATOS]] | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TIT_CLAVE` | VARCHAR2 | NO |  |  |
| `IAF_FECHA` | DATE | YES |  |  |
| `IAF_DETALLE` | VARCHAR2 | YES |  |  |
| `IAF_CANTIDAD` | NUMBER | YES |  |  |
| `IAF_PRECIO` | NUMBER | YES |  |  |
| `IAF_IMPORTE` | NUMBER | NO |  |  |
| `IAF_FACT_INMEDIATA` | VARCHAR2 | YES |  |  |
| `IAF_NUMERO_FINAN` | NUMBER | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `IAF_IMPORTE_FACTURADO` | NUMBER | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `USR_NUMERO_AUTORIZADOR` | NUMBER | YES |  |  |
| `IAF_ESTADO` | VARCHAR2 | NO |  |  |
| `IAF_DETALLE_IMPRESO` | VARCHAR2 | YES |  |  |
| `DOC_TIPO_AJUSTADO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_AJUSTADO` | NUMBER | YES |  |  |
| `IAF_ANIO` | NUMBER | YES |  |  |
| `IAF_PERIODO` | NUMBER | YES |  |  |
| `DOC_TIPO_GENERA` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_GENERA` | NUMBER | YES |  |  |
| `TRT_NUMERO` | NUMBER | YES |  |  |
| `IAF_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |

## FK declaradas → otras tablas

- **IAF_FK_CNT**: `SRV_CODIGO`, `CNT_NUMERO` → [[CONTRATOS]] (`SRV_CODIGO`, `CNT_NUMERO`)

## Tablas que referencian esta tabla

- [[XX_CONT_PROYECTOS_ITEM]] via `IAF_NUMERO`
