---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 1528557
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_AJUSTE_ESTIMACION"
---

# 🔧 XXCO_AJUSTE_ESTIMACION

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 1,528,557

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `CRL_ANIO` | NUMBER | YES |  |  |
| `CRL_PERIODO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `CONSUMO` | NUMBER | YES |  |  |
| `DIAS` | NUMBER | YES |  |  |
| `CONSUMO_DIARIO` | NUMBER | YES |  |  |
| `CONSUMO_PRORRATEADO` | NUMBER | YES |  |  |
| `CONSUMO_DIARIO_PRORRATEADO` | NUMBER | YES |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `CRF_ANIO` | NUMBER | YES |  |  |
| `CRF_PERIODO` | NUMBER | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `LCT_FECHA_LECTURA` | DATE | YES |  | Fecha en que se tomó la lectura. |
| `LCT_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `APLICAR_AJUESTE` | VARCHAR2 | YES |  |  |
| `TIPO_ESTIMACION` | VARCHAR2 | YES |  |  |
| `IMPORTE_BASICO_FACTRUADO` | NUMBER | YES |  |  |
| `IMPORTE_BASICO_CALCULADO` | NUMBER | YES |  |  |
| `RESULTADO` | VARCHAR2 | YES |  |  |
| `DIFERENCIA_RESULTANTE` | NUMBER | YES |  |  |
| `FECHA_RESOLUCION` | DATE | YES |  |  |
| `IAF_NUMERO_1` | NUMBER | YES |  |  |
| `IAF_NUMERO_2` | NUMBER | YES |  |  |
| `IAF_NUMERO_3` | NUMBER | YES |  |  |
| `IAF_NUMERO_4` | NUMBER | YES |  |  |
