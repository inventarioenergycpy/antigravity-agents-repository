---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 608360
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "AFIP_FELEC_VENTA_MENSUAL"
---

# 📋 AFIP_FELEC_VENTA_MENSUAL

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 608,360

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `DOC_FECHA_EMISION` | VARCHAR2 | YES |  |  |
| `TCE_CODIGO_AFIP` | NUMBER | YES |  |  |
| `TCE_PUNTO_VENTA` | NUMBER | YES |  |  |
| `TCE_NUMERO` | NUMBER | YES |  |  |
| `TIPO_DOCUMENTO_AFIP` | VARCHAR2 | YES |  |  |
| `NRO_DOCUMENTO` | NUMBER | YES |  |  |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | NO |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `DOC_IVV_CODIGO` | NUMBER | YES |  |  |
| `DOC_IMPORTE` | NUMBER | NO |  | Importe TOTAL facturado del documento, CON impuestos: es 'cuánto se le facturó al cliente'. Igual a DOC_IMPORTE_ORIGINAL en el 100% de las facturas 2025 (el _ORIGINAL solo diverge en documentos refinanciados). Se parte exactamente en DOC_IMPORTE_GRAVADO + DOC_IMPORTE_EXENTO (99,27%). Verificado contra el desglose de ITEMS: SUM(ITM_IMPORTE) lo reproduce al centavo en el 100% de la muestra. NO confundir con DOC_SALDO (pendiente) ni con DOC_IMPORTE_BASICO. |
| `FECHA_VENC_PAGO` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `TCE_PUNTO_VENTA` → [[XXCO_TIPOS_COMP_ELECTRONICO]] _TCE_PUNTO_VENTA es PK de XXCO_TIPOS_COMP_ELECTRONICO_
