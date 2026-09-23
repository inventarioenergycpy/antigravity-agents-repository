---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 100460
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "OBSERVACIONES_SERVICIO"
---

# 📋 OBSERVACIONES_SERVICIO

**Filas estimadas:** 100,460

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `OSE_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `OSE_FECHA` | DATE | NO |  |  |
| `OSE_NOVEDAD` | VARCHAR2 | YES |  |  |
| `OSE_DETALLE` | VARCHAR2 | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
