---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 513383
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_CONSULTAS_CLIENTES"
---

# 🔧 XXCO_CONSULTAS_CLIENTES

**Filas estimadas:** 513,383

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CLC_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `CLC_USR_NUMERO_CARGA` | NUMBER | YES |  |  |
| `CLC_FECHA_INICIO` | DATE | YES |  |  |
| `CLC_FECHA_FIN` | DATE | YES |  |  |
| `CLC_MOTIVO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `CLC_TIPO_CONSULTA` | VARCHAR2 | YES |  |  |
