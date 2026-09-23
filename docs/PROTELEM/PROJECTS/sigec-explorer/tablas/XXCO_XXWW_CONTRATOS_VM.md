---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 574377
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_XXWW_CONTRATOS_VM"
---

# 🔧 XXCO_XXWW_CONTRATOS_VM

**Filas estimadas:** 574,377

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `USU_ID` | NUMBER | NO | 🔑 PK |  |
| `PRS_NUMERO` | NUMBER | NO | 🔑 PK | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `FECHA` | DATE | YES |  |  |
| `ACEPTO` | CHAR | YES |  |  |
| `SERVICIO_ID` | NUMBER | NO | 🔑 PK |  |
| `REFERENCIA` | VARCHAR2 | NO |  |  |
| `USU_ORIGEN` | VARCHAR2 | YES |  |  |
| `RECIBE_FACTURA_IMPRESA` | VARCHAR2 | YES |  |  |
| `USU_ID_ES_TITULAR` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
