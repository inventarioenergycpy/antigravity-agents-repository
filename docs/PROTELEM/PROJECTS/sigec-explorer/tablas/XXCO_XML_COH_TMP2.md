---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_XML_COH_TMP2"
---

# 🔧 XXCO_XML_COH_TMP2

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ANIO` | NUMBER | YES |  |  |
| `MES` | NUMBER | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `CONSUMO` | NUMBER | YES |  |  |
| `TIPO_LECTURA` | VARCHAR2 | YES |  |  |
| `CANTIDAD_DIAS` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `ANIO_PERIODO` | NUMBER | YES |  |  |
