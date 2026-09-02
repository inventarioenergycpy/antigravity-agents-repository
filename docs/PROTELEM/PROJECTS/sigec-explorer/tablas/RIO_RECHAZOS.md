---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 257557
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "RIO_RECHAZOS"
---

# 📋 RIO_RECHAZOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 257,557

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `RRC_COD_RECIBIDO` | VARCHAR2 | NO |  |  |
| `RCR_COD_RECHAZO` | VARCHAR2 | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `RRE_FECHA_RECHAZO` | DATE | YES |  |  |
| `RBA_COD_BANCO` | NUMBER | YES |  |  |
| `RRE_IMPORTE` | NUMBER | YES |  |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_FINAN` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
