---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 6253
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "DOC_ELEMENTOS_VARIOS"
---

# 📋 DOC_ELEMENTOS_VARIOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 6,253

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `DOC_FECHA_EMISION` | DATE | YES |  |  |
| `DEV_ESTADO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_FINAN` | NUMBER | YES |  |  |
| `DEV_CANT_CUOTAS` | NUMBER | YES |  |  |
| `DEV_CUOTA_ULT_CARGA` | NUMBER | YES |  |  |
| `DEV_FECHA_ULT_CARGA` | DATE | YES |  |  |
