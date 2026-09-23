---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: contratos
num_rows: 20943
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/contratos
  - documentada/negocio
aliases:
  - "XXCO_INTERFASE_QUITA_SUB"
---

# 🔧 XXCO_INTERFASE_QUITA_SUB

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 20,943

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `IFS_FECHA_PROCESO` | DATE | YES |  |  |
| `P_CNT_FECHA_CBIO_COND_SUB` | DATE | YES |  |  |
| `IFS_FECHA_CARGA` | DATE | YES |  |  |
| `DOC_NUMERO_AJUSTADO` | VARCHAR2 | YES |  |  |
| `IAF_NUMERO` | NUMBER | YES |  |  |
| `CNT_CODIGO_ACTIVIDAD` | VARCHAR2 | YES |  |  |
