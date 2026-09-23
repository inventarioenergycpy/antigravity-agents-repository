---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: equipos
num_rows: 348390
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/equipos
  - documentada/negocio
aliases:
  - "ERRORES_EQUIPO"
---

# 📋 ERRORES_EQUIPO

**Prefijo `EQP_`:** Equipos instalados en puntos de medición (EQUIPOS)

**Filas estimadas:** 348,390

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `GRM_NUMERO` | NUMBER | NO |  |  |
| `EQP_ORDEN` | NUMBER | NO |  |  |
| `TRT_NUMERO` | NUMBER | NO |  |  |
| `EEQ_CANT_DEM_PERDIDA` | NUMBER | YES |  |  |
| `EEQ_CANT_DEM_VACIO` | NUMBER | YES |  |  |
| `EEQ_CANT_PUESTA_CERO` | NUMBER | YES |  |  |
| `EEQ_PORCENTAJE_ERROR` | NUMBER | YES |  |  |
| `EEQ_COMENTARIO` | VARCHAR2 | YES |  |  |
| `EEQ_LECTURA` | NUMBER | YES |  |  |
| `CDR_UNIDAD` | VARCHAR2 | NO |  |  |
| `EEQ_CARGA_MAXIMA` | NUMBER | YES |  |  |
| `EEQ_CARGA_MINIMA` | NUMBER | YES |  |  |
| `EQP_FACTOR_INTENSIDAD` | NUMBER | YES |  |  |
| `EQP_FACTOR_TENSION` | NUMBER | YES |  |  |
