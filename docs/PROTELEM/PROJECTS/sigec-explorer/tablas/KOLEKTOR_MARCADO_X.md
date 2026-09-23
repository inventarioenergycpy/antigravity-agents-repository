---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 130927
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "KOLEKTOR_MARCADO_X"
---

# 📋 KOLEKTOR_MARCADO_X

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 130,927

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `DOC_SITUACION_OLD` | VARCHAR2 | YES |  |  |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `CRE_SITUACION` | VARCHAR2 | YES |  |  |
| `CAPITAL_FACTURA` | VARCHAR2 | YES |  |  |
| `CRE_SALDO_INTIMADO` | NUMBER | YES |  |  |
