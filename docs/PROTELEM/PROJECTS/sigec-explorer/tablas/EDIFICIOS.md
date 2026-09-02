---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 24873
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "EDIFICIOS"
---

# 📋 EDIFICIOS

**Filas estimadas:** 24,873

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `EDI_NUMERO` | NUMBER | NO |  |  |
| `EDI_NOMBRE` | VARCHAR2 | YES |  |  |
| `EDI_CALLE` | VARCHAR2 | YES |  |  |
| `EDI_NRO` | NUMBER | YES |  |  |
| `EDI_DIRECCION` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `EDI_FECHA_ALTA` | DATE | NO |  |  |
| `EDI_FECHA_CONEX` | DATE | YES |  |  |
| `EDI_FECHA_DESPACHO` | DATE | YES |  |  |
| `EDI_CANT_TORRES` | NUMBER | YES |  |  |
| `EDI_CANT_PISOS` | NUMBER | YES |  |  |
| `EDI_CANT_DEPTOS` | NUMBER | YES |  |  |
| `EDI_CANT_OFICINAS` | NUMBER | YES |  |  |
| `EDI_CANT_LOCALES` | NUMBER | YES |  |  |
| `EDI_CANT_SRV_GRALES` | NUMBER | YES |  |  |
| `EDI_DISTRITO_CAT` | NUMBER | YES |  |  |
| `EDI_ZONA_CAT` | NUMBER | YES |  |  |
| `EDI_MANZANA_CAT` | NUMBER | YES |  |  |
| `EDI_LOTE_CAT` | NUMBER | YES |  |  |
| `EDI_SUBESTACION` | VARCHAR2 | YES |  |  |
| `EDI_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `EDI_OBSERVACIONES_TEC` | VARCHAR2 | YES |  |  |
| `EDI_CORR_PCP` | VARCHAR2 | YES |  |  |
| `EDI_PAGO_PCP` | VARCHAR2 | YES |  |  |
| `EDI_CORR_PCT` | VARCHAR2 | YES |  |  |
| `EDI_PAGO_PCT` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `EDI_POTENCIA_KW` | NUMBER | YES |  |  |
| `EDI_SUP_TOTAL_M2` | NUMBER | YES |  |  |
| `EDI_PLAZO_EJECUCION` | NUMBER | YES |  |  |
| `EDI_CONTRIB_DONACION` | CHAR | YES |  |  |
| `EDI_CONTRIB_ECON` | CHAR | YES |  |  |
| `EDI_CONTRIB_FINAN` | CHAR | YES |  |  |
| `EDI_FEC_INICIO_DEV` | DATE | YES |  |  |
| `EDI_CUOTAS_DEV` | NUMBER | YES |  |  |
| `EDI_PRESUP_DEV` | NUMBER | YES |  |  |
| `EDI_OBSERVACIONES_DEV` | VARCHAR2 | YES |  |  |
| `EDI_DOCUMENTID_THUBAN` | VARCHAR2 | YES |  |  |
| `EDI_EXPTE_SUME` | VARCHAR2 | YES |  |  |
| `EDI_TELEMEDIBLE` | VARCHAR2 | YES |  |  |
| `EDI_TIPO` | VARCHAR2 | NO |  |  |
| `EDI_FECHA_REGISTRO` | DATE | YES |  |  |
| `ULT_PERIODO_INFORMADO` | DATE | YES |  |  |
| `ULT_PERIODO_INFORMADO_CEI` | DATE | YES |  |  |
| `EDI_PORC_MANT_Y_OPER_EPEC` | NUMBER | YES |  |  |
