---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 13828
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "TARIFA_SOCIAL"
---

# 📋 TARIFA_SOCIAL

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 13,828

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `PRS_DOC_TIPO` | VARCHAR2 | YES |  |  |
| `PRS_DOC_NRO` | NUMBER | YES |  |  |
| `SRV_CALLE` | VARCHAR2 | YES |  |  |
| `SRV_NRO` | NUMBER | YES |  |  |
| `TAS_BARRIO` | VARCHAR2 | YES |  |  |
| `TAS_LOCALIDAD` | VARCHAR2 | YES |  |  |
| `TAS_RESOL_NRO` | NUMBER | YES |  |  |
| `TAS_RESOL_FECHA` | DATE | YES |  |  |
| `TAS_FECHA_CARGA` | DATE | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `TAS_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `TAS_COD_MOVIM` | NUMBER | YES |  |  |
| `TAS_FECHA_MOVIM` | DATE | YES |  |  |
| `TAS_ESTADO` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
