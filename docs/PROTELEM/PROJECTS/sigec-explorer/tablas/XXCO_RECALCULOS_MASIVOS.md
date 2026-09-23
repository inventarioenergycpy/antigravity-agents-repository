---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 1470250
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_RECALCULOS_MASIVOS"
---

# 🔧 XXCO_RECALCULOS_MASIVOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 1,470,250

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `DOC_IMPORTE_BASICO` | NUMBER | YES |  | NO USAR como neto de la factura: coincide con DOC_IMPORTE_GRAVADO en solo el 70,6% y es MENOR en el 28,2% (muestra 322.120 docs de 2025). Poblada al 100% pero con semántica distinta al neto gravado. Para el neto usar DOC_IMPORTE_GRAVADO. |
| `SUBTOTAL_SIN_SUB_ORIG` | NUMBER | YES |  |  |
| `SUBTOTAL_CON_SUB_ORIG` | NUMBER | YES |  |  |
| `SEN_ORIGINAL` | NUMBER | YES |  |  |
| `CFE_ORIGINAL` | NUMBER | YES |  |  |
| `COS_ORIGINAL` | NUMBER | YES |  |  |
| `OTROS_ORIGINAL` | NUMBER | YES |  |  |
| `SUBTOTAL_SIN_SUB_RECALC` | NUMBER | YES |  |  |
| `SUBTOTAL_CON_SUB_RECALC` | NUMBER | YES |  |  |
| `SEN_RECALC` | NUMBER | YES |  |  |
| `CFE_RECALC` | NUMBER | YES |  |  |
| `COS_RECALC` | NUMBER | YES |  |  |
| `OTROS_RECALC` | NUMBER | YES |  |  |
| `DOC_SALDO_ACTUAL` | NUMBER | YES |  |  |
| `AJUSTE_AFB` | NUMBER | YES |  |  |
| `AJUSTE_CFE` | NUMBER | YES |  |  |
| `AJUSTE_COS` | NUMBER | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `DOC_TIPO_ORIGEN` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_ORIGEN` | NUMBER | YES |  |  |
| `TIENE_EXCESO_A_FAC` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `INSERTAR_IAF` | VARCHAR2 | YES |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `LCT_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `LCT_FECHA_LECTURA` | DATE | YES |  | Fecha en que se tomó la lectura. |
| `LCT_DIAS` | NUMBER | YES |  |  |
| `LCT_CONSUMO` | NUMBER | YES |  | Consumo calculado del período (diferencia entre lecturas). |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `AJUSTE_SEN` | NUMBER | YES |  |  |
| `CIE_ORIGINAL` | NUMBER | YES |  |  |
| `CIE_RECALC` | NUMBER | YES |  |  |
| `AJUSTE_CIE` | NUMBER | YES |  |  |
| `TIT_CLAVE_BONIFICACION` | VARCHAR2 | YES |  |  |
