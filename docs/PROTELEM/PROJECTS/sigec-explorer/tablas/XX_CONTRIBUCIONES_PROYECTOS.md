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
  - "XX_CONTRIBUCIONES_PROYECTOS"
---

# 📋 XX_CONTRIBUCIONES_PROYECTOS

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CPY_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `CNT_NUMERO` | NUMBER | YES | 🔗 → [[CONTRATOS]] | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SRV_CODIGO` | NUMBER | YES | 🔗 → [[CONTRATOS]] | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `PRS_NUMERO` | NUMBER | YES | 🔗 → [[PERSONAS]] | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PROJECT_NUMBER` | NUMBER | NO |  |  |
| `CPY_ESTADO` | VARCHAR2 | NO |  |  |
| `CPY_IMPORTE` | NUMBER | YES |  |  |
| `CPY_FECHA` | DATE | NO |  |  |
| `CPY_DEM_MAX_AUT` | NUMBER | YES |  |  |
| `CPY_FECHA_CUOTA` | DATE | YES |  |  |

## FK declaradas → otras tablas

- **CPY_CNT_FK**: `SRV_CODIGO`, `CNT_NUMERO` → [[CONTRATOS]] (`SRV_CODIGO`, `CNT_NUMERO`)
- **CPY_PER_FK**: `PRS_NUMERO` → [[PERSONAS]] (`PRS_NUMERO`)

## Tablas que referencian esta tabla

- [[XX_CONT_PROYECTOS_ITEM]] via `CPY_NUMERO`
