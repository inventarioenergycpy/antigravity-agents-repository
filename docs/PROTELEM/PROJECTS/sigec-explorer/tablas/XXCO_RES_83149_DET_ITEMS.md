---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 3637127
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_RES_83149_DET_ITEMS"
---

# 🔧 XXCO_RES_83149_DET_ITEMS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 3,637,127

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ITM_NUMERO` | NUMBER | NO |  |  |
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `DOC_TIPO_ORIGEN_1` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_ORIGEN_1` | NUMBER | YES |  |  |
| `TIT_CLAVE` | VARCHAR2 | NO |  |  |
| `ITM_DETALLE` | VARCHAR2 | YES |  |  |
| `ITM_CANTIDAD` | NUMBER | YES |  |  |
| `ITM_PRECIO_UNIT` | NUMBER | YES |  |  |
| `ITM_IMPORTE` | NUMBER | NO |  |  |
| `ITM_SALDO` | NUMBER | YES |  |  |
| `ITM_MES_CONTABLE` | NUMBER | YES |  |  |
| `ITM_ESTADO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_ORIGEN` | NUMBER | YES |  |  |
| `DOC_TIPO_ORIGEN` | VARCHAR2 | YES |  |  |
| `ITM_VENC_NRO` | VARCHAR2 | YES |  |  |
| `ITM_SALDO_CANTIDAD` | NUMBER | YES |  |  |
| `ITM_DETALLE_IMPRESO` | VARCHAR2 | YES |  |  |
| `DOC_FECHA_EMISION` | DATE | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `TAB_NUMERO` | NUMBER | YES |  |  |
| `ITM_SECCION` | NUMBER | YES |  |  |
| `ITM_PRECIO_POR_IVA` | NUMBER | YES |  |  |
| `ITM_BASE_CALCULO` | NUMBER | YES |  |  |
| `ITM_PORCENTAJE` | NUMBER | YES |  |  |
| `ITM_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TIPO_CALCULO` | VARCHAR2 | YES |  |  |
| `ID_REPORTE` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ITM_NUMERO` → [[XX_INFORMES_PROCESOS_ITEMS]] _ITM_NUMERO es PK de XX_INFORMES_PROCESOS_ITEMS_
- `ID_REPORTE` → [[XXCO_RES_83149_DET]] _ID_REPORTE es PK de XXCO_RES_83149_DET_
