---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 17753
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_NUEVOS_CONTATOS_WEB"
---

# 🔧 XXCO_NUEVOS_CONTATOS_WEB

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 17,753

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `NCW_NUMERO_CONSTANCIA` | NUMBER | YES |  |  |
| `NCW_FECHA_CARGA_INT` | DATE | YES |  |  |
| `NCW_FECHA_CARGA_WEB` | DATE | YES |  |  |
| `USR_NUMERO_GESTION` | NUMBER | YES |  |  |
| `NCW_FECHA_GESTION` | DATE | YES |  |  |
| `NCW_CODIGO_RECHAZO` | VARCHAR2 | YES |  |  |
| `NCW_AMPLIACION_RECHAZO` | VARCHAR2 | YES |  |  |
| `PRS_NUMERO` | VARCHAR2 | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `PRS_TIPO_DOC` | VARCHAR2 | YES |  |  |
| `PRS_DOCUMENTO` | VARCHAR2 | YES |  | Número de documento del titular en PERSONAS (NUMBER), con PRS_TIPO_DOC ('DNI', 'LC', 'LE', 'CI'…). Distinto de PRS_CUIT (que a veces está y a veces no). Es el 'número de documento del titular' de una consulta comercial. |
| `PRS_CUIT` | VARCHAR2 | YES |  |  |
| `PRS_MAIL` | VARCHAR2 | YES |  |  |
| `PRS_CALLE` | VARCHAR2 | YES |  |  |
| `PRS_NRO` | VARCHAR2 | YES |  |  |
| `PRS_PISO` | VARCHAR2 | YES |  |  |
| `PRS_DEPTO` | VARCHAR2 | YES |  |  |
| `PRS_LOCAL` | VARCHAR2 | YES |  |  |
| `PRS_TORRE` | VARCHAR2 | YES |  |  |
| `PRS_LOTE` | VARCHAR2 | YES |  |  |
| `PRS_MZNA` | VARCHAR2 | YES |  |  |
| `PRS_C_POSTAL` | VARCHAR2 | YES |  |  |
| `PRS_BARRIO` | VARCHAR2 | YES |  |  |
| `PRS_LOCALIDAD` | VARCHAR2 | YES |  |  |
| `PRS_PROVINCIA` | VARCHAR2 | YES |  |  |
| `PRS_TELEFONOS` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | VARCHAR2 | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `SRV_CALLE` | VARCHAR2 | YES |  |  |
| `SRV_NRO` | VARCHAR2 | YES |  |  |
| `SRV_PISO` | VARCHAR2 | YES |  |  |
| `SRV_DEPTO` | VARCHAR2 | YES |  |  |
| `SRV_LOCAL` | VARCHAR2 | YES |  |  |
| `SRV_TORRE` | VARCHAR2 | YES |  |  |
| `SRV_LOTE` | VARCHAR2 | YES |  |  |
| `SRV_MZNA` | VARCHAR2 | YES |  |  |
| `SRV_C_POSTAL` | VARCHAR2 | YES |  |  |
| `SRV_BARRIO` | VARCHAR2 | YES |  |  |
| `SRV_LOCALIDAD` | VARCHAR2 | YES |  |  |
| `SRV_PROVINCIA` | VARCHAR2 | YES |  |  |
| `SRV_DISTRITO_CATA` | VARCHAR2 | YES |  |  |
| `SRV_ZONA_CATA` | VARCHAR2 | YES |  |  |
| `SRV_MANZANA_CATA` | VARCHAR2 | YES |  |  |
| `SRV_LOTE_CATA` | VARCHAR2 | YES |  |  |
| `SRV_PH_CATA` | VARCHAR2 | YES |  |  |
| `CNT_NUMERO` | VARCHAR2 | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_ACTIVIDAD` | VARCHAR2 | YES |  |  |
| `CNT_ACTIVIDAD_SEC` | VARCHAR2 | YES |  |  |
| `CNT_CALLE` | VARCHAR2 | YES |  |  |
| `CNT_NRO` | VARCHAR2 | YES |  |  |
| `CNT_PISO` | VARCHAR2 | YES |  |  |
| `CNT_DEPTO` | VARCHAR2 | YES |  |  |
| `CNT_LOCAL` | VARCHAR2 | YES |  |  |
| `CNT_TORRE` | VARCHAR2 | YES |  |  |
| `CNT_LOTE` | VARCHAR2 | YES |  |  |
| `CNT_MZNA` | VARCHAR2 | YES |  |  |
| `CNT_C_POSTAL` | VARCHAR2 | YES |  |  |
| `CNT_BARRIO` | VARCHAR2 | YES |  |  |
| `CNT_LOCALIDAD` | VARCHAR2 | YES |  |  |
| `CNT_PROVINCIA` | VARCHAR2 | YES |  |  |
| `NCW_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `NCW_MEDIDOR` | VARCHAR2 | YES |  |  |
| `NCW_TIPO_MEDIDOR` | VARCHAR2 | YES |  |  |
| `CNT_TIPO_SUMINISTRO` | VARCHAR2 | YES |  |  |
| `NCW_FECHA_RECHAZO` | DATE | YES |  |  |
| `USR_NUMERO_RECHAZO` | NUMBER | YES |  |  |
| `SRV_CODIGO_GENERADO` | NUMBER | YES |  |  |
| `CNT_NUMERO_GENERADO` | NUMBER | YES |  |  |
