---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 425090
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "PAGOS_TEMPRANOS"
---

# 📋 PAGOS_TEMPRANOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 425,090

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DOC_TIPO` | VARCHAR2 | NO | 🔑 PK |  |
| `DOC_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | NO | 🔗 → [[CONTRATOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔗 → [[CONTRATOS]] | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PTE_FECHA_PAGO` | DATE | NO |  |  |
| `PTE_FECHA_VENC_1` | DATE | NO |  |  |
| `ASI_NUMERO` | NUMBER | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |

## FK declaradas → otras tablas

- **PTE_CORRESPONDER_A**: `SRV_CODIGO`, `CNT_NUMERO` → [[CONTRATOS]] (`SRV_CODIGO`, `CNT_NUMERO`)

## Tablas que referencian esta tabla

- [[DOCUMENTOS]] via `DOC_NUMERO`, `DOC_TIPO`
