---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: documentos
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_DOC_RIO_TEMP"
---

# ⏱️ XXCO_DOC_RIO_TEMP

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `NRO_TRANSACION` | NUMBER | YES |  |  |
| `ID_REGISTRO` | VARCHAR2 | YES |  |  |
| `TIPO_REG` | VARCHAR2 | YES |  |  |
| `FECHA` | VARCHAR2 | YES |  |  |
| `MFP_FORMA_PAGO` | VARCHAR2 | YES |  |  |
| `MFP_IMPORTE` | NUMBER | YES |  |  |
| `FECHA_ACREDITACION` | VARCHAR2 | YES |  |  |
| `MARCA_ACRED` | VARCHAR2 | YES |  |  |
| `MARCA_CAMBIO_ESTADO` | VARCHAR2 | YES |  |  |
| `MARCA_PRIMERA_REND` | VARCHAR2 | YES |  |  |
| `URC_CODIGO_BANCO` | VARCHAR2 | YES |  |  |
| `MFP_SUCURSAL_CHEQUE` | NUMBER | YES |  |  |
| `MFP_NUMERO_CHEQUE` | VARCHAR2 | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `MOV_IMPORTE` | NUMBER | YES |  |  |
| `MOV_ARCHIVO_COBRANZA` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `MFP_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `DRT_CONVENIO` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
