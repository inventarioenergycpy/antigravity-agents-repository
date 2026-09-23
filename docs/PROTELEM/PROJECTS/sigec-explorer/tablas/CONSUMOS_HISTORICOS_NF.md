---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 26848
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "CONSUMOS_HISTORICOS_NF"
---

# 📋 CONSUMOS_HISTORICOS_NF

**Filas estimadas:** 26,848

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `COH_ANIO_PERIODO` | NUMBER | NO |  |  |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `COH_CONSUMO` | NUMBER | NO |  |  |
| `COH_FRECUENCIA` | NUMBER | NO |  |  |
| `COH_CANTIDAD_DIAS` | NUMBER | YES |  |  |
| `COH_TIPO_LECTURA` | VARCHAR2 | YES |  |  |
