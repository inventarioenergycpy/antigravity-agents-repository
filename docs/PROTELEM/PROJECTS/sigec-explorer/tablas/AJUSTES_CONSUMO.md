---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "AJUSTES_CONSUMO"
---

# 📋 AJUSTES_CONSUMO

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ACO_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `ACO_FECHA` | DATE | NO |  |  |
| `ACO_DETALLE` | VARCHAR2 | YES |  |  |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `ACO_CONSUMO` | NUMBER | YES |  |  |
| `USR_NUMERO` | NUMBER | NO |  |  |
| `USR_NUMERO_AUTORIZADOR` | NUMBER | NO |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `ACO_ESTADO` | VARCHAR2 | NO |  |  |
