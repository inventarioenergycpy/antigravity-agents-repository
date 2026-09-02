---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 2015373
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "EXCESOS_A_FACTURAR"
---

# 📋 EXCESOS_A_FACTURAR

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 2,015,373

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `EAF_ANIO` | NUMBER | NO |  |  |
| `EAF_FRECUENCIA` | NUMBER | NO |  |  |
| `EAF_PERIODO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO | 🔗 → [[CONTRATOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔗 → [[CONTRATOS]] | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `EAF_CANTIDAD` | NUMBER | NO |  |  |
| `EAF_ESTADO` | VARCHAR2 | NO |  |  |
| `EAF_NUMERO` | NUMBER | NO |  |  |
| `EAF_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `EAF_FECHA_CARGA` | DATE | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `DOC_TIPO_APLICA` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_APLICA` | NUMBER | YES |  |  |
| `DOC_TIPO_GENERA` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO_GENERA` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **EAF_FK_CNT**: `SRV_CODIGO`, `CNT_NUMERO` → [[CONTRATOS]] (`SRV_CODIGO`, `CNT_NUMERO`)
