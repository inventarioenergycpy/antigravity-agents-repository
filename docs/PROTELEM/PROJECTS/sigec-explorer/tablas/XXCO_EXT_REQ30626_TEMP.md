---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: contratos
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/contratos
  - documentada/negocio
aliases:
  - "XXCO_EXT_REQ30626_TEMP"
---

# ⏱️ XXCO_EXT_REQ30626_TEMP

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | VARCHAR2 | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | VARCHAR2 | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_COND_INTIMACION` | VARCHAR2 | YES |  | Flag S/N en CONTRATOS: si el contrato es intimable. S=3.705.652, N=53.615. CNT_FECHA_TOPE_INTIMAC casi no se usa (20 filas). |
| `CNT_COND_CORTE` | VARCHAR2 | YES |  |  |
| `CNT_COND_RETIRO` | VARCHAR2 | YES |  |  |
| `PERIODOS_RECLAMADOS` | VARCHAR2 | YES |  |  |
| `PERIODOS_RECLAMADOS2` | VARCHAR2 | YES |  |  |
| `PERIODOS_RECLAMADOS3` | VARCHAR2 | YES |  |  |
| `NRO_CONTROL` | VARCHAR2 | YES |  |  |
