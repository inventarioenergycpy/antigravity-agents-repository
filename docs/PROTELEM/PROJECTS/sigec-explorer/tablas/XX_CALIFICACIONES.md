---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: cobranza
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/cobranza
  - documentada/negocio
aliases:
  - "XX_CALIFICACIONES"
---

# 📋 XX_CALIFICACIONES

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[CONTRATOS]] | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK · 🔗 → [[CONTRATOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `PRS_NUMERO` | NUMBER | NO | 🔑 PK · 🔗 → [[PERSONAS]] | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `TCA_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `CAL_VALOR_CALCULADO` | NUMBER | NO |  |  |
| `CAL_FECHA_PROCESO` | DATE | NO | 🔑 PK |  |

## FK declaradas → otras tablas

- **CAL_CAL_FK**: `PRS_NUMERO` → [[PERSONAS]] (`PRS_NUMERO`)
- **CAL_FK**: `SRV_CODIGO`, `CNT_NUMERO` → [[CONTRATOS]] (`SRV_CODIGO`, `CNT_NUMERO`)
