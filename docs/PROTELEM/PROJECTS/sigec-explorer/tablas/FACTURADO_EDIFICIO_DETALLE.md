---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 69756
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "FACTURADO_EDIFICIO_DETALLE"
---

# 📋 FACTURADO_EDIFICIO_DETALLE

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 69,756

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `EDI_NUMERO` | NUMBER | YES |  |  |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `ZON_CODIGO` | VARCHAR2 | YES |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `TCL_GRUPO` | VARCHAR2 | YES |  | Grupo/rubro tarifario en TARIFAS. Mapea al sector de venta: 1=Residencial, 2=Comercial(Gral y Serv), 3=Industrial(Grandes Consumos), 4=Cooperativas, 5=Oficial(Gob y Us.Esp.), 6=Alumbrado Público, 7=Servicio de Agua, 8=Rural. Peaje y Uso Propio viven dentro del grupo 3 (identificar por TCL_DESCRIPCION). |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
