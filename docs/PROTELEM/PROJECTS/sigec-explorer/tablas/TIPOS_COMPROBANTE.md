---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 47
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "TIPOS_COMPROBANTE"
---

# 📋 TIPOS_COMPROBANTE

> [!info] Significado de negocio
> Catálogo de tipos de documento (PK DOC_TIPO → TCP_DESCRIPCION). Clave: F=FACTURA (definitiva), FP=FACTURA PROVISORIA (estimada, sin lectura — NO es energía facturada definitiva; excluir), C=NOTA DE CREDITO (TCP_SIGNO_CAJA=-1), D=NOTA DE DEBITO. Otros: RC recibo, NC/CV crédito, FA/FB factura comp. interno, etc.

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 47

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | NO | 🔑 PK |
| `TCP_DESCRIPCION` | VARCHAR2 | YES |  |
| `TCP_GRUPO` | VARCHAR2 | NO |  |
| `TCP_DEBE` | VARCHAR2 | NO |  |
| `TCP_NUMERO` | NUMBER | YES |  |
| `TCP_ORDEN` | NUMBER | YES |  |
| `TCP_IDENTIFICACION_CONTABLE` | VARCHAR2 | YES |  |
| `TCP_CODIGO` | VARCHAR2 | YES |  |
| `DOC_TIPO_CANCELADOR` | VARCHAR2 | YES |  |
| `TCP_PROXIMO_NUMERO` | NUMBER | YES |  |
| `TCP_MANUAL` | VARCHAR2 | YES |  |
| `TCP_SUBDIARIO` | NUMBER | YES |  |
| `TCP_AUXILIAR` | NUMBER | YES |  |
| `TCP_EXTERNO` | VARCHAR2 | YES |  |
| `TCP_APLICA` | VARCHAR2 | YES |  |
| `TCP_COPIAS` | NUMBER | YES |  |
| `TCP_TIPO` | VARCHAR2 | YES |  |
| `TCP_ESTADO` | VARCHAR2 | YES |  |
| `TCP_GENERICO` | VARCHAR2 | NO |  |
| `TCP_SIGNO_CAJA` | NUMBER | NO |  |
| `GTD_CODIGO` | VARCHAR2 | YES |  |
| `TCP_CONTABILIZA` | VARCHAR2 | YES |  |
| `TCP_GENERA_INTERESES` | VARCHAR2 | YES |  |
| `TCP_COBRA_VENCIDO` | VARCHAR2 | YES |  |
| `TCE_PUNTO_VENTA` | NUMBER | YES |  |
| `TCE_CODIGO` | VARCHAR2 | YES |  |
| `TCE_CODIGO_AUX` | VARCHAR2 | YES |  |
| `TCE_PUNTO_VENTA_AUX` | NUMBER | YES |  |

## FK inferidas (alta confianza)

- `TCE_PUNTO_VENTA` → [[XXCO_TIPOS_COMP_ELECTRONICO]] _TCE_PUNTO_VENTA es PK de XXCO_TIPOS_COMP_ELECTRONICO_
- `TCE_CODIGO` → [[XXCO_TIPOS_COMP_ELECTRONICO]] _TCE_CODIGO es PK de XXCO_TIPOS_COMP_ELECTRONICO_
