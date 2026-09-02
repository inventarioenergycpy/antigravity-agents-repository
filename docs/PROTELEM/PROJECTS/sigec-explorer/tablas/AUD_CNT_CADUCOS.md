---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 140857
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "AUD_CNT_CADUCOS"
---

# 📋 AUD_CNT_CADUCOS

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 140,857

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CODIGO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TRT_NUMERO` | NUMBER | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `ACC_FECHA_CARGA` | DATE | YES |  |  |
| `ACC_TOTAL_ADEUDADO` | NUMBER | YES |  |  |
| `PRS_DOCUMENTO` | NUMBER | YES |  | Número de documento del titular en PERSONAS (NUMBER), con PRS_TIPO_DOC ('DNI', 'LC', 'LE', 'CI'…). Distinto de PRS_CUIT (que a veces está y a veces no). Es el 'número de documento del titular' de una consulta comercial. |
| `PRS_CUIT` | NUMBER | YES |  |  |
| `ACC_TOTAL_A_FAVOR` | NUMBER | YES |  |  |
