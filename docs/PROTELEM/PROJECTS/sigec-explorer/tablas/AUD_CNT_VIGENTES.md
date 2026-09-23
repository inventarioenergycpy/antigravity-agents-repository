---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 165147
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "AUD_CNT_VIGENTES"
---

# 📋 AUD_CNT_VIGENTES

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 165,147

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CODIGO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `ACV_FECHA_CARGA` | DATE | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `CREA_ORD` | VARCHAR2 | YES |  |  |
| `ACV_FECHA_ENVIO` | DATE | YES |  |  |
| `PRS_DOCUMENTO` | NUMBER | YES |  | Número de documento del titular en PERSONAS (NUMBER), con PRS_TIPO_DOC ('DNI', 'LC', 'LE', 'CI'…). Distinto de PRS_CUIT (que a veces está y a veces no). Es el 'número de documento del titular' de una consulta comercial. |
| `PRS_CUIT` | NUMBER | YES |  |  |
