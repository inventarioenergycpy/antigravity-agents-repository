---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: servicios
num_rows: 30435
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/servicios
  - documentada/negocio
aliases:
  - "DEUDA_DETALLE_TEMP"
---

# ⏱️ DEUDA_DETALLE_TEMP

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 30,435

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `CANTIDAD` | NUMBER | YES |  |  |
| `SALDO` | NUMBER | YES |  |  |
| `ESTADO` | VARCHAR2 | YES |  |  |
| `CRE_FECHA_CARGA` | DATE | YES |  |  |
| `PRS_DOCUMENTO` | NUMBER | YES |  | Número de documento del titular en PERSONAS (NUMBER), con PRS_TIPO_DOC ('DNI', 'LC', 'LE', 'CI'…). Distinto de PRS_CUIT (que a veces está y a veces no). Es el 'número de documento del titular' de una consulta comercial. |
| `PRS_CUIT` | NUMBER | YES |  |  |
