---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 6612
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_RESUMEN_DEUDA_USR_TMP_1"
---

# 🔧 XXCO_RESUMEN_DEUDA_USR_TMP_1

**Filas estimadas:** 6,612

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `RAZON_SOCIAL` | VARCHAR2 | NO |  |  |
| `NRO_CLIENTE` | NUMBER | NO |  | Número de cliente en tablas EXT_VKO_* (integración externa). |
| `SUMINISTRO` | NUMBER | NO |  | Clave de punto de suministro con nombre corto sin prefijo (7 tablas de integración/TMP). |
| `CNT` | NUMBER | NO |  |  |
| `ETDO_CNT` | VARCHAR2 | NO |  |  |
| `TIPO_ENTE` | VARCHAR2 | YES |  |  |
| `COD_ENTE` | VARCHAR2 | NO |  |  |
| `ENTE` | VARCHAR2 | YES |  |  |
| `CANT_DOC_DEUDA` | NUMBER | YES |  |  |
| `SALDO_HISTORICO` | NUMBER | YES |  |  |
| `SALDO_ACTUALIZADO` | NUMBER | YES |  |  |
| `MENOR_F_VENC` | DATE | YES |  |  |
| `MAYOR_F_VENC` | DATE | YES |  |  |
| `DEUDA_NO_VENCIDA` | NUMBER | YES |  |  |
| `DEUDA_VENCIDA` | NUMBER | YES |  |  |
| `DEUDA_EN_GESTION_JUDICIAL` | NUMBER | YES |  |  |
| `TIENE_GARANTE` | CHAR | YES |  |  |
| `RC_CREDITOS` | NUMBER | YES |  |  |
| `DEP_EN_GARANTIA` | NUMBER | YES |  |  |
| `FACTURACIN_LTIMOS_3_MESES` | NUMBER | YES |  |  |
| `ULTIMO_PAGO_30_DAS` | DATE | YES |  |  |
| `IMPORTE_TOTAL_PAGO_30_DIAS` | NUMBER | YES |  |  |
| `ZONA` | VARCHAR2 | NO |  |  |
| `COD_DISTRITO` | NUMBER | NO |  |  |
| `DISTRITO` | VARCHAR2 | NO |  |  |
| `INTIMA` | VARCHAR2 | NO |  |  |
| `CORTE` | VARCHAR2 | NO |  |  |
| `RETIRO` | VARCHAR2 | NO |  |  |
| `F_TOPE_CORTE` | DATE | YES |  |  |
| `G_FACTRUACION` | VARCHAR2 | YES |  |  |
| `TIPO_CLIENTE` | VARCHAR2 | YES |  |  |
