---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 46147
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_RECALC_TAR_SUB"
---

# 🔧 XXCO_RECALC_TAR_SUB

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 46,147

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `DOC_IMPORTE_BASICO` | NUMBER | YES |  | NO USAR como neto de la factura: coincide con DOC_IMPORTE_GRAVADO en solo el 70,6% y es MENOR en el 28,2% (muestra 322.120 docs de 2025). Poblada al 100% pero con semántica distinta al neto gravado. Para el neto usar DOC_IMPORTE_GRAVADO. |
| `DOC_IMPORTE_BASICO_REC` | NUMBER | YES |  |  |
| `ITM_IMPORTE_SUB` | NUMBER | YES |  |  |
| `CONSUMO` | NUMBER | YES |  |  |
| `DIAS` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CALCULO_SUBCIDIO` | VARCHAR2 | YES |  |  |
| `PERIODO` | NUMBER | YES |  |  |
| `IAF_NUMERO` | NUMBER | YES |  |  |
| `IAF_CPR_NUMERO` | NUMBER | YES |  |  |
