---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 2
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "TRANSFERIDOS"
---

# 📋 TRANSFERIDOS

**Filas estimadas:** 2

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PLAN` | NUMBER | YES |  |  |
| `ZONA` | VARCHAR2 | YES |  |  |
| `LOCALI` | NUMBER | YES |  |  |
| `RUTA` | NUMBER | YES |  |  |
| `SUMI` | NUMBER | YES |  |  |
| `ZONA_NEW` | VARCHAR2 | YES |  |  |
| `LOCALI_NEW` | NUMBER | YES |  |  |
| `RUTA_NEW` | NUMBER | YES |  |  |
| `SUMI_NEW` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `FECHA_TRANSF` | DATE | YES |  |  |
