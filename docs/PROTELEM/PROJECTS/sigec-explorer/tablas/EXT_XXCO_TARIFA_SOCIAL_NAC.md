---
tipo: tabla
categoria: base
owner: XXSIGEC
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "EXT_XXCO_TARIFA_SOCIAL_NAC"
---

# 📋 EXT_XXCO_TARIFA_SOCIAL_NAC

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ID_PERSONA` | NUMBER | YES |  |  |
| `DISTRIBUIDORA` | VARCHAR2 | YES |  |  |
| `TDOC_ORIG` | VARCHAR2 | YES |  |  |
| `NDOC_ORIG` | NUMBER | YES |  |  |
| `SEXO_ORIGINAL` | VARCHAR2 | YES |  |  |
| `APELLIDO_ORIG` | VARCHAR2 | YES |  |  |
| `NOMBRE_ORIG` | VARCHAR2 | YES |  |  |
| `CUIT_ORIG` | VARCHAR2 | YES |  |  |
| `SUMINISTRO` | VARCHAR2 | YES |  | Clave de punto de suministro con nombre corto sin prefijo (7 tablas de integración/TMP). |
| `CONSUMO` | VARCHAR2 | YES |  |  |
| `LOCALIDAD` | VARCHAR2 | YES |  |  |
| `BARRIO` | VARCHAR2 | YES |  |  |
| `DIRECCION` | VARCHAR2 | YES |  |  |
| `TEMATICA` | VARCHAR2 | YES |  |  |
| `ID_REGISTRO_ENVIO` | VARCHAR2 | YES |  |  |
| `ID_PEDIDO` | VARCHAR2 | YES |  |  |
