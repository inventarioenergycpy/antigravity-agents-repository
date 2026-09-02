---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 89640
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "FACTURADO"
---

# 📋 FACTURADO

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 89,640

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ZON_CODIGO` | VARCHAR2 | NO |  |  |
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `DOC_ANIO` | NUMBER | YES |  |  |
| `DOC_PERIODO` | NUMBER | YES |  | Período/ciclo de facturación de la boleta (1-12), junto con DOC_ANIO. TRAMPA CENTRAL: NO es el mes consumido. En 2025 el período es el mes de fin de consumo +1 en el 97,3% de las facturas (13.702.593 de 14,09M; +2 meses en 239.079 y 0 en 137.398); solo el 0,97% tiene DOC_FECHA_HASTA dentro del mes etiquetado. Contra la emisión el reparto es ~mitad y mitad: 48% se emite el mes anterior a la etiqueta y 46% en el mismo mes. Para 'lo facturado en el mes X' hay que elegir a propósito entre DOC_ANIO/DOC_PERIODO (ciclo), DOC_FECHA_EMISION (cuándo se facturó) y DOC_FECHA_DESDE/HASTA (qué días se consumieron). |
| `DOC_SITUACION` | VARCHAR2 | YES |  | Situacion del documento de deuda en DETALLE_SALDO. El valor 'G' = en Gestion Judicial y tiene correlacion 1:1 con FECHA_PASE_GJ (los 158.883 documentos con pase a GJ tienen DOC_SITUACION='G'): es el indicador equivalente y mas simple de usar. NO existe estado de retorno: 157.751 siguen con saldo pendiente, 1.132 sin SALDO_ACTUAL y CERO saldados. |
| `CANTIDAD` | NUMBER | YES |  |  |
| `DOC_IMPORTE` | NUMBER | YES |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `DOC_SALDO` | NUMBER | YES |  | Lo que queda PENDIENTE de cobro de ese documento, no lo facturado. Cero en el 97,3% de las facturas 2025 (13.707.392 de 14,09M). Para 'cuánto se le facturó' usar DOC_IMPORTE; DOC_SALDO responde 'cuánto debe'. |
| `CANTIDAD_ADEUDADO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
