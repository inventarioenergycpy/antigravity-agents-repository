---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 406
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_EXT_EPECOR"
---

# 🔧 XXCO_EXT_EPECOR

**Filas estimadas:** 406

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `IDVALIDAR` | VARCHAR2 | YES |  |  |
| `ADHESIONVOLUNTARIAID` | VARCHAR2 | YES |  |  |
| `IDDETALLEUSOINTERNO` | VARCHAR2 | YES |  |  |
| `TIPOSERVICIONOMBRE` | VARCHAR2 | YES |  |  |
| `DISTRIBUIDORANOMBRE` | VARCHAR2 | YES |  |  |
| `CONTACTONOMBRE` | VARCHAR2 | YES |  |  |
| `CONTACTOAPELLIDO` | VARCHAR2 | YES |  |  |
| `CONTACTOTELEFONOPARTICULAR` | VARCHAR2 | YES |  |  |
| `CONTACTOTELEFONOMOVIL` | VARCHAR2 | YES |  |  |
| `CONTACTOTELEFONOALTERNATIVO` | VARCHAR2 | YES |  |  |
| `CONTACTOEMAIL` | VARCHAR2 | YES |  |  |
| `TITULARDESCRIPCION` | VARCHAR2 | YES |  |  |
| `CALLE` | VARCHAR2 | YES |  |  |
| `CALLENUMERO` | VARCHAR2 | YES |  |  |
| `PISO` | VARCHAR2 | YES |  |  |
| `DEPATO` | VARCHAR2 | YES |  |  |
| `DATOSCOMPLEMENTARIOS` | VARCHAR2 | YES |  |  |
| `LOCALIDAD` | VARCHAR2 | YES |  |  |
| `CODIGOPOSTAL` | VARCHAR2 | YES |  |  |
| `PROVINCIANOMBRE` | VARCHAR2 | YES |  |  |
| `FECHAFINCONTRATO` | VARCHAR2 | YES |  |  |
| `TELEFONOPARTICULAR` | VARCHAR2 | YES |  |  |
| `TELEFONOMOVIL` | VARCHAR2 | YES |  |  |
| `TELEFONOALTERNATIVO` | VARCHAR2 | YES |  |  |
| `EMAIL` | VARCHAR2 | YES |  |  |
| `DETNOMBREUSUARIO` | VARCHAR2 | YES |  |  |
| `DETAPELLIDOUSUARIO` | VARCHAR2 | YES |  |  |
| `DETNUMDOCUMENTOUSUARIO` | VARCHAR2 | YES |  |  |
| `DETIDUSUARIO` | VARCHAR2 | YES |  |  |
| `DETNOMBREAPELLIDOTITULAR` | VARCHAR2 | YES |  |  |
| `ESTITULAR` | VARCHAR2 | YES |  |  |
| `SUB_ESTADO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
