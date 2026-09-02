---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_RECLAMOS"
---

# 🔧 XXCO_RECLAMOS

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `REC_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `REC_MOTIVO` | VARCHAR2 | NO |  |  |
| `REC_FECHA_CARGA` | DATE | YES |  |  |
| `REC_FECHA_FIN_ESTIMADA` | DATE | YES |  |  |
| `REC_FECHA_FIN` | DATE | YES |  |  |
| `REC_FECHA_CIERRE` | DATE | YES |  |  |
| `TRT_NUMERO` | NUMBER | NO |  |  |
| `USR_NUMERO_CARGA` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `MRE_CODIGO` | VARCHAR2 | NO |  |  |
| `SEC_CODIGO` | VARCHAR2 | NO |  |  |
| `CLC_NUMERO` | NUMBER | YES |  |  |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
