---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: documentos
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/documentos
  - documentada/negocio
aliases:
  - "CERTIFICADOS_DEUDA_JN"
---

# 📝 CERTIFICADOS_DEUDA_JN

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `CER_NUMERO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CER_DOC_SALDO_TOTAL` | NUMBER | NO |  |  |
| `CER_FECHA_GENERACION` | DATE | NO |  |  |
| `G_PRS_NUMERO` | NUMBER | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |  |
| `OBSERVACION` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
