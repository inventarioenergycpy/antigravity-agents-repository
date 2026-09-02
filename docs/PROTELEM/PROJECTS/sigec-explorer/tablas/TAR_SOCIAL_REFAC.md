---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 16184193
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "TAR_SOCIAL_REFAC"
---

# 📋 TAR_SOCIAL_REFAC

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 16,184,193

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `TAB_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `TEN_CODIGO` | VARCHAR2 | NO |  |  |
| `DOC_FECHA_EMISION` | DATE | YES |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | NO |  |  |
| `DOC_IMPORTE_BASICO` | NUMBER | YES |  | NO USAR como neto de la factura: coincide con DOC_IMPORTE_GRAVADO en solo el 70,6% y es MENOR en el 28,2% (muestra 322.120 docs de 2025). Poblada al 100% pero con semántica distinta al neto gravado. Para el neto usar DOC_IMPORTE_GRAVADO. |
| `DOC_IMPORTE` | NUMBER | YES |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `CANTIDAD_CFI` | NUMBER | YES |  |  |
| `CANTIDAD_BONIF` | NUMBER | YES |  |  |
| `CANTIDAD_ENE` | NUMBER | YES |  |  |
| `FECHA_REFAC` | DATE | YES |  |  |
| `ESTADO` | VARCHAR2 | YES |  |  |
| `DOC_IMPORTE_BASICO_NUEVO` | NUMBER | YES |  |  |
| `CANTIDAD_ENE_PROM` | NUMBER | YES |  |  |
| `DOC_FECHA_CALCULO` | DATE | YES |  |  |
| `TSR_FECHA_RECALCULO` | DATE | YES |  |  |
| `LCT_FECHA_LECTURA` | DATE | YES |  | Fecha en que se tomó la lectura. |
| `LCT_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `TSR_FECHA_CARGA` | DATE | YES |  |  |
| `DOC_IMPORTE_BASICO_NUEVO_RESID` | NUMBER | YES |  |  |
