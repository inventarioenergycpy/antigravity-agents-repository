---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "XX_INTERFASE_PROYECTOS"
---

# 📋 XX_INTERFASE_PROYECTOS

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `IPR_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `PROJECT_NUMBER` | NUMBER | NO |  |  |
| `IPR_IMPORTE` | NUMBER | NO |  |  |
| `CNT_NUMERO` | NUMBER | YES | 🔗 → [[CONTRATOS]] | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SRV_CODIGO` | NUMBER | YES | 🔗 → [[CONTRATOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `IPR_PORCENTAJE_APORTE_FIN` | NUMBER | YES |  |  |
| `IPR_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `BUDGET_VERSION_ID` | NUMBER | YES |  |  |
| `BUDGET_TYPE_CODE` | VARCHAR2 | YES |  |  |
| `PROJECT_CALSS_CODE` | VARCHAR2 | YES |  |  |
| `IPR_STATUS` | VARCHAR2 | YES |  |  |
| `IPR_BUDJET_DUE_DATE` | DATE | YES |  |  |

## FK declaradas → otras tablas

- **IPR_CON2_FK**: `SRV_CODIGO`, `CNT_NUMERO` → [[CONTRATOS]] (`SRV_CODIGO`, `CNT_NUMERO`)
