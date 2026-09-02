---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 193
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "TEMP_IAF"
---

# 📋 TEMP_IAF

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 193

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TIT_CLAVE` | VARCHAR2 | YES |  |  |
| `IAF_FECHA` | DATE | YES |  |  |
| `IAF_DETALLE` | VARCHAR2 | YES |  |  |
| `IAF_IMPORTE` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `IAF_IMPORTE_FACTURADO` | NUMBER | YES |  |  |
| `IAF_ESTADO` | VARCHAR2 | YES |  |  |
| `DIFERENCIA` | NUMBER | YES |  |  |
