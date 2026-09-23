---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 1326803
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "RED_FACTURAS"
---

# 📋 RED_FACTURAS

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 1,326,803

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `RFA_FECHA_VTO_3` | DATE | YES |  |  |
| `RFA_FECHA_EMISION` | DATE | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `RFA_FECHA_VTO_1` | DATE | YES |  |  |
| `RFA_FECHA_VTO_2` | DATE | YES |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_2` | NUMBER | YES |  |  |
| `DOC_RECARGO_VENC_3` | NUMBER | YES |  |  |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `COD_BARRA` | VARCHAR2 | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `IVV_CODIGO` | NUMBER | YES |  |  |
| `MPA_TIPO` | VARCHAR2 | YES |  |  |
| `CNT_NUMERO_CUENTA` | VARCHAR2 | YES |  | NO es el número de contrato/cuenta comercial. Es el número de CUENTA BANCARIA o TARJETA para débito automático (VARCHAR2: 16 dígitos = tarjeta, 22 = CBU). Solo 122.016 de 3,74M filas de CONTRATOS lo tienen poblado (3,2%) y viene NULL en la mayoría de los suministros. En DOCUMENTOS también viene NULL. El identificador comercial es la PK (SRV_CODIGO, CNT_NUMERO). |
| `RFA_CARGA_TABLA` | DATE | YES |  |  |
