---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: contratos
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/contratos
  - documentada/negocio
aliases:
  - "ARTEFACTOS"
---

# 📋 ARTEFACTOS

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TIA_CODIGO` | VARCHAR2 | NO | 🔑 PK |  |
| `ART_CANTIDAD` | NUMBER | NO |  |  |
