---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 364043
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "LIQUIDACIONES_ILICITOS"
---

# 📋 LIQUIDACIONES_ILICITOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 364,043

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LIQ_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `LIQ_FECHA` | DATE | YES |  |  |
| `LIQ_ESTADO` | VARCHAR2 | YES |  | Estado de la liquidacion de ilicito. A=194.247 (solo 3.292 con DOC_NUMERO), F=116.807 (116.802 con documento -> facturada), N=58.596 (importe promedio mas alto, 1,7M, casi sin documento), S=1.805 (sin actividad desde 2023). |
| `LIQ_IMPORTE` | NUMBER | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES | 🔗 → [[CONTRATOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES | 🔗 → [[CONTRATOS]] | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | YES | 🔗 → [[PERSONAS]] | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `TCL_CODIGO` | VARCHAR2 | YES | 🔗 → [[TARIFAS]] | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `LIQ_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **LIQ_CNT_FK**: `SRV_CODIGO`, `CNT_NUMERO` → [[CONTRATOS]] (`SRV_CODIGO`, `CNT_NUMERO`)
- **LIQ_PRS_FK**: `PRS_NUMERO` → [[PERSONAS]] (`PRS_NUMERO`)
- **LIQ_TCL_FK**: `TCL_CODIGO` → [[TARIFAS]] (`TCL_CODIGO`)

## Tablas que referencian esta tabla

- [[ITEMS_LIQUIDACIONES]] via `LIQ_NUMERO`
- [[RECLAMOS]] via `LIQ_NUMERO`
