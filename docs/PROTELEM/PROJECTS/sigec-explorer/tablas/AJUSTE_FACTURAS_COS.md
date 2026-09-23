---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 44427
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "AJUSTE_FACTURAS_COS"
---

# 📋 AJUSTE_FACTURAS_COS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 44,427

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `AFA_CANTIDAD_EA` | NUMBER | YES |  |  |
| `AFA_COEFICIENTE` | NUMBER | YES |  |  |
| `AFA_IMPORTE_AJUSTE` | NUMBER | YES |  |  |
| `AFA_ESTADO` | VARCHAR2 | YES |  |  |
| `AFA_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `AFA_FECHA_ALTA` | DATE | YES |  |  |
