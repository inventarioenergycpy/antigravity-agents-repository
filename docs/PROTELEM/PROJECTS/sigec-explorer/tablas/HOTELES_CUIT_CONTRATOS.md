---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 557
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "HOTELES_CUIT_CONTRATOS"
---

# 📋 HOTELES_CUIT_CONTRATOS

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 557

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PRS_CUIT` | NUMBER | YES |  |  |
| `RAZON_SOCIAL` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_FECHA_INICIO` | DATE | NO |  |  |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
| `TAR_CNT` | VARCHAR2 | NO |  |  |
| `CLA_CNT` | VARCHAR2 | NO |  |  |
| `SRV_CALLE` | VARCHAR2 | YES |  |  |
| `SRV_NRO` | NUMBER | YES |  |  |
| `SRV_PISO` | VARCHAR2 | YES |  |  |
| `SRV_DEPTO` | VARCHAR2 | YES |  |  |
| `SRV_DIRECCION` | VARCHAR2 | YES |  |  |
