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
  - "XXCO_XML_COH_TMP"
---

# ⏱️ XXCO_XML_COH_TMP

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ANIO` | NUMBER | YES |  |  |
| `MES` | NUMBER | YES |  |  |
| `CONSUMO` | NUMBER | YES |  |  |
| `COH_TIPO_LECTURA` | VARCHAR2 | YES |  |  |
| `COH_CANTIDAD_DIAS` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `COH_ANIO_PERIODO` | NUMBER | YES |  |  |
| `LIQUIDACION` | NUMBER | YES |  |  |
