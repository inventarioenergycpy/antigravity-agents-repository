---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 2126040
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "LECTURAS_DET"
---

# 📋 LECTURAS_DET

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 2,126,040

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LTD_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO |  |  |
| `EQP_ORDEN` | NUMBER | NO |  |  |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `LTD_FECHA_LECTURA` | DATE | NO |  |  |
| `LTD_VALOR_LEIDO` | NUMBER | NO |  |  |
| `LTD_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `LTD_VALOR_LEIDO_ANTERIOR` | NUMBER | YES |  |  |
| `LTD_CONSUMO` | NUMBER | YES |  |  |
| `LTD_CONSUMO_INFORMADO` | NUMBER | YES |  |  |
| `LTD_TIPO_CONSUMO` | VARCHAR2 | YES |  |  |
| `LTD_TIPO_LECTURA` | VARCHAR2 | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `LTD_ANORMALIDAD` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `LTD_ESTADO` | VARCHAR2 | YES |  |  |
| `LTD_ORIGEN` | VARCHAR2 | YES |  |  |
| `LTD_DIVIDIDA` | VARCHAR2 | YES |  |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `LTD_SALDO_CONSUMO` | NUMBER | YES |  |  |
| `LTD_SALDO_DIAS` | NUMBER | YES |  |  |
| `LTD_CUOTA` | NUMBER | YES |  |  |
| `LTD_ACTUALIZADO` | VARCHAR2 | YES |  |  |
| `LTD_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `LTD_MARCA_RESTAURACION` | NUMBER | YES |  |  |
| `USR_NUMERO_MODIFICA` | NUMBER | YES |  |  |
| `LTD_ENLACE_LEC` | NUMBER | YES |  |  |
| `LTD_FECHA_CARGA` | DATE | YES |  |  |
| `CRF_ANIO` | NUMBER | YES |  |  |
| `CRF_MES` | NUMBER | YES |  |  |
