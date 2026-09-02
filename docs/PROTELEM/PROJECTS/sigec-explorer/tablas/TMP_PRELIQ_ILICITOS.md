---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 1269183
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "TMP_PRELIQ_ILICITOS"
---

# 📋 TMP_PRELIQ_ILICITOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 1,269,183

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `LIQ_NUMERO` | NUMBER | NO |  |  |
| `LIQ_FECHA` | DATE | NO |  |  |
| `LIQ_IMPORTE` | NUMBER | NO |  |  |
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |

## FK inferidas (alta confianza)

- `LIQ_NUMERO` → [[LIQUIDACIONES_ILICITOS]] _LIQ_NUMERO es PK de LIQUIDACIONES_ILICITOS_
